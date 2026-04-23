from enum import Enum
from collections.abc import Callable

class Suit(Enum):
    HEARTS = 0
    DIAMONDS = 1
    CLUBS = 2 
    SPADES = 3

class Groups(Enum):
    BY_VALUE = 0
    BY_SUIT = 1
    BY_SEQUENCE = 2

class SortKey(Enum):
    SUIT = 0
    VALUE = 1

class HandRank(Enum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9

    


    
class Card: 
    def __init__(self,value:int,suit:Suit)->None:
        if not isinstance(suit,Suit):
            raise TypeError(f"suit:{suit} must be Suit")
        if value > 14 or value < 2:
            raise ValueError(f"value:{value} must be from 2-14")
        if not isinstance(value,int):
            raise TypeError(f"value:{value} should be an int")
        self.suit = suit
        self.value = value

    def __repr__(self):         
        return f"Card{{suit={self.suit.name} value={self.value}}}"

    def __eq__(self,other):
        if not isinstance(other,Card):
            return NotImplemented
        return self.value == other.value and self.suit == other.suit
    
class CardCollection: 
    def __init__(self,cards:list[Card]):
        if not isinstance(cards,list):
            raise ValueError(f"must provide list of Card instances.Instead got {type(cards)}")
        for card in cards: 
            if not isinstance(card,Card):
                raise ValueError(f"items in list must be instances of Card class.Instead got {type(card)}")
        self.cards = list(cards)
    
    def to_values(self):
        return [card.value for card in self.cards]

    def to_suits(self):
        return [card.suit for card in self.cards]
    
    def sort_by_value(self,reverse=False):
        return CardCollection(sorted(self.cards,key=lambda x:x.value,reverse=reverse))

    def _find_groups_by_key(self,key_func):
        found = []
        pairs = []
        for i,card in enumerate(self):
            temp = []
            if card in found:
                continue
            found.append(card)
            for other_card in self[i+1:]:
                if key_func(card) == key_func(other_card): 
                    if card not in temp:
                        temp.append(card)
                    temp.append(other_card)
                    found.append(other_card)
            if temp:
                pairs.append(CardCollection(temp))
        return pairs
    
    def find_value_groups(self):
        return self._find_groups_by_key(lambda x:x.value)

    def find_suit_groups(self):
        return self._find_groups_by_key(lambda x:x.suit)

    def find_sequences(self)->list[list[Card]]:
        sorted_cards = self.sort_by_value()
        results = []
        found = []
        for i,card in enumerate(sorted_cards):
            if card in found:
                continue
            real_length = 1
            found.append(card)
            temp = [card]
            value = card.value
            for other_card in sorted_cards[i+1:]:
                if other_card.value == value + 1 or other_card.value == value:
                    found.append(other_card)
                    temp.append(other_card)
                    if other_card.value == value + 1:
                        real_length += 1
                        value += 1 
                else: 
                    break
            if real_length >= 5:
                results.append(CardCollection(temp))
        return results

    def find_best_hand(self):
        best_comb = []
        groups_suits = self.find_suit_groups()
        group_values = self.find_value_groups()

        fours_groups = filter_groups(group_values,lambda item:len(item) ,4)
        threes_groups = filter_groups(group_values,lambda item:len(item),3)
        twos_groups = filter_groups(group_values,lambda item:len(item),2)
        suits_count = count_suits(self)
        tiebreakers = tuple()

        #----------------------------------------#
        #STRAIGHT FLUSH
        for group_suit in groups_suits:
            if len(group_suit) < 5:
                continue 
            sequences = group_suit.find_sequences()
            best_comb.extend(sequences)
        if best_comb: 
            best = max(best_comb,key=lambda x:max(y.value for y in x))
            best = list(card for card in reversed(best))[:5]
            tiebreakers = tuple(card.value for card in best)
            return EvaluatedHand(HandRank.STRAIGHT_FLUSH,best,tiebreakers)
        #----------------------------------------#
        #FOUR OF KIND
        if fours_groups:
            best_comb.append(max(fours_groups,key=lambda x:x[0].value))
            quad_value = best_comb[0][0].value
            remaining_values = [card.value for card in self if card.value != quad_value]
            kicker = max(remaining_values)
            tiebreakers = (quad_value, kicker)
            return EvaluatedHand(HandRank.FOUR_OF_A_KIND,best_comb,tiebreakers)
        #----------------------------------------#
        #FULL HOUSE  
        condition_1 = threes_groups and twos_groups
        condition_2 = len(threes_groups) >= 2 
        if condition_1 or condition_2:
            if condition_1:
                best_comb.append(threes_groups[0]) # can only have one threes 
                best_comb.append(max(twos_groups,key=lambda x:x[0].value))
                
            elif condition_2 : 
                if threes_groups[0][0].value > threes_groups[1][0].value:
                    best_comb.append(threes_groups[0])
                    best_comb.append([threes_groups[1][0],threes_groups[1][1]])
                else:
                    best_comb.append(threes_groups[1])
                    best_comb.append([threes_groups[0][0],threes_groups[0][1]])
            tiebreakers = (best_comb[0][0].value,best_comb[1][0].value)   

            return EvaluatedHand(HandRank.FULL_HOUSE,best_comb,tiebreakers)
        #----------------------------------------#
        #FLUSH
        for suit in suits_count:
            if suits_count[suit] >= 5 : 
                cards_with_suit = filter_groups(self,lambda item:item.suit,suit)
                best_comb = sorted(cards_with_suit,key=lambda x:x.value,reverse=True)[:5]
                tiebreakers = tuple(card.value for card in best_comb)
                return EvaluatedHand(HandRank.FLUSH,best_comb,tiebreakers)

        #----------------------------------------#
        #STRAIGHT
        sequences = self.find_sequences()
        if sequences:
            best_sequence = max(sequences,key=lambda x: max(x,key=lambda y:y.value))
            filtered = []
            found_values = []
            for card in best_sequence:
                temp_val = card.value 
                if temp_val not in found_values : 
                    found_values.append(temp_val)
                    filtered.append(card)
            
            best_comb = list(reversed(filtered[-5:]))
            tiebreakers = tuple(card.value for card in best_comb)
            return EvaluatedHand(HandRank.STRAIGHT,best_comb,tiebreakers)
        #----------------------------------------#
        #THREE OF KIND
        if threes_groups:
            best_comb = max(threes_groups,key=lambda x:x[0].value) #can have only one . not necessary to use max function. if there were two we would have full house
            sorted_cards = sorted(self,key=lambda x:x.value,reverse=True) 
            three_rank = best_comb[0].value
            rest_of_cards = list(filter(lambda x:x.value != three_rank,sorted_cards) )
            tiebreakers = (three_rank,rest_of_cards[0].value,rest_of_cards[1].value)
            return EvaluatedHand(HandRank.THREE_OF_A_KIND,best_comb,tiebreakers)
        #----------------------------------------#
        # TWO PAIRS
        if twos_groups:
            sorted_cards = sorted(self,key=lambda card:card.value,reverse=True)
            if len(twos_groups) >= 2 : 
                sorted_pairs = sorted(twos_groups,key=lambda x:x[0].value,reverse=True)
                best_comb.append(sorted_pairs[0])
                best_comb.append(sorted_pairs[1])
                rank_1 = best_comb[0][0].value
                rank_2 = best_comb[1][0].value 
                sorted_rest_cards = list(filter(lambda card:card.value != rank_1 and card.value != rank_2,sorted_cards ))
                tiebreakers = (rank_1,rank_2,sorted_rest_cards[0].value)
                return EvaluatedHand(HandRank.TWO_PAIR,best_comb,tiebreakers)
            else:
                best_comb.append(twos_groups[0])
                rank = best_comb[0][0].value
                sorted_rest_cards = list(filter(lambda card:card.value != rank,sorted_cards ))
                tiebreakers = (rank,sorted_rest_cards[0].value,sorted_rest_cards[1].value,sorted_rest_cards[2].value)
                return EvaluatedHand(HandRank.PAIR,best_comb,tiebreakers)
            
        #----------------------------------------#
        #HIGH CARD
        sorted_cards = sorted(self,key=lambda x:x.value,reverse=True)
        best_comb.append(sorted_cards[0])
        tiebreakers = tuple(card.value for card in sorted_cards[:5])
        return EvaluatedHand(HandRank.HIGH_CARD,best_comb,tiebreakers)
    
    def __getitem__(self, key):
        return self.cards[key]

    def __len__(self):
        return len(self.cards)
    
    def __iter__(self):
        return iter(self.cards)
    
    def __add__(self,other):
        if not isinstance(other,CardCollection):
            return NotImplemented
        return CardCollection(self.cards + other.cards)
    
    def __repr__(self):
        result = "CardCollection["
        for i,card_obj in enumerate(self.cards): 
            result += card_obj.__repr__()
            if i != len(self.cards) - 1:
                result += ', '
        result += ']'
        return result
    
    def __eq__(self,other):
        if not isinstance(other,CardCollection):
            return NotImplemented
        if len(self) != len(other):
            return False
        for i,card in enumerate(self):
            if card != other[i]:
                return False
        return True
    
class EvaluatedHand:
    def __init__(self,rank:HandRank,cards,tiebreakers:tuple[int, ...]):
        self.rank = rank
        self.cards = cards
        self.tiebreakers = tiebreakers

    def __lt__(self,other):
        if not isinstance(other,EvaluatedHand):
            return NotImplemented
        return (self.rank.value, self.tiebreakers) < (other.rank.value, other.tiebreakers)
    
    def __gt__(self,other):
        if not isinstance(other,EvaluatedHand):
            return NotImplemented
        return (self.rank.value, self.tiebreakers) > (other.rank.value, other.tiebreakers)
    
    def __repr__(self):
        return f"EvaluatedCard{{rank:{self.rank},\n cards:{self.cards},\n tiebreakers:{self.tiebreakers}}}"






#FUNCTIONS
def is_flush(card_list:list[Card])->bool:
    s = card_list[0].suit
    print('s',s)
    for card in card_list[1:]:
        if card.suit != s:
            return False
    return True

def count_suits(card_list:list[Card])->dict[Suit,int]:
    results = {}
    for card in card_list:
        suit = card.suit
        if suit not in results:
            results[suit] = 0
        results[suit] += 1 
    return results

def filter_groups(group:list["CardCollection"],key:Callable,value)->list["CardCollection"]:
    lst = []
    if group:
        for item in group: 
            if key(item) == value:
                lst.append(item)
    return lst 
    

