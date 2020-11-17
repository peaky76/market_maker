class Odds:
    
    '''Internal representation of odds is decimal'''
    
    def __init__(self, decimal):
        self.decimal = float(decimal)

    @classmethod
    def from_fractional(cls, enum, denom):
        return cls((enum / denom) + 1)

    # _valid_denoms = [
    #     # Enumerator, valid_from, valid_to
    #     (2, 2, 8),
    #     (4, 2, 4),
    #     (5, 1, 2),
    #     (8, 1.25, 2),
    #     (10, 1, 1.1)
    # ]

    # @classmethod
    # def decimal(cls, value):
    #     return cls(value)

    # @classmethod
    # def fractional(cls, enum, denom):
    #     return cls((enum / denom) + 1)

    # @classmethod
    # def _generate_fractionals(cls):
    #     permitted_fractionals = []
    #     for denom in cls._valid_denoms:
    #         min = int(denom[0] * denom[1])
    #         max = int(denom[0] * denom[2])
    #         for enum in range(min, max + 1):
    #             if not Number.have_common_divisor(denom[0], enum):
    #                 permitted_fractionals.append((enum, denom[0]))
    #     return permitted_fractionals

    # @classmethod
    # def all_fractionals(cls):
    #     return cls._generate_fractionals

    # # @staticmethod
    # # def _convert_to_decimal(denom, enum):
    # #     return (denom / enum) + 1
