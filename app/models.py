from enum import Enum

class Suit(Enum):
    HEARTS = 0
    DIAMONDS = 1
    CLUBS = 2 
    SPADES = 3
    

class Card: 
    def __init__(self,suit:Suit,value:int)->None:
        if not isinstance(suit,Suit):
            raise TypeError("suit must be Suit")
        if value > 14 or value < 2:
            raise ValueError("value must be from 2-14")
        self.suit = suit
        self.value = value

    def __repr__(self):         
        return f"Card: suit={self.suit} value={self.value}"