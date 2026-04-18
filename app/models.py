from enum import Enum

class Suit(Enum):
    HEARTS = 0
    DIAMONDS = 1
    CLUBS = 2 
    SPADES = 3
    
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
        return f"suit={self.suit.name} value={self.value}"

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
    
    def __repr__(self):
        result = "["
        for card_obj in self.cards: 
            result += card_obj.__repr__()
            result += ', '
        result += ']'
        return result
    
    def to_values(self):
        return [card.value for card in self.cards]

    def to_suits(self):
        return [card.suit for card in self.cards]
    
    def __getitem__(self, key):
        return self.cards[key]

    def __len__(self):
        return len(self.cards)
    
    def __iter__(self):
        return iter(self.cards)