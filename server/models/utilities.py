import math

class Number:

    @classmethod
    def primes(cls, max):
        '''Calculates all prime numbers up to a maximum value using the Sieve of Eratosthenes method'''

        potentials = list(range(2, max+1))

        for i in range(2, int(math.sqrt(max)) + 1):
            for j in range(2, int(max/i) + 1):
                if (i*j) in potentials:
                    potentials.remove(i*j)

        return potentials

    @staticmethod
    def have_common_divisor(num1, num2):
        if num1 == num2:
            return True
        if Number.is_prime(max(num1, num2)):
            return False
        for testnum in Number.primes(min(num1, num2)):
            if num1 % testnum == 0 and num2 % testnum == 0:
                return True
        return False

    @staticmethod
    def is_prime(num):
        for i in range(2, int(math.sqrt(num)+1)):
            if num % i == 0:
                return False
        return True