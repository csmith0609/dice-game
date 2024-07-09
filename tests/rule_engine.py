import unittest
from unittest.mock import patch
from rule_engine import calculate_score

class TestCalculateScore(unittest.TestCase):
    @patch('rule_engine.generate_dice_roll', return_value=4)
    def test_even_total_score(self, mock_generate_dice_roll):
        self.assertEqual(calculate_score(2, 2), 18)  # 2+2=4, 4+10=14, 14+4=18 (doubles)
        self.assertEqual(calculate_score(1, 3), 14)  # 1+3=4, 4+10=14
        self.assertEqual(calculate_score(4, 6), 20)  # 4+6=10, 10+10=20

    @patch('rule_engine.generate_dice_roll', return_value=4)
    def test_odd_total_score(self, mock_generate_dice_roll):
        self.assertEqual(calculate_score(1, 2), 0)   # 1+2=3, 3-5=-2, min score is 0
        self.assertEqual(calculate_score(1, 5), 16)  # 1+5=6, 6+10=16 (even sum)

    @patch('rule_engine.generate_dice_roll', return_value=4)
    def test_doubles(self, mock_generate_dice_roll):
        self.assertEqual(calculate_score(3, 3), 20)  # 3+3=6, 6+10=16, 16+4=20
        self.assertEqual(calculate_score(2, 2), 18)  # 2+2=4, 4+10=14, 14+4=18

    @patch('rule_engine.generate_dice_roll', return_value=4)
    def test_negative_total_score(self, mock_generate_dice_roll):
        self.assertEqual(calculate_score(1, 1), 16)  # 1+1=2, 2+10=12, 12+4=16 (doubles)

    @patch('rule_engine.generate_dice_roll', return_value=4)
    def test_dice1_dice2_different(self, mock_generate_dice_roll):
        self.assertEqual(calculate_score(1, 3), 14)  # 1+3=4, 4+10=14
        self.assertEqual(calculate_score(4, 5), 4)   # 4+5=9, 9-5=4

    @patch('rule_engine.generate_dice_roll', return_value=4)
    def test_very_high_scores(self, mock_generate_dice_roll):
        self.assertEqual(calculate_score(20, 20), 54)  # 20+20=40, 40+10=50, 50+4=54 (doubles)

if __name__ == '__main__':
    unittest.main()