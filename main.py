from app.models import Suit,Card,CardCollection,Groups
import sys
import argparse
from app.odds import odds
from app.parser import parse_game_input,full_string_to_card_strings,card_string_to_single_Card
import time 
from app.utils import pretty_print

def main(): 
    #-----------------------------------------------#
    #-----------------------------------------------#
    start = time.perf_counter()
    #PARSING
    parser = argparse.ArgumentParser() #create parser
    parser.add_argument("--players", type=int,default=2)
    parser.add_argument("--player_cards",type=str,default=None)
    parser.add_argument("--other_players_cards",type=str,nargs="*",default=None)
    parser.add_argument("--community_cards",type=str,default=None)
    parser.add_argument(
        "--mode",
        choices=["auto","exact","monte-carlo"],
        default="auto"
    )
    parser.add_argument(
        "--simulations",
        type=int,
        default=10_000
    )
    args = parser.parse_args() #parse
    mode = args.mode
    simulations = args.simulations
    parsed = parse_game_input(args)
    #-----------------------------------------------#
    #-----------------------------------------------#
    temp = odds(parsed,mode,simulations)
    winning_odds = temp["odds"]
    method = temp["method"]
    iterations = temp["iterations"]
    player_points = temp["player_points"]
    total_cases = temp["total_cases"]

    end = time.perf_counter()
    pretty_print(args,method,iterations,winning_odds,player_points,total_cases)
    print("""===========================""")
    print("Duration",end-start)

if __name__ == "__main__": 
    main()
