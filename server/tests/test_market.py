import pytest
import sys 
sys.path.append('..')

from market import Market
from odds import Odds
from runner import Runner

@pytest.fixture
def example_market():
    runner1 = Runner("Argy Bargy", Odds(2))
    runner2 = Runner("Boogie Woogie", Odds(4))
    runner3 = Runner("Chicken Licken", Odds(4))
    runner4 = Runner("Doobie Doo", Odds(10))
    market = Market()
    for runner in [runner1, runner2, runner3, runner4]:
        market.add_runner(runner)    
    return market

def test_favourite(example_market):
    assert example_market.favourite.name == "Argy Bargy"
    
def test_overround(example_market):
    assert example_market.overround == 110.00