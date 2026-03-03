You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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
    return fact

 Here is the complete unittest test suite for the `factorize` function:


import unittest
from HumanEval_25_code import factorize

class TestFactorize(unittest.TestCase):

    def test_factorize_simple_cases(self):
        self.assertEqual(factorize(8), [2, 2, 2])
        self.assertEqual(factorize(25), [5, 5])
        self.assertEqual(factorize(70), [2, 5, 7])
        self.assertEqual(factorize(1), [1])
        self.assertEqual(factorize(4), [2, 2])
        self.assertEqual(factorize(9), [3, 3])
        self.assertEqual(factorize(16), [2, 2, 2, 2])
        self.assertEqual(factorize(24), [2, 2, 2, 3, 3])

    def test_factorize_prime_numbers(self):
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

    def test_factorize_large_numbers(self):
        self.assertEqual(factorize(120), [2, 2, 2, 3, 5])
        self.assertEqual(factorize(168), [2, 2, 2, 3, 3, 7])
        self.assertEqual(factorize(200), [2, 2, 2, 2, 5, 5])
        self.assertEqual(factorize(252), [2, 2, 3, 3, 7])
        self.assertEqual(factorize(300), [2, 3, 5, 5, 7])
        self.assertEqual(factorize(360), [2, 2, 2, 3, 3, 5])
        self.assertEqual(factorize(448), [2, 2, 2, 2, 2, 7])
        self.assertEqual(factorize(576), [2, 2, 2, 2, 3, 3, 3])
        self.assertEqual(factorize(720), [2, 2, 2, 3, 3, 5])
        self.assertEqual(factorize(960), [2, 2, 2, 2, 2, 2, 3, 5])
        self.assertEqual(factorize(1200), [2, 2, 2, 2, 3, 3, 5])
        self.assertEqual(factorize(1440), [2, 2, 2, 3, 3, 3,