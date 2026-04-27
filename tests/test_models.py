import unittest
from app.models import CardCollection,Card,Suit,HandRank

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

        expected_1 = [CardCollection([
            Card(5,Suit.HEARTS),
            Card(6,Suit.HEARTS),
            Card(7,Suit.HEARTS),
            Card(8,Suit.CLUBS),
            Card(9,Suit.HEARTS),
        ])]

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

        expected_2 = [CardCollection([
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
        ])]

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

        expected_3 = [CardCollection([
            Card(9,Suit.CLUBS),
            Card(9,Suit.HEARTS),
            Card(10,Suit.HEARTS),
            Card(11,Suit.HEARTS),
            Card(12,Suit.HEARTS),
            Card(13,Suit.HEARTS),
        ])]

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

        expected_5 = [CardCollection([
            Card(6,Suit.CLUBS),
            Card(7,Suit.DIAMONDS),
            Card(8,Suit.HEARTS),
            Card(9,Suit.SPADES),
            Card(10,Suit.HEARTS),
        ])]

        self.assertEqual(result_5, expected_5)

        
        test_6 = CardCollection([
            Card(5,Suit.CLUBS),
            Card(14,Suit.DIAMONDS),
            Card(4,Suit.HEARTS),
            Card(3,Suit.SPADES),
            Card(2,Suit.HEARTS),
        ])

        result_6 = test_6.find_sequences()

        expected_6 = [CardCollection([
            Card(1,Suit.DIAMONDS),
            Card(2,Suit.HEARTS),
            Card(3,Suit.SPADES),
            Card(4,Suit.HEARTS),
            Card(5,Suit.CLUBS),
        ])]

        self.assertEqual(result_6, expected_6)
    
    def test_find_best_hand(self):
        #clean_straight_flush
        #extra_irrelevant_cards straight flush
        #larger flush
        #other_suits_too straight flush
        #four_of_kind
        #full_house_1
        #full_house_2
        #flush
        #straight
        #three of kind
        #two pairs
        #two_pairs_2 
        #high card
        #single pair
        card_cases = [
            CardCollection([
                Card(5,Suit.HEARTS),
                Card(6,Suit.HEARTS),
                Card(7,Suit.HEARTS),
                Card(8,Suit.HEARTS),
                Card(9,Suit.HEARTS),
            ]),
            CardCollection([
                Card(5,Suit.HEARTS),
                Card(6,Suit.HEARTS),
                Card(7,Suit.HEARTS),
                Card(8,Suit.HEARTS),
                Card(9,Suit.HEARTS),
                Card(2,Suit.CLUBS),
                Card(14,Suit.SPADES),
                Card(11,Suit.DIAMONDS),
            ]),
            CardCollection([
                Card(4,Suit.SPADES),
                Card(5,Suit.SPADES),
                Card(6,Suit.SPADES),
                Card(7,Suit.SPADES),
                Card(8,Suit.SPADES),
                Card(9,Suit.SPADES),
                Card(10,Suit.SPADES),
            ]),
            CardCollection([
                Card(3,Suit.HEARTS),
                Card(4,Suit.HEARTS),
                Card(4,Suit.CLUBS),
                Card(5,Suit.HEARTS),
                Card(6,Suit.HEARTS),
                Card(7,Suit.HEARTS),

                Card(9,Suit.DIAMONDS),
                Card(10,Suit.DIAMONDS),
                Card(11,Suit.DIAMONDS),
                Card(12,Suit.DIAMONDS),
                Card(13,Suit.DIAMONDS),
            ]),
            CardCollection([
                Card(5,Suit.HEARTS),
                Card(5,Suit.DIAMONDS),
                Card(5,Suit.SPADES),
                Card(5,Suit.CLUBS),
                Card(13,Suit.DIAMONDS),
                Card(4,Suit.HEARTS),
                Card(4,Suit.DIAMONDS),
                Card(4,Suit.CLUBS),
                Card(4,Suit.SPADES),
                Card(7,Suit.HEARTS),
            ]),
            CardCollection([
                Card(5,Suit.HEARTS),
                Card(5,Suit.SPADES),
                Card(5,Suit.CLUBS),
                Card(13,Suit.DIAMONDS),
                Card(4,Suit.HEARTS),
                Card(4,Suit.SPADES),
                Card(7,Suit.HEARTS),
            ]),
            CardCollection([
                Card(5,Suit.HEARTS),
                Card(5,Suit.SPADES),
                Card(5,Suit.CLUBS),
                Card(13,Suit.DIAMONDS),
                Card(4,Suit.HEARTS),
                Card(4,Suit.CLUBS),
                Card(4,Suit.SPADES),
                Card(7,Suit.HEARTS),
            ]),
            CardCollection([
                Card(8,Suit.CLUBS),
                Card(9,Suit.HEARTS),
                Card(5,Suit.HEARTS),
                Card(11,Suit.DIAMONDS),
                Card(4,Suit.HEARTS),
                Card(3,Suit.HEARTS),
                Card(4,Suit.HEARTS),
                Card(12,Suit.CLUBS),
            ]),
            CardCollection([
                Card(8,Suit.CLUBS),
                Card(9,Suit.HEARTS),
                Card(10,Suit.HEARTS),
                Card(11,Suit.HEARTS),
                Card(12,Suit.CLUBS),
                Card(13,Suit.CLUBS),
                Card(2,Suit.CLUBS),
            ]),
            CardCollection([
                Card(8,Suit.CLUBS),
                Card(9,Suit.HEARTS),
                Card(8,Suit.HEARTS),
                Card(8,Suit.DIAMONDS),
                Card(10,Suit.SPADES),
                Card(7,Suit.SPADES),
                Card(12,Suit.SPADES),
            ]),
            CardCollection([
                Card(8,Suit.CLUBS),
                Card(9,Suit.SPADES),
                Card(8,Suit.HEARTS),
                Card(9,Suit.HEARTS),
                Card(10,Suit.HEARTS),
                Card(2,Suit.SPADES),
                Card(10,Suit.SPADES),
            ]),
            CardCollection([
                Card(8,Suit.CLUBS),
                Card(2,Suit.SPADES),
                Card(8,Suit.HEARTS),
                Card(9,Suit.HEARTS),
                Card(10,Suit.HEARTS),
                Card(3,Suit.SPADES),
                Card(10,Suit.SPADES),
            ]),
            CardCollection([
                Card(8,Suit.CLUBS),
                Card(9,Suit.SPADES),
                Card(11,Suit.HEARTS),
                Card(3,Suit.HEARTS),
                Card(2,Suit.SPADES),
                Card(4,Suit.SPADES),
            ]),
            CardCollection([
                Card(8,Suit.CLUBS),
                Card(9,Suit.SPADES),
                Card(11,Suit.HEARTS),
                Card(3,Suit.HEARTS),
                Card(2,Suit.SPADES),
                Card(11,Suit.SPADES),
            ])
        ]
        correct_results = [
            {
                "rank":HandRank.STRAIGHT_FLUSH,
                "tiebreakers":(9,8,7,6,5)
            },
            {
                "rank":HandRank.STRAIGHT_FLUSH,
                "tiebreakers":(9,8,7,6,5)
            },
            {
                "rank":HandRank.STRAIGHT_FLUSH,
                "tiebreakers":(10,9,8,7,6)
            },
            {
                "rank":HandRank.STRAIGHT_FLUSH,
                "tiebreakers":(13,12,11,10,9)
            },
            {
                "rank":HandRank.FOUR_OF_A_KIND,
                "tiebreakers":(5,13)
            },
            {
                "rank":HandRank.FULL_HOUSE,
                "tiebreakers":(5,4)
            },
            {
                "rank":HandRank.FULL_HOUSE,
                "tiebreakers":(5,4)
            },
            {
                "rank":HandRank.FLUSH,
                "tiebreakers":(9,5,4,4,3)
            },
            {
                "rank":HandRank.STRAIGHT,
                "tiebreakers":(13,12,11,10,9)
            },
            {
                "rank":HandRank.THREE_OF_A_KIND,
                "tiebreakers":(8,12,10)
            },
            {
                "rank":HandRank.TWO_PAIR,
                "tiebreakers":(10,9,8)
            },
            {
                "rank":HandRank.TWO_PAIR,
                "tiebreakers": (10,8,9)
            },
            {
                "rank":HandRank.HIGH_CARD,
                "tiebreakers":(11,9,8,4,3)
            },
            {
                "rank":HandRank.PAIR,
                "tiebreakers":(11,9,8,3)
            }
        ]
        #----------------------------------------#
        for i,card_case in enumerate(card_cases): 
            result = card_case.find_best_hand()
            self.assertEqual(result.rank,correct_results[i]["rank"])
            self.assertEqual(result.tiebreakers,correct_results[i]["tiebreakers"])
        #----------------------------------------#

        
        