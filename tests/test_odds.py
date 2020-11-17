import sys 
sys.path.append('..')

from odds import Odds

def test_from_decimal():
    assert Odds(3).decimal == 3.0

def test_from_fractional():
    assert Odds.from_fractional(5, 2).decimal == 3.5        