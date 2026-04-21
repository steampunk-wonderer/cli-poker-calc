from enum import Enum

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
        groups_suits = self.find_suit_groups()
        group_values = self.find_value_groups()
        fours_groups = filter_groups(group_values,4)
        threes_groups = filter_groups(group_values,3)
        twos_groups = filter_groups(group_values,2)

        print("group values:",group_values)
        #----------------------------------------#
        #STRAIGHT FLUSH
        straight_flushes = []
        for group_suit in groups_suits:
            if len(group_suit) < 5:
                continue 
            sequences = group_suit.find_sequences()
            straight_flushes.extend(sequences)
        if straight_flushes: 
            best = max(straight_flushes,key=lambda x:max(y.value for y in x))
            # best = straight_flushes[0]
            # high_card = best[-1].value
            # for temp in straight_flushes[1:]:
            #     if temp[-1].value > high_card:
            #         best = temp
            #         high_card = best[-1].value
            print("straight flush!")
            print('best : ',best)
        #----------------------------------------#
        #FOUR OF KIND
        four_of_kind = []
        if fours_groups:
            four_of_kind.append(max(fours_groups,key=lambda x:x[0].value))
            print("four of kind : ",four_of_kind)
            print('four of kind !')
        #----------------------------------------#
        #FULL HOUSE  
        condition_1 = threes_groups and twos_groups
        condition_2 = len(threes_groups) >= 2 
        if  condition_1 or condition_2:
            print("full house !")
            full_house = []
            if condition_1:
                full_house.append(threes_groups[0]) # can only have one because max cards are 7
                best_two = twos_groups[0]
                








        
    

    
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

def filter_groups(groups:list["CardCollection"],group_len:int)->list["CardCollection"]:
    lst = []
    if groups:
        for group in groups: 
            if len(group) == group_len:
                lst.append(group)
    return lst 
    

