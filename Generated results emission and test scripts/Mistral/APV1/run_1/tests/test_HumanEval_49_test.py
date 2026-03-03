You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_49_code import modp

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret

 Here is a comprehensive unittest test suite for the given Python function `modp`. The test cases cover various edge cases and boundary values to ensure the function works as expected.


import unittest
from HumanEval_49_code import modp

class TestModP(unittest.TestCase):

    def test_modp_with_positive_numbers(self):
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(10, 17), 13)
        self.assertEqual(modp(100, 101), 1)
        self.assertEqual(modp(1000, 10001), 1)

    def test_modp_with_zero(self):
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(0, 10001), 1)

    def test_modp_with_negative_numbers(self):
        self.assertEqual(modp(-1, 5), 4)
        self.assertEqual(modp(-3, 5), 3)
        self.assertEqual(modp(-100, 101), 100)
        self.assertEqual(modp(-1000, 10001), 1000)

    def test_modp_with_large_numbers(self):
        self.assertEqual(modp(1000000, 1000001), 1)
        self.assertEqual(modp(1000000000, 1000000001), 1)

    def test_modp_with_large_exponent(self):
        self.assertEqual(modp(1, 5), 1)
        self.assertEqual(modp(1, 10), 1)
        self.assertEqual(modp(1, 100), 1)
        self.assertEqual(modp(1, 1000), 1)
        self.assertEqual(modp(1, 10000), 1)
        self.assertEqual(modp(1, 100000), 1)
        self.assertEqual(modp(1, 1000000), 1)

    def test_modp_with_large_base(self):
        self.assertEqual(modp(2, 5), 2)
        self.assertEqual(modp(3, 10), 3)
        self.assertEqual(modp(5, 15), 5)
        self.assertEqual(modp(7, 20), 13)
        self.assertEqual(modp(11, 20), 11)
        self.assertEqual(modp(13, 20), 13)
        self.assertEqual(modp(17, 20), 17)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive numbers, zero, negative numbers, large numbers, large exponents, and large bases. It covers a wide range of test cases to ensure the function works correctly.