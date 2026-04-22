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
        print("group values",group_values)

        fours_groups = filter_groups(group_values,lambda item:len(item) ,4)
        print("fours groups",fours_groups)
        threes_groups = filter_groups(group_values,lambda item:len(item),3)
        twos_groups = filter_groups(group_values,lambda item:len(item),2)
        suits_count = count_suits(self)

        print("group values:",group_values)
        print("twos groups",twos_groups)
        print("threes groups:",threes_groups)
        print("fours groups",fours_groups)
        #----------------------------------------#
        #STRAIGHT FLUSH
        for group_suit in groups_suits:
            if len(group_suit) < 5:
                continue 
            sequences = group_suit.find_sequences()
            best_comb.extend(sequences)
        if best_comb: 
            best = max(best_comb,key=lambda x:max(y.value for y in x))
            print("straight flush!")
            print('best : ',best)
            return
        #----------------------------------------#
        #FOUR OF KIND
        if fours_groups:
            best_comb.append(max(fours_groups,key=lambda x:x[0].value))
            print("four of kind : ",best_comb)
            print('four of kind !')
            return
        #----------------------------------------#
        #FULL HOUSE  
        condition_1 = threes_groups and twos_groups
        condition_2 = len(threes_groups) >= 2 
        if condition_1 or condition_2:
            print('gjfodhgoasduoghoasghodhoasghuoi')
            if condition_1:
                print("condition 1 ")
                best_comb.append(threes_groups[0]) # can only have one threes 
                best_comb.append(max(twos_groups,key=lambda x:x[0].value))
            elif condition_2 : 
                print("condition 2 ")
                if threes_groups[0][0].value > threes_groups[1][0].value:
                    best_comb.append(threes_groups[0])
                    best_comb.append([threes_groups[1][0],threes_groups[1][1]])
                else:
                    best_comb.append(threes_groups[1])
                    best_comb.append([threes_groups[0][0],threes_groups[0][1]])
            print("full house:",best_comb)
            return
        #----------------------------------------#
        #FLUSH
        print('self',self)
        print('suits_count',suits_count)
        for suit in suits_count:
            if suits_count[suit] >= 5 : 
                print("FLUSH")
                cards_with_suit = filter_groups(self,lambda item:item.suit,suit)
                print("cards with suits:",cards_with_suit)
                best_comb.append(sorted(cards_with_suit,key=lambda x:x.value,reverse=True)[:5])
                print("flush:",best_comb)
                return 
        #----------------------------------------#
        #STRAIGHT
        sequences = self.find_sequences()
        print("----------------------")
        print("sequences:",sequences)
        if sequences:
            best_sequence = max(sequences,key=lambda x: max(x,key=lambda y:y.value))
            # print("best : ",best)
            filtered = []
            found_values = []
            for card in best_sequence:
                print("card",card)
                temp_val = card.value 
                if temp_val not in found_values : 
                    found_values.append(temp_val)
                    filtered.append(card)
            
            print("filtered: ",filtered)
            best_comb = filtered[-5:]
            print("best_comb:",best_comb)
            return
        #----------------------------------------#
        #THREE OF KIND
        if threes_groups:
            best_comb = max(threes_groups,key=lambda x:x[0].value) #can have only one . not necessary to use max function. if there were two we would have full house 
            print("threes :",best_comb)
            return
        



        







            
                








        
    

    
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

def filter_groups(group:list["CardCollection"],key:Callable,value)->list["CardCollection"]:
    lst = []
    if group:
        for item in group: 
            if key(item) == value:
                lst.append(item)
    return lst 
    

