system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_139_code import special_factorial
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! *... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    fact_i = 1
    special_fact = 1
    for i in range(1, n + 1):
        fact_i *= i
        special_fact *= fact_i
    return special_factassistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_139_code import special_factorial

class TestSpecialFactorial(unittest.TestCase):

    def test_special_factorial_positive_integer(self):
        self.assertEqual(special_factorial(4), 288)
        self.assertEqual(special_factorial(5), 3452)
        self.assertEqual(special_factorial(6), 40320)
        self.assertEqual(special_factorial(7), 362880)

    def test_special_factorial_zero(self):
        with self.assertRaises(ValueError):
            special_factorial(0)

    def test_special_factorial_negative_integer(self):
        with self.assertRaises(ValueError):
            special_factorial(-1)
        with self.assertRaises(ValueError):
            special_factorial(-2)

    def test_special_factorial_non_integer(self):
        with self.assertRaises(TypeError):
            special_factorial(3.5)

if __name__ == '__main__':
    unittest.main()