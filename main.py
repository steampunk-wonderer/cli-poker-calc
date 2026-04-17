from app.models import Suit,Card
import sys
import argparse
from app.parser import parse_game_input,full_string_to_card_strings

def main(): 
    #-----------------------------------------------#
    #-----------------------------------------------#
    #PARSING
    parser = argparse.ArgumentParser() #create parser
    parser.add_argument("--players", type=int,default=1)
    parser.add_argument("--player_cards",default=None)
    parser.add_argument("--other_players_cards",nargs="*",default=None)
    parser.add_argument("--community_cards",default=None)
    args = parser.parse_args() #parse

    parse_game_input(args)

    test_str = "Ac"
    full_string_to_card_strings("10s7cQh2cAhKh")
    #-----------------------------------------------#
    #-----------------------------------------------#)

if __name__ == "__main__": 
    main()
