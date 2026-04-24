from app.models import Suit,Card,CardCollection,Groups
import sys
import argparse
from app.odds import odds
from app.parser import parse_game_input,full_string_to_card_strings,card_string_to_single_Card

def main(): 
    #-----------------------------------------------#
    #-----------------------------------------------#
    #PARSING
    parser = argparse.ArgumentParser() #create parser
    parser.add_argument("--players", type=int,default=2)
    parser.add_argument("--player_cards",type=str,default=None)
    parser.add_argument("--other_players_cards",type=str,nargs="*",default=None)
    parser.add_argument("--community_cards",type=str,default=None)
    args = parser.parse_args() #parse

    parsed = parse_game_input(args)
    # print("parsed: ",parsed)
    print("-----------------------")
    odds(parsed)
    
    #-----------------------------------------------#
    #-----------------------------------------------#

if __name__ == "__main__": 
    main()
