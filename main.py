from app.models import Suit,Card,CardCollection
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
    print("parsed: ",parsed)
    print("-----------------------")
    card_collection = CardCollection([Card(10,Suit.HEARTS),Card(12,Suit.CLUBS)])

    card_collection_values = card_collection.to_values()
    print('card collection values:',card_collection_values)
    # for card in card_collection:
    #     print('card: ',card)

    # if Card(10,Suit.HEARTS) in card_collection:
        # print("YES !! ")

    # print('card_collection[1]',card_collection[1])
    print('len(card_collection)',len(card_collection))

    #-----------------------------------------------#
    #-----------------------------------------------#

if __name__ == "__main__": 
    main()
