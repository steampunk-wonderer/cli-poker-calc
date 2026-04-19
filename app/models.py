from enum import Enum

class Suit(Enum):
    HEARTS = 0
    DIAMONDS = 1
    CLUBS = 2 
    SPADES = 3

class Groups(Enum):
    BY_VALUE = 0
    BY_SUIT = 1
    
class Card: 
    def __init__(self,value:int,suit:Suit)->None:
        if not isinstance(suit,Suit):
            raise TypeError("suit must be Suit")
        if value > 14 or value < 2:
            raise ValueError("value must be from 2-14")
        if not isinstance(value,int):
            raise TypeError("value should be an int")
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
    
    def find_same_groups(self,group:Groups):
        if not isinstance(group,Groups):
            raise TypeError(f"group must be an instance of Groups class.Got {type(group)}")
        found = []
        pairs = []
        for i,card in enumerate(self):
            temp = []
            if card in found:
                continue
            found.append(card)
            for other_card in self[i+1:]:
                condition = False
                if group == Groups.BY_SUIT:
                    condition = card.suit == other_card.suit
                elif group == Groups.BY_VALUE:
                    condition = card.value == other_card.value

                if condition: 
                    if card not in temp:
                        temp.append(card)
                    temp.append(other_card)
                    found.append(other_card)
            if temp:
                pairs.append(CardCollection(temp))
        return pairs
 
    
    def find_same_value_groups(self):
        pass
    def find_same_suit_groups(self):
        pass 


    
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
