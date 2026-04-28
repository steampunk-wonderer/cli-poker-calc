from itertools import product
from app.models import Suit,CardCollection,Card
from math import sqrt
# TODO : CHANGE THIS MONSTROSITY

def monte_carlo_error(p:float,n:int)->float:
    error = sqrt(p * (1 - p) / n)
    return error 

def monte_carlo_error_95(p: float, n: int) -> float:
    return 2 * sqrt(p * (1 - p) / n)

def create_full_deck(all_values:list[int],all_suits:list[Suit])->CardCollection:
    all_cards = list(product(all_values,all_suits))
    all_cards = CardCollection(list(map(lambda x:Card(x[0],x[1]),all_cards)))
    return all_cards

def pretty_print(args,method,iterations,winning_odds,player_points,total_cases):
    community_cards = args.community_cards
    print("INSIDE!!! ",player_points)
    mode = args.mode
    print("""===========================
      Poker Odds
===========================\n""")
    print("Players:")

    players_cards = [args.player_cards]
    for other in args.other_players_cards:
        players_cards.append(other)    

    for i in range(args.players):
        print(f"   player-{i} | {players_cards[i]}")
    print('')    
    print("Board:")
    print(f"   {args.community_cards}")
    print("")
    print("Method:")
    if method == 'monte-carlo':
        print(f"   Monte Carlo ({iterations} simulations)")
    else:
        print(f"   Exact")
    print("")
    print("""---------------------------
Results:
---------------------------""")
    if method == 'exact':
        for i in range(args.players):
            print(f"   player-{i}: {winning_odds[f"player-{i}"]*100:.2f}% ({player_points[f"player-{i}"]:.0f} / {total_cases})")
    elif method == 'monte-carlo':
        for i in range(args.players):
            print(
                    f"   player-{i}: {winning_odds[f'player-{i}'] * 100:.2f}% "
                    f"(±{monte_carlo_error_95(winning_odds[f'player-{i}'], iterations) * 100:.2f}%)"
                )


"""
===========================
      Poker Odds
===========================

Players:
  player-0  | 3c 4d
  player-1  | Ts 7c
  player-2  | 3h 2d

Board:
  Qh 2c Ah

Method:
  Monte Carlo (10,000 simulations)

---------------------------
Results:
---------------------------
  🥇 player-2  → 51.77%
  🥈 player-0  → 26.08%
  🥉 player-1  → 22.15%
"""

# player-0: 19.02%  (235,123 / 1,370,754)
# player-1: 40.41%  (553,892 / 1,370,754)
# player-2: 40.56%  (556,739 / 1,370,754)