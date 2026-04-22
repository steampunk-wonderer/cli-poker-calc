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
    card_collection_3 = CardCollection([Card(9,Suit.HEARTS),Card(8,Suit.HEARTS),])

    new_card_collection = card_collection + card_collection_2 + card_collection_3
    # print("new_card_collection",new_card_collection)
    sequences = new_card_collection.find_sequences()
    # new_card_collection.find_best_hand()

    clean_straight_flush = CardCollection([
    Card(5,Suit.HEARTS),
    Card(6,Suit.HEARTS),
    Card(7,Suit.HEARTS),
    Card(8,Suit.HEARTS),
    Card(9,Suit.HEARTS),
])
    extra_irrelevant_cards = CardCollection([
    Card(5,Suit.HEARTS),
    Card(6,Suit.HEARTS),
    Card(7,Suit.HEARTS),
    Card(8,Suit.HEARTS),
    Card(9,Suit.HEARTS),
    Card(2,Suit.CLUBS),
    Card(14,Suit.SPADES),
    Card(11,Suit.DIAMONDS),
])
    
    larger_flush = CardCollection([
    Card(4,Suit.SPADES),
    Card(5,Suit.SPADES),
    Card(6,Suit.SPADES),
    Card(7,Suit.SPADES),
    Card(8,Suit.SPADES),
    Card(9,Suit.SPADES),
    Card(10,Suit.SPADES),
])
    
    other_suits_too = CardCollection([
    Card(3,Suit.HEARTS),
    Card(4,Suit.HEARTS),
    Card(4,Suit.CLUBS),
    Card(5,Suit.HEARTS),
    Card(6,Suit.HEARTS),
    Card(7,Suit.HEARTS),

    Card(9,Suit.DIAMONDS),
    Card(10,Suit.DIAMONDS),
    Card(11,Suit.DIAMONDS),
    Card(12,Suit.DIAMONDS),
    Card(13,Suit.DIAMONDS),
])
    
    four_of_kind = CardCollection([
                Card(5,Suit.HEARTS),
        Card(5,Suit.DIAMONDS),
        Card(5,Suit.SPADES),
        Card(5,Suit.CLUBS),
        Card(13,Suit.DIAMONDS),
        Card(4,Suit.HEARTS),
        Card(4,Suit.DIAMONDS),
        Card(4,Suit.CLUBS),
        Card(4,Suit.SPADES),
        Card(7,Suit.HEARTS),


    ])

    full_house_1 = CardCollection([
                Card(5,Suit.HEARTS),
        Card(5,Suit.SPADES),
        Card(5,Suit.CLUBS),
        Card(13,Suit.DIAMONDS),
        Card(4,Suit.HEARTS),
        Card(4,Suit.SPADES),
        Card(7,Suit.HEARTS),
    ])
    full_house_2 = CardCollection([
                Card(5,Suit.HEARTS),
        Card(5,Suit.SPADES),
        Card(5,Suit.CLUBS),
        Card(13,Suit.DIAMONDS),
        Card(4,Suit.HEARTS),
        Card(4,Suit.CLUBS),
        Card(4,Suit.SPADES),
        Card(7,Suit.HEARTS),
    ])

    flush = CardCollection([
                Card(8,Suit.CLUBS),
        Card(9,Suit.HEARTS),
        Card(5,Suit.HEARTS),
        Card(11,Suit.DIAMONDS),
        Card(4,Suit.HEARTS),
        Card(3,Suit.HEARTS),
        Card(4,Suit.HEARTS),
        Card(12,Suit.CLUBS),
    ])
    
    straight = CardCollection([
                Card(8,Suit.CLUBS),
        Card(9,Suit.HEARTS),
        Card(10,Suit.HEARTS),
        Card(11,Suit.HEARTS),
        Card(12,Suit.CLUBS),
        Card(13,Suit.CLUBS),
        Card(2,Suit.CLUBS),
    ])
    

    three_of_kind = CardCollection([
                Card(8,Suit.CLUBS),
        Card(9,Suit.HEARTS),
        Card(8,Suit.HEARTS),
        Card(8,Suit.DIAMONDS),
        Card(10,Suit.SPADES),
        Card(7,Suit.SPADES),
        Card(12,Suit.SPADES),
    ])

    two_pairs = CardCollection([
                Card(8,Suit.CLUBS),
        Card(9,Suit.SPADES),
        Card(8,Suit.HEARTS),
        Card(9,Suit.HEARTS),
        Card(10,Suit.HEARTS),
        Card(2,Suit.SPADES),
        Card(10,Suit.SPADES),
    ])

    two_pairs_2 = CardCollection([
                Card(8,Suit.CLUBS),
        Card(2,Suit.SPADES),
        Card(8,Suit.HEARTS),
        Card(9,Suit.HEARTS),
        Card(10,Suit.HEARTS),
        Card(3,Suit.SPADES),
        Card(5,Suit.SPADES),
    ])



    high_card = CardCollection([
                Card(8,Suit.CLUBS),
        Card(9,Suit.SPADES),
        Card(11,Suit.HEARTS),
        Card(3,Suit.HEARTS),
        Card(2,Suit.SPADES),
        Card(4,Suit.SPADES),
    ])



    

    
    high_card.find_best_hand()
    # print(other_suits_too.find_sequences())

    
    #-----------------------------------------------#
    #-----------------------------------------------#

if __name__ == "__main__": 
    main()
