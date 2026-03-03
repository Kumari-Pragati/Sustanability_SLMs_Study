You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_25_code import factorize

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    import math
    fact = []
    i = 2
    while i <= int(math.sqrt(n) + 1):
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1

    if n > 1:
        fact.append(n)
    return fact

 Here is a comprehensive unittest test suite for the `factorize` function:


import unittest
from HumanEval_25_code import factorize

class TestFactorize(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(factorize(1), [])
        self.assertEqual(factorize(2), [2])
        self.assertEqual(factorize(3), [3])
        self.assertEqual(factorize(4), [2, 2])
        self.assertEqual(factorize(5), [5])
        self.assertEqual(factorize(6), [2, 3])
        self.assertEqual(factorize(7), [7])
        self.assertEqual(factorize(8), [2, 2, 2])
        self.assertEqual(factorize(9), [3, 3])
        self.assertEqual(factorize(10), [2, 5])
        self.assertEqual(factorize(15), [3, 5])
        self.assertEqual(factorize(16), [2, 2, 2, 2])
        self.assertEqual(factorize(25), [5, 5])
        self.assertEqual(factorize(70), [2, 5, 7])
        self.assertEqual(factorize(81), [3, 3, 3])
        self.assertEqual(factorize(120), [2, 2, 2, 3, 5])

    def test_large_numbers(self):
        self.assertEqual(factorize(1000), [2, 2, 2, 2, 2, 5, 5, 5, 7, 7, 11, 13])
        self.assertEqual(factorize(600851475143), [67, 739, 4679, 6731, 33799])

    def test_prime_numbers(self):
        self.assertEqual(factorize(2), [2])
        self.assertEqual(factorize(3), [3])
        self.assertEqual(factorize(5), [5])
        self.assertEqual(factorize(7), [7])
        self.assertEqual(factorize(11), [11])
        self.assertEqual(factorize(13), [13])
        self.assertEqual(factorize(17), [17])
        self.assertEqual(factorize(19), [19])
        self.assertEqual(factorize(23), [23])
        self.assertEqual(factorize(29), [29])
        self.assertEqual(factorize(31), [31])
        self.assertEqual(factorize(37), [37])
        self.assertEqual(factorize(41), [41])
        self.assertEqual(factorize(43), [43])
        self.assertEqual(factorize(47), [47])
        self.assertEqual(factorize(53), [53])
        self.assertEqual(factorize(59), [59])
        self.assertEqual(factorize(61), [61])
        self.assertEqual(factorize(67), [67])
        self.assertEqual(factorize(71), [71])
        self.assertEqual(factorize(73), [73])
        self.assertEqual(factorize(79), [79])
        self.assertEqual(factorize(83), [83])
        self.assertEqual(factorize(89), [89])
        self.assertEqual(factorize(97), [97])
        self.assertEqual(factorize(101), [101])
        self.assertEqual(factorize(103), [103])
        self.assertEqual(factorize(107), [107])
        self.assertEqual(factorize(109), [109])
        self.assertEqual(factorize(113), [113])
        self.assertEqual(factorize(127), [127])
        self.assertEqual(factorize(131), [131])
        self.assertEqual(factorize(137), [137])
        self.assertEqual(factorize(139),