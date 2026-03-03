You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
Here is a unittest script for the given function:


import unittest
from HumanEval_25_code import factorize

class TestFactorize(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(factorize(8), [2, 2, 2])
        self.assertEqual(factorize(25), [5, 5])
        self.assertEqual(factorize(70), [2, 5, 7])

    def test_negative(self):
        self.assertEqual(factorize(-8), "Input should be a positive integer")

    def test_zero(self):
        self.assertEqual(factorize(0), "Input should be a positive integer")

    def test_one(self):
        self.assertEqual(factorize(1), [])

    def test_prime(self):
        self.assertEqual(factorize(2), [2])
        self.assertEqual(factorize(3), [3])
        self.assertEqual(factorize(5), [5])
        self.assertEqual(factorize(7), [7])

    def test_large(self):
        self.assertEqual(factorize(1000), [2, 2, 2, 5, 5, 5])

if __name__ == '__main__':
    unittest.main()


This script includes tests for positive numbers, negative numbers, zero, one, prime numbers, and large numbers. It checks if the function returns the correct factors and in the correct order.

Please note that the function `factorize` should be defined in a file named `HumanEval_25_code.py` in the same directory as the test script.

Also, the function should be modified to return an error message when the input is not a positive integer. Here is the modified function:


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
    if n <= 0:
        return "Input should be a positive integer"

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


This version of the function will return an error message if the input is not a positive integer.