import sys 
sys.path.append('..')

from betting import Betting
import unittest

class TestBetting(unittest.TestCase):

    def test_kelly_postive(self):
        self.assertEqual(Betting.kelly(0.5, 3.0, 100), 25)

    def test_kelly_zero(self):
        self.assertEqual(Betting.kelly(0.5, 2.0, 100), 0)

    def test_kelly_negative(self):
        self.assertEqual(Betting.kelly(0.5, 1.5, 100), 0)        
        
if __name__ == '__main__':
    unittest.main()