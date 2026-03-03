system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return factassistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_25_code import factorize

class TestFactorize(unittest.TestCase):

    def test_factorize_8(self):
        self.assertEqual(factorize(8), [2, 2, 2])

    def test_factorize_25(self):
        self.assertEqual(factorize(25), [5, 5])

    def test_factorize_70(self):
        self.assertEqual(factorize(70), [2, 5, 7])

    def test_factorize_1(self):
        self.assertEqual(factorize(1), [])

    def test_factorize_prime(self):
        self.assertEqual(factorize(23), [23])

    def test_factorize_composite(self):
        self.assertEqual(factorize(36), [2, 2, 3, 3])

    def test_factorize_large(self):
        self.assertEqual(factorize(1001), [7, 11, 13])

    def test_factorize_edge(self):
        self.assertEqual(factorize(2), [2])

    def test_factorize_edge2(self):
        self.assertEqual(factorize(3), [3])

    def test_factorize_edge3(self):
        self.assertEqual(factorize(4), [2, 2])

if __name__ == '__main__':
    unittest.main()