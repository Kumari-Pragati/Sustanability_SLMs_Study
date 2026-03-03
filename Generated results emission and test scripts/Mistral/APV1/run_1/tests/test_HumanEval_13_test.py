You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_13_code import greatest_common_divisor

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return a

 Here is a comprehensive unittest test suite for the given Python function `greatest_common_divisor`. I've included several test cases to cover various scenarios, including edge cases.


import unittest
from HumanEval_13_code import greatest_common_divisor

class TestGCD(unittest.TestCase):

    def test_gcd_positive_numbers(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)
        self.assertEqual(greatest_common_divisor(48, 18), 6)
        self.assertEqual(greatest_common_divisor(12, 36), 12)

    def test_gcd_zero(self):
        self.assertEqual(greatest_common_divisor(0, 5), 0)
        self.assertEqual(greatest_common_divisor(5, 0), 0)

    def test_gcd_negative_numbers(self):
        self.assertEqual(greatest_common_divisor(-3, -5), 1)
        self.assertEqual(greatest_common_divisor(-25, -15), 5)
        self.assertEqual(greatest_common_divisor(-48, -18), 6)
        self.assertEqual(greatest_common_divisor(-12, -36), 12)

    def test_gcd_large_numbers(self):
        self.assertEqual(greatest_common_divisor(1000000007, 2147483647), 1)
        self.assertEqual(greatest_common_divisor(2147483647, 1000000007), 1)

    def test_gcd_prime_numbers(self):
        self.assertEqual(greatest_common_divisor(7, 11), 1)
        self.assertEqual(greatest_common_divisor(13, 17), 1)
        self.assertEqual(greatest_common_divisor(19, 23), 1)

    def test_gcd_powers_of_two(self):
        self.assertEqual(greatest_common_divisor(2, 4), 2)
        self.assertEqual(greatest_common_divisor(2**10, 2**12), 2**10)
        self.assertEqual(greatest_common_divisor(2**15, 2**17), 2**15)

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios, including positive numbers, zero, negative numbers, large numbers, prime numbers, and powers of two. It should provide a good starting point for testing the `greatest_common_divisor` function.