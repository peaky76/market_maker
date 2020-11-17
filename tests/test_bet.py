import sys 
sys.path.append('..')

from bet import Bet

def test_kelly_positive():
    assert Bet.kelly(0.5, 3.0, 100) == 25

def test_kelly_zero():
    assert Bet.kelly(0.5, 2.0, 100) == 0
    
def test_kelly_negative():
    assert Bet.kelly(0.5, 1.5, 100) == 0       
