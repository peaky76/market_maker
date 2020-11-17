import sys 
sys.path.append('..')

from bet import Bet
import unittest

class TestBet(unittest.TestCase):

    def test_kelly_positive(self):
        self.assertEqual(Bet.kelly(0.5, 3.0, 100), 25)

    def test_kelly_zero(self):
        self.assertEqual(Bet.kelly(0.5, 2.0, 100), 0)

    def test_kelly_negative(self):
        self.assertEqual(Bet.kelly(0.5, 1.5, 100), 0)        
        
if __name__ == '__main__':
    unittest.main()