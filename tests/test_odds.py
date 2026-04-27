import unittest
import argparse
from app.parser import parse_game_input
from app.odds import odds

class TestFinalOdds(unittest.TestCase):
    def test_final_odds(self):
        args = [
            argparse.Namespace(
                players=3,
                player_cards="3c4d",
                other_players_cards=["10s7c", "3h2d"],
                community_cards="Qh2cAh"
            ),
            argparse.Namespace(
                players=3,
                player_cards="3cKd",
                other_players_cards=["10s7c", "3h2d"],
                community_cards=""
            ),
            ]
        
        equal = [
            [0.26085,0.2215,0.51775]
        ]

        for i,a in enumerate(args):
            parsed = parse_game_input(a)
            winning_odds = odds(parsed)
            print("winnig odds",winning_odds)

            self.assertAlmostEqual(winning_odds['player-0'],equal[i][0],delta=1e-4)
            self.assertAlmostEqual(winning_odds['player-1'],equal[i][1],delta=1e-4)
            self.assertAlmostEqual(winning_odds['player-2'],equal[i][2],delta=1e-4)
            
