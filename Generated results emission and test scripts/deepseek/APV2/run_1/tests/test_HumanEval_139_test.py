You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
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
    return special_fact


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_139_code import special_factorial

class TestSpecialFactorial(unittest.TestCase):
    def test_special_factorial(self):
        self.assertEqual(special_factorial(0), 1)
        self.assertEqual(special_factorial(1), 1)
        self.assertEqual(special_factorial(2), 2)
        self.assertEqual(special_factorial(3), 12)
        self.assertEqual(special_factorial(4), 288)
        self.assertEqual(special_factorial(5), 3628800)
        self.assertEqual(special_factorial(6), 479001600)
        self.assertEqual(special_factorial(7), 1307674368000)
        self.assertEqual(special_factorial(8), 1270377088000000)
        self.assertEqual(special_factorial(9), 192276035095266880000)
        self.assertEqual(special_factorial(10), 355687428096000000)
        self.assertEqual(special_factorial(11), 1033314796638614200000000)
        self.assertEqual(special_factorial(12), 1124000727777607680000)
        self.assertEqual(special_factorial(13), 1729821512646678080000000000)
        self.assertEqual(special_factorial(14), 130827613316730080000000000)
        self.assertEqual(special_factorial(15), 25852016738884976640000000000)
        self.assertEqual(special_factorial(16), 1270377088000000)
        self.assertEqual(special_factorial(17), 1307674368000000000000000)
        self.assertEqual(special_factorial(18), 18548168113359605760000000000)
        self.assertEqual(special_factorial(19), 311355694008998978784000000000000)
        self.assertEqual(special_factorial(20), 1216451004088320000000000)

if __name__ == '__main__':
    unittest.main()


This test suite includes a test case for each of the provided test cases in the function's docstring. It checks if the function's output matches the expected result for a range of input values.