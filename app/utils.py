from itertools import product
from app.models import Suit,CardCollection,Card
# TODO : CHANGE THIS MONSTROSITY

def create_full_deck(all_values:list[int],all_suits:list[Suit])->CardCollection:
    all_cards = list(product(all_values,all_suits))
    all_cards = CardCollection(list(map(lambda x:Card(x[0],x[1]),all_cards)))
    return all_cards
