from app.models import Suit,Card
import sys
import argparse

def main(): 
    parser = argparse.ArgumentParser() #create parser
    parser.add_argument("--players", type=int,default=1)
    parser.add_argument("--player_cards",default=None)
    parser.add_argument("--other_player_cards",default=None)
    parser.add_argument("--community_cards",default=None)




    args = parser.parse_args() #parse
    print('args: ',args)
    print("type: ",type(args))



    card = Card(Suit.HEARTS,4)
    print(card)
    # print("sys.argv: ",sys.argv)
    

if __name__ == "__main__": 
    main()
