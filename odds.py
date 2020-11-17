from utilities import Number

class Odds:
    
    '''Internal representation of odds is decimal, but can be input as fractional or probability using class methods
       and output as decimal, fractional or probability'''

    _VALID_FRACTIONS = [
        # Denominator, valid_from_decimal, valid_to_decimal
        (2, 2, 8),
        (3, 3, 3.5),
        (4, 2, 4),
        (5, 1, 2),
        (8, 1.25, 2),
        (10, 1, 1.1)
    ]
    
    _VALID_WHOLES = [n for n in 
                        list(range(1, 13))
                        + list(range(14, 23, 2)) 
                        + [25, 28, 33, 40, 50, 66, 80] 
                        + list(range(100, 151, 25)) 
                        + list(range(200, 1001, 100))
                    ]
        
    def __init__(self, decimal):
        self._decimal = float(decimal)

    @classmethod
    def from_fractional(cls, enum, denom):
        return cls((enum / denom) + 1)
    
    @classmethod
    def from_probability(cls, prob):
        return cls(1 / prob)  
 
    @classmethod
    def list_all_fractionals(cls):
        permitted_fractionals = []
        # Add whole numbers from evens to 1000/1
        for enum in cls._VALID_WHOLES:
            permitted_fractionals.append((enum, 1))
        # Add fractions, i.e /2, /4, /8 etc.
        for denom in cls._VALID_FRACTIONS:
            min = int(denom[0] * denom[1])
            max = int(denom[0] * denom[2])
            for enum in range(min, max + 1):
                if not Number.have_common_divisor(denom[0], enum):
                    permitted_fractionals.append((enum, denom[0]))
        # Add odds-on (removing evens)        
        permitted_fractionals += [(y, x) for (x, y) in permitted_fractionals[1:]]
        # Return list sorted by decimal value
        return sorted(permitted_fractionals, key=lambda x: x[0] / x[1])
    
    def as_decimal(self):
        return self._decimal
        
    def as_fractional(self):
        absolute_difference = lambda x: abs(self._decimal - Odds.from_fractional(x[0], x[1]).as_decimal())
        return min(Odds.list_all_fractionals(), key=absolute_difference)
    
    def as_probability(self):
        return 1 / self._decimal      