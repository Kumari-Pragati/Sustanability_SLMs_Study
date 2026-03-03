You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_25_code import factorize

class TestFactorize(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(factorize(8), [2, 2, 2])
        self.assertEqual(factorize(25), [5, 5])
        self.assertEqual(factorize(70), [2, 5, 7])

    def test_prime_numbers(self):
        self.assertEqual(factorize(2), [2])
        self.assertEqual(factorize(3), [3])
        self.assertEqual(factorize(5), [5])
        self.assertEqual(factorize(7), [7])

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            factorize(-8)

    def test_zero_and_one(self):
        with self.assertRaises(ValueError):
            factorize(0)
        with self.assertRaises(ValueError):
            factorize(1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            factorize(8.5)
        with self.assertRaises(TypeError):
            factorize('8')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive numbers, prime numbers, negative numbers, zero, one, and non-integer inputs. It uses the `unittest` framework's `unittest.TestCase` class to create test cases and the `assertEqual` method to check if the output of the `factorize` function matches the expected output. The `assertRaises` method is used to check if the function raises a `ValueError` when given 0 or 1, and a `TypeError` when given a non-integer input.