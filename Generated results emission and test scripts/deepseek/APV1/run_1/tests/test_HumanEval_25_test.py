You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_25_code import factorize

class TestFactorize(unittest.TestCase):
    def test_simple_numbers(self):
        self.assertEqual(factorize(2), [2])
        self.assertEqual(factorize(3), [3])
        self.assertEqual(factorize(5), [5])
        self.assertEqual(factorize(7), [7])

    def test_composite_numbers(self):
        self.assertEqual(factorize(8), [2, 2, 2])
        self.assertEqual(factorize(25), [5, 5])
        self.assertEqual(factorize(70), [2, 5, 7])

    def test_large_numbers(self):
        self.assertEqual(factorize(100), [2, 2, 5, 5])
        self.assertEqual(factorize(1000), [2, 2, 2, 5, 5, 5])

    def test_edge_cases(self):
        self.assertEqual(factorize(1), [])
        self.assertEqual(factorize(0), [])
        self.assertEqual(factorize(-1), [])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for simple numbers, composite numbers, large numbers, and edge cases (1, 0, and -1). It uses the `assertEqual` method to check if the output of the `factorize` function matches the expected output.