
from app.models import CardCollection,Suit,Card
from app.parser import values_dict
from app.utils import create_full_deck
from app.consts import ALL_SUITS, ALL_VALUES
from itertools import combinations

# TODO : CREATE FULL DECK ETC SHOULD TAKE FROM A CONSTS FILE    

def community_combinations(community_cards:CardCollection,excluded_cards:CardCollection)->list[CardCollection]:
    all_cards = create_full_deck(ALL_VALUES,ALL_SUITS)
    available_cards = list(filter(lambda card:card not in excluded_cards,all_cards))
    available_community_slots = 5 - len(community_cards)
    community_rest_combinations = list(CardCollection(list(c)) for c in combinations(available_cards,available_community_slots))
    community_combinations = [c+community_cards for c in community_rest_combinations]

    return community_combinations



def odds(parsed):
    print("odds function running")
    player_cards = parsed["player_cards"]
    print("palyer cards:",player_cards,'\n')
    other_players_cards = parsed["other_players_cards"]
    print("other players cards",other_players_cards,'\n')
    community_cards = parsed["community_cards"]
    print("comunity_cards",community_cards,'\n')

    all_used_cards = player_cards + CardCollection([card for collection in other_players_cards for card in collection]) + community_cards
    print("all player cards",all_used_cards)
    all_community_combinations = community_combinations(community_cards,all_used_cards)
    print("all_community_combinations",all_community_combinations)
