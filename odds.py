from utilities import Number

class Odds:
    
    '''Internal representation of odds is decimal, but can be input as fractional or probability using class methods
       and output as decimal, fractional or probability'''

    _VALID_DENOMS = [
        # Enumerator, valid_from, valid_to
        (2, 2, 8),
        (4, 2, 4),
        (5, 1, 2),
        (8, 1.25, 2),
        (10, 1, 1.1)
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
        for denom in cls._VALID_DENOMS:
            min = int(denom[0] * denom[1])
            max = int(denom[0] * denom[2])
            for enum in range(min, max + 1):
                if not Number.have_common_divisor(denom[0], enum):
                    permitted_fractionals.append((enum, denom[0]))
        return permitted_fractionals
    
    def as_decimal(self):
        return self._decimal
        
    def as_fractional(self):
        pass
    
    def as_probability(self):
        return 1 / self._decimal      