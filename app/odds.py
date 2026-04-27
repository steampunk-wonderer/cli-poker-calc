
from app.models import CardCollection,Suit,Card,EvaluatedHand
from app.parser import values_dict
from app.utils import create_full_deck
from app.consts import ALL_SUITS, ALL_VALUES
from itertools import combinations
import random




# TODO : CREATE FULL DECK ETC SHOULD TAKE FROM A CONSTS FILE    

def community_combinations(community_cards:CardCollection,excluded_cards:CardCollection,mode:str,simulations:int|None=None)->list[CardCollection]:
    if len(community_cards) > 5:
        raise ValueError("community_cards cannot have more than 5 cards")

    all_cards = create_full_deck(ALL_VALUES,ALL_SUITS)
    available_cards = list(filter(lambda card:card not in excluded_cards,all_cards))

    available_community_slots = 5 - len(community_cards)

    community_rest_combinations = [] 

    if mode == 'exact':
        community_rest_combinations = [
            CardCollection(list(c))
            for c in combinations(available_cards, available_community_slots)
        ]

    elif mode == 'monte-carlo':
        if simulations is None:
            simulations = 10_000

        for _ in range(simulations):
            sample = random.sample(available_cards, available_community_slots)
            community_rest_combinations.append(CardCollection(sample))

    elif mode == 'auto':
        if available_community_slots >= 3:
            if simulations is None:
                simulations = 10_000

            for _ in range(simulations):
                sample = random.sample(available_cards, available_community_slots)
                community_rest_combinations.append(CardCollection(sample))
        else:
            community_rest_combinations = [
                CardCollection(list(c))
                for c in combinations(available_cards, available_community_slots)
            ]

    else:
        raise ValueError(f"Invalid mode: {mode}")

    community_combinations = [
        c + community_cards
        for c in community_rest_combinations
    ]

    return community_combinations

def find_winner(evaluated_hands:dict[str, EvaluatedHand]):
    best_hand = max(evaluated_hands.values())
    return {
        player_name : hand 
        for player_name,hand in evaluated_hands.items()
        if hand == best_hand
    }

def odds(parsed,mode,simulations=None):
    player_cards = parsed["player_cards"]
    other_players_cards = parsed["other_players_cards"]
    community_cards = parsed["community_cards"]

    player_cards_lst = [player_cards]
    player_points = {
        "player-0":0
    }
    for j,t in enumerate(other_players_cards):
        player_cards_lst.append(t)
        player_points[f"player-{j+1}"] = 0

    

    # TODO : maybe change that thing below now that i have player_cards_lst
    all_used_cards = player_cards + CardCollection([card for collection in other_players_cards for card in collection]) + community_cards






    all_community_combinations = community_combinations(community_cards,all_used_cards,mode,simulations)








    total_cases = len(all_community_combinations)

    for community_cards_combination in all_community_combinations:
        evaluated_hands = {}
        for i,c in enumerate(player_cards_lst):
            gatherd_cards = community_cards_combination + c
            result = gatherd_cards.find_best_hand()
            evaluated_hands[f"player-{i}"] = result
        winners = find_winner(evaluated_hands)
        for key in winners:
            player_points[key] += 1/len(winners) 

    odds = { 
        player_name:points/total_cases
        for player_name,points in player_points.items()
    }
    print("player-points:",player_points)
    return odds




