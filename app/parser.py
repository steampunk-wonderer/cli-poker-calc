import argparse
from app.models import Suit,Card
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

values_group = "|".join(values_dict.keys())
suits_group = "".join(suits_dict.keys())
#############################################################
#############################################################
def full_string_to_card_strings(full_str:str,no_duplicates=True)->list[str]:
    """
    10s7cQh2cAh -> [10s,7c,Qh,2c,Ah]
    """
    full_str = full_str.replace(" ","")

    if not full_str: 
        raise ValueError(f"Invalid full_str:{full_str}")
    if not isinstance(full_str,str): 
        raise TypeError(f"full_str:{full_str} must be a string got {type(full_str)}")
    
    #regex pattern validation
    validation_pattern = rf"^(({values_group})([{suits_group}]))+$"
    if not re.fullmatch(validation_pattern,full_str): 
        raise ValueError(f"Invalid card sequence '{full_str}'. Expected one or more cards in the form rank+suit with valid ranks and suits like 'AhKd10s'")


    pattern = rf"[{suits_group}]"
    matches = re.finditer(pattern,full_str)

    indexes_suits = [m.start() for m in matches]
    indexes_suits = [-1] + indexes_suits
    card_strings = []
    for i in range(0,len(indexes_suits)-1): 
        card_str = full_str[indexes_suits[i]+1:indexes_suits[i+1]+1]
        if no_duplicates and card_str in card_strings: 
            raise ValueError("no duplicate cards allowed")
        card_strings.append(card_str)
    
    # print(card_strings)
    return card_strings

def card_string_to_single_Card(card_string:str)->Card:
    """
    Kh -> Card.value=13 , Card.suit=Suit.HEARTS
    """

    if not card_string:
        raise ValueError(f"Invalid card_string:{card_string}")
    if not isinstance(card_string,str):
        raise TypeError(f"card_string:{card_string} must be a string")

    card_string = card_string.replace(" ","")
    validation_pattern = rf"({values_group})[{suits_group}]"
    if not re.fullmatch(validation_pattern,card_string):
        raise ValueError(f"card_string:{card_string} is not of format valuesuit like Kh")
    
    suit_str = card_string[-1]
    value_str = card_string[:-1]
    return Card(values_dict[value_str],suits_dict[suit_str])
     
def parse_game_input(args:argparse.Namespace): 
    print("-----------------------------")
    print("-----------------------------")
    print("inside the parse_game_input function")
    players = args.players
    if not players: 
        raise ValueError("must provide number of players")
    if players < 1 or players > 6: 
        raise ValueError("players must be between and including 1 and 6 ")
    #CHECKS FOR STRING ARE IN full_string_to_card_strings
    player_cards = args.player_cards
    other_players_cards = args.other_players_cards
    print("other players cards: ",other_players_cards)
    community_cards = args.community_cards
    duplicate_cards = []
    #-----------------------------------------------#
    #PLAYER CARDS
    player_cards_list = full_string_to_card_strings(player_cards)
    if len(player_cards_list) > 2 : 
        raise ValueError("number of player cards cannot exceed 2")
    player_cards = []
    for my_str in player_cards_list:
        local_card = card_string_to_single_Card(my_str)
        for duplicate in duplicate_cards: 
            if duplicate == local_card:
                raise ValueError("duplicate card")
        duplicate_cards.append(local_card)
        player_cards.append(local_card)

    #-----------------------------------------------#
    #OTHER PLAYER CARDS
    other_players_cards_list = []
    for cards in other_players_cards:
        temp_player_cards = []
        single_player_cards = full_string_to_card_strings(cards)
        if len(single_player_cards) > 2:
            raise ValueError("a player can have max 2 cards")
        print('single player cards:',single_player_cards)
        for card in single_player_cards:
            local_card = card_string_to_single_Card(card)
            for duplicate in duplicate_cards: 
                if duplicate == local_card:
                    raise ValueError("duplicate card")
            duplicate_cards.append(local_card)
            temp_player_cards.append(local_card)
            print("temp player cards",temp_player_cards)
        other_players_cards_list.append(temp_player_cards)
    #-----------------------------------------------#
    #COMMUNITY CARDS 
    print('------------------------')
    print('------------------------')
    print('------------------------')
    print('community cards',community_cards)
    community_cards = full_string_to_card_strings(community_cards)
    print('community cards: ',community_cards)
    if len(community_cards) > 5: 
        raise ValueError("community cards number must be up to 5")


    
    #check if total cards are correct for the total players
    #check if there is a duplicate card somewhere . i have duplicate check for a single string but i have to check across the players,community cards etc ! 




    


