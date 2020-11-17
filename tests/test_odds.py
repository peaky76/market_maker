import sys 
sys.path.append('..')

from odds import Odds
import unittest

class TestOdds(unittest.TestCase):

    def test_from_decimal(self):
        self.assertEqual(Odds(3).decimal, 3.0)

    def test_from_fractional(self):
        self.assertEqual(Odds.from_fractional(5, 2).decimal, 3.5)        
        
if __name__ == '__main__':
    unittest.main()