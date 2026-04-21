import unittest
from app.models import CardCollection,Card,Suit

class TestModels(unittest.TestCase):
    def test_find_sequences(self):

        # ✅ basic straight (unordered input)
        test_1 = CardCollection([
            Card(5,Suit.HEARTS),
            Card(6,Suit.HEARTS),
            Card(8,Suit.CLUBS),
            Card(9,Suit.HEARTS),
            Card(7,Suit.HEARTS),
        ])

        result_1 = test_1.find_sequences()

        expected_1 = [[
            Card(5,Suit.HEARTS),
            Card(6,Suit.HEARTS),
            Card(7,Suit.HEARTS),
            Card(8,Suit.CLUBS),
            Card(9,Suit.HEARTS),
        ]]

        self.assertEqual(result_1, expected_1)


        # ✅ duplicates inside sequence (should still detect straight)
        test_2 = CardCollection([
            Card(2,Suit.HEARTS),
            Card(4,Suit.HEARTS),
            Card(3,Suit.CLUBS),
            Card(5,Suit.HEARTS),
            Card(6,Suit.HEARTS),

            Card(11,Suit.SPADES),
            Card(8,Suit.HEARTS),
            Card(9,Suit.HEARTS),
            Card(10,Suit.CLUBS),

            Card(9,Suit.HEARTS),   # duplicate
            Card(7,Suit.HEARTS),
            Card(7,Suit.SPADES),   # duplicate
        ])

        result_2 = test_2.find_sequences()

        expected_2 = [[
            Card(2,Suit.HEARTS),
            Card(3,Suit.CLUBS),
            Card(4,Suit.HEARTS),
            Card(5,Suit.HEARTS),
            Card(6,Suit.HEARTS),
            Card(7,Suit.HEARTS),
            Card(7,Suit.SPADES),
            Card(8,Suit.HEARTS),
            Card(9,Suit.HEARTS),
            Card(9,Suit.HEARTS),
            Card(10,Suit.CLUBS),
            Card(11,Suit.SPADES),
        ]]

        self.assertEqual(result_2, expected_2)


        # ✅ sequence with gaps (should still find valid 5+ run)
        test_3 = CardCollection([
            Card(10,Suit.HEARTS),
            Card(12,Suit.HEARTS),
            Card(13,Suit.HEARTS),
            Card(11,Suit.HEARTS),
            Card(9,Suit.CLUBS),

            Card(9,Suit.HEARTS),
            Card(7,Suit.HEARTS),
            Card(7,Suit.SPADES),
        ])

        result_3 = test_3.find_sequences()

        expected_3 = [[
            Card(9,Suit.CLUBS),
            Card(9,Suit.HEARTS),
            Card(10,Suit.HEARTS),
            Card(11,Suit.HEARTS),
            Card(12,Suit.HEARTS),
            Card(13,Suit.HEARTS),
        ]]

        self.assertEqual(result_3, expected_3)


        # ❌ no sequence (less than 5)
        test_4 = CardCollection([
            Card(2,Suit.HEARTS),
            Card(3,Suit.HEARTS),
            Card(5,Suit.HEARTS),
            Card(8,Suit.HEARTS),
        ])

        result_4 = test_4.find_sequences()

        self.assertEqual(result_4, [])


        # ✅ edge: exactly 5 cards
        test_5 = CardCollection([
            Card(6,Suit.CLUBS),
            Card(7,Suit.DIAMONDS),
            Card(8,Suit.HEARTS),
            Card(9,Suit.SPADES),
            Card(10,Suit.HEARTS),
        ])

        result_5 = test_5.find_sequences()

        expected_5 = [[
            Card(6,Suit.CLUBS),
            Card(7,Suit.DIAMONDS),
            Card(8,Suit.HEARTS),
            Card(9,Suit.SPADES),
            Card(10,Suit.HEARTS),
        ]]

        self.assertEqual(result_5, expected_5)
        