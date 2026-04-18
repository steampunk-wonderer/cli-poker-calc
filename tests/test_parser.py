import unittest
from app.parser import full_string_to_card_strings

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

        

