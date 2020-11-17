import sys 
sys.path.append('..')

from odds import Odds

def test_from_decimal():
    assert Odds(3).as_decimal() == 3.0

def test_from_fractional():
    assert Odds.from_fractional(5, 2).as_decimal() == 3.5    
    
def test_from_probability():
    assert Odds.from_probability(0.5).as_decimal() == 2.0    
    
def test_as_fractional_exact_whole():
    assert Odds(3).as_fractional() == (2, 1)
    
def test_as_fractional_exact_fraction():
    assert Odds(3.5).as_fractional() == (5, 2)
    
def test_as_fractional_inexact_whole():
    assert Odds(13.2).as_fractional() == (12, 1)
    
def test_as_fractional_inexact_fraction():
    assert Odds(4.35).as_fractional() == (10, 3)
    
def test_as_fractional_extreme_odds_on():
    assert Odds(1.00000000001).as_fractional() == (1, 1000)
    
def test_as_fractional_extreme_odds_against():
    assert Odds(10000000).as_fractional() == (1000, 1)
        
def test_as_probability():
    assert Odds(4).as_probability() == 0.25

def test_to_fractional_string_evens():
    assert Odds(2).to_fractional_string() == "Evens"
        
def test_to_fractional_string_10_3():
    assert Odds(4.33).to_fractional_string() == "100/30"

def test_to_fractional_string_regular():
    assert Odds(34).to_fractional_string() == "33/1"  