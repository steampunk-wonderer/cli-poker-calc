import unittest
import argparse
from app.parser import full_string_to_card_strings,card_string_to_single_Card,parse_game_input
from app.models import Suit,Card

class TestParser(unittest.TestCase): 
    def test_full_string_to_card_strings(self):
        test_str = "10s7cQh2cAh "
        result = full_string_to_card_strings(test_str)
        self.assertListEqual(["10s","7c","Qh","2c","Ah"],result)

        test_str = "s107c"
        with self.assertRaises(ValueError):
            full_string_to_card_strings(test_str)
        
        test_str = "10s7cQh2cAh10s"
        with self.assertRaises(ValueError):
            full_string_to_card_strings(test_str)
        
        test_str = "Ah  K   c"
        self.assertListEqual(["Ah","Kc"],full_string_to_card_strings(test_str))

        test_str = "5c 4h Ah Kd"
        self.assertListEqual(["5c","4h","Ah","Kd"],full_string_to_card_strings(test_str))

        test_str = "5k6h"
        with self.assertRaises(ValueError):
            full_string_to_card_strings(test_str)
        
        test_str = "5s5dKh5s"
        with self.assertRaises(ValueError):
            full_string_to_card_strings(test_str)

    def test_card_string_to_single_Card(self):
        correct_strs = [
            "Kh",
            "Ac",
            "3 d",
            "4 c",
            "8s"
        ]
        correct_results = [
            Card(13,Suit.HEARTS),
            Card(14,Suit.CLUBS),
            Card(3,Suit.DIAMONDS),
            Card(4,Suit.CLUBS),
            Card(8,Suit.SPADES)
        ]
        for i,my_str in enumerate(correct_strs): 
            self.assertEqual(correct_results[i],card_string_to_single_Card(my_str))



        type_error_strs = [
            2,
            3.4
        ]
        for my_str in type_error_strs:
            with self.assertRaises(TypeError):
                card_string_to_single_Card(my_str)

        value_error_strs = [
            "hK",
            "16c",
            "",
            " ",
            "8",
            "KhA",
            "10s3"
        ]
        for my_str in value_error_strs:
            with self.assertRaises(ValueError):
                card_string_to_single_Card(my_str)

    def test_parse_game_input_player_cards_errors(self):
        player_cards_value_error = [ 
            argparse.Namespace(
                players=2,
                player_cards="Ah5d 7s",
                other_players_cards=["QsJs"],
                community_cards="8h7s"
            ),
            argparse.Namespace(
                players=2,
                player_cards="hA5d",
                other_players_cards=["QsJs"],
                community_cards="8h7s"
            ),
            argparse.Namespace(
                players=2,
                player_cards="",
                other_players_cards=["QsJs"],
                community_cards="8h7s"
            ),
            argparse.Namespace(
                players=2,
                player_cards="8s1d",
                other_players_cards=["QsJs"],
                community_cards="8h7s"
            ),
            argparse.Namespace(
                players=2,
                player_cards="17sKh",
                other_players_cards=["QsJs"],
                community_cards="8h7s"
            ),
            argparse.Namespace(
                players=2,
                player_cards="7s7s",
                other_players_cards=["QsJs"],
                community_cards="8h7s"
            )
        ]

        for i in player_cards_value_error:
            with self.assertRaises(ValueError):
                parse_game_input(i)
    
    def test_parse_game_input_other_players_cards_errors(self):
        value_errors = [
            argparse.Namespace(
                players=2,
                player_cards="Ah 7s",
                other_players_cards=["QsJs","4s6h8"],
                community_cards="8h7s"
            ),
            argparse.Namespace(
                players=2,
                player_cards="Ah 7s",
                other_players_cards=["QsJs","4sJs"],
                community_cards="8h7s"
            ),
            argparse.Namespace(
                players=2,
                player_cards="Ah 7s",
                other_players_cards=["Ah3o"],
                community_cards="8h7s"
            ),
        ]
        for i in value_errors: 
            with self.assertRaises(ValueError):
                parse_game_input(i)



        

