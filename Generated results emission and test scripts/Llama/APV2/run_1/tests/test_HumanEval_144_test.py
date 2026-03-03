system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
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
    return Falseassistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_144_code import simplify

class TestSimplifyFunction(unittest.TestCase):

    def test_simplify_true(self):
        self.assertTrue(simplify("1/5", "5/1"))

    def test_simplify_false(self):
        self.assertFalse(simplify("1/6", "2/1"))

    def test_simplify_false2(self):
        self.assertFalse(simplify("7/10", "10/2"))

    def test_simplify_true2(self):
        self.assertTrue(simplify("2/4", "4/2"))

    def test_simplify_false3(self):
        self.assertFalse(simplify("3/4", "5/2"))

    def test_simplify_true4(self):
        self.assertTrue(simplify("1/1", "1/1"))

    def test_simplify_false5(self):
        self.assertFalse(simplify("1/2", "3/4"))

if __name__ == '__main__':
    unittest.main()