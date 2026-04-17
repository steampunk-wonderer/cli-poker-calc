import argparse
from app.models import Suit
import re

values_dict = { 
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'J':11,
    'Q':12,
    'K':13,
    'A':14,
}

suits_dict = { 
    'h':Suit.HEARTS,
    'c':Suit.CLUBS,
    's':Suit.SPADES,
    'd':Suit.DIAMONDS
}

def full_string_to_card_strings(full_str:str)->list[str]:
    """
    10s7cQh2cAh -> [10s,7c,Qh,2c,Ah]
    """
    if not full_str: 
        raise ValueError(f"Invalid full_str:{full_str}")
    if not isinstance(full_str,str): 
        raise TypeError(f"full_str:{full_str} must be a string got {type(full_str)}")
    
    #regex pattern validation
    values_group = "|".join(values_dict.keys())
    print('values_group',values_group)
    suits_group = "".join(suits_dict.keys())
    print('suits_group',suits_group)

    validation_pattern = rf"^(({values_group})([{suits_group}]))+$"
    if not re.fullmatch(validation_pattern,full_str): 
        raise ValueError(f"Invalid card sequence '{full_str}'. Expected one or more cards in the form rank+suit like 'AhKd10s'")


    pattern = rf"[{suits_group}]"


    matches = re.finditer(pattern,full_str)

    indexes_suits = [m.start() for m in matches]
    indexes_suits = [-1] + indexes_suits
    card_strings = []
    for i in range(0,len(indexes_suits)-1): 
        card_str = full_str[indexes_suits[i]+1:indexes_suits[i+1]+1]
        card_strings.append(card_str)
    print(card_strings)
    return card_strings


    
    

def card_string_to_single_Card(card_string:str):
    print("card_string_to_Card function running")
    if not card_string:
        raise ValueError(f"Invalid card_string:{card_string}")
    if not isinstance(card_string,str):
        raise TypeError(f"card_string:{card_string} must be a string")
    card_string = card_string.strip()
    if len(card_string) != 2 or len(card_string) !=3 : 
        raise ValueError(f"card_string:{card_string} must have len 2 or 3")
    if card_string[-1] not in suits_dict or card_string[:-1] not in values_dict: 
        raise ValueError(f"card_string:{card_string} must be valuesuit like 2h")
    
    suit_str = card_string[-1]
    value_str = card_string[:-1]
    print('suit_str: ',suit_str)
    print('value_str: ',value_str)
     
def parse_game_input(args:argparse.Namespace): 
    print("inside the parse_game_input function")
    print("args: ",args)
    players = args.players
    player_cards = args.player_cards
    other_players_cards = args.other_players_cards
    community_cards = args.community_cards
    #PLAYER CARDS
    # card_string_to_Card(player_cards)

