from app.models import Suit,Card,CardCollection,Groups
import sys
import argparse
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
    card_collection = CardCollection([Card(10,Suit.HEARTS),Card(12,Suit.CLUBS),Card(2,Suit.SPADES)])
    card_collection_2 = CardCollection([Card(11,Suit.SPADES),Card(5,Suit.HEARTS),Card(12,Suit.HEARTS)])

    new_card_collection = card_collection + card_collection_2
    # print("new_card_collection",new_card_collection)
    result = new_card_collection.find_same_groups(Groups.BY_VALUE)
    print("result",result)



    #-----------------------------------------------#
    #-----------------------------------------------#

if __name__ == "__main__": 
    main()
