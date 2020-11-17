class Bet:

    @staticmethod
    def kelly(probability, market_odds, bank):
        
        """ Calculate the recommended Kelly criterion bet 
        for any given win probability, decimal win odds and size of bank"""

        p = prob  # Win probability
        q = 1 - p  # Loss probability
        odds = market_odds - 1 # Converts 'odds' from decimal into odds to 1
        
        edge = (o * p) - q
        fraction_to_bet = edge / odds # Kelly formula, aka "edge over odds"  
        kelly = bank * fraction_to_bet     

        return kelly if kelly > 0 else 0