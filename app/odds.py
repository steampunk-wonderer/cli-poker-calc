
from app.models import CardCollection,Suit,Card,EvaluatedHand
from app.parser import values_dict
from app.utils import create_full_deck
from app.consts import ALL_SUITS, ALL_VALUES
from itertools import combinations

# TODO : CREATE FULL DECK ETC SHOULD TAKE FROM A CONSTS FILE    

def community_combinations(community_cards:CardCollection,excluded_cards:CardCollection)->list[CardCollection]:
    if len(community_cards) > 5:
        raise ValueError("community_cards cannot have more than 5 cards")

    all_cards = create_full_deck(ALL_VALUES,ALL_SUITS)
    available_cards = list(filter(lambda card:card not in excluded_cards,all_cards))
    available_community_slots = 5 - len(community_cards)
    community_rest_combinations = list(CardCollection(list(c)) for c in combinations(available_cards,available_community_slots))
    community_combinations = [c+community_cards for c in community_rest_combinations]

    return community_combinations

def find_winner(evaluated_hands:dict[str, EvaluatedHand]):
    # print('-------------------------------')
    # print("evaluated hands",evaluated_hands)
    best_hand = max(evaluated_hands.values())
    # print("best_hand",best_hand)
    return {
        player_name : hand 
        for player_name,hand in evaluated_hands.items()
        if hand == best_hand
    }

def odds(parsed):
    print("odds function running \n")
    player_cards = parsed["player_cards"]
    print("palyer cards:",player_cards,'\n')
    other_players_cards = parsed["other_players_cards"]
    print("other players cards",other_players_cards,'\n')
    community_cards = parsed["community_cards"]
    print("comunity_cards",community_cards,'\n')

    player_cards_lst = [player_cards]
    player_points = {
        "player-0":0
    }
    for j,t in enumerate(other_players_cards):
        player_cards_lst.append(t)
        player_points[f"player-{j+1}"] = 0

    
    print('plaer cards list :',player_cards_lst)

    # TODO : maybe change that thing below now that i have player_cards_lst
    all_used_cards = player_cards + CardCollection([card for collection in other_players_cards for card in collection]) + community_cards
    print("all player cards",all_used_cards,'\n\n')
    all_community_combinations = community_combinations(community_cards,all_used_cards)

    total_cases = len(all_community_combinations)
    print("total_cases",total_cases)

    for community_cards_combination in all_community_combinations:
        evaluated_hands = {}
        for i,c in enumerate(player_cards_lst):
            print(f"player-{i}")
            print("player cards:",player_cards)
            gatherd_cards = community_cards_combination + c
            result = gatherd_cards.find_best_hand()
            print("gathered cards",gatherd_cards)
            print("result:",result)
            evaluated_hands[f"player-{i}"] = result
        winners = find_winner(evaluated_hands)
        for key in winners:
            player_points[key] += 1 
        # print('\n')
    print("player_points:",player_points)

    odds = { 
        player_name:points/total_cases
        for player_name,points in player_points.items()
    }
    print("odds:",odds)




