You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_144_code import simplify
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if (numerator / denom == int(numerator / denom)):
        return True
    return False

 import unittest
from HumanEval_144_code import simplify

class TestSimplifyFunction(unittest.TestCase):

    def test_simplify_whole_number(self):
        self.assertTrue(simplify("1/5", "5/1"))

    def test_simplify_not_whole_number(self):
        self.assertFalse(simplify("1/6", "2/1"))

    def test_simplify_not_whole_number_2(self):
        self.assertFalse(simplify("7/10", "10/2"))

    def test_simplify_zero_denominator(self):
        with self.assertRaises(ValueError):
            simplify("1/0", "1/1")

    def test_simplify_negative_numbers(self):
        with self.assertRaises(ValueError):
            simplify("-1/5", "-5/1")

    def test_simplify_non_integer_numbers(self):
        with self.assertRaises(ValueError):
            simplify("1/3", "2/1.5")

if __name__ == '__main__':
    unittest.main()