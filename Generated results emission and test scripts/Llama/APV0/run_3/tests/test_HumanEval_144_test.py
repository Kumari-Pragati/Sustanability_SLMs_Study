user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_144_code import simplify

class TestSimplify(unittest.TestCase):

    def test_simplify(self):
        self.assertTrue(simplify("1/5", "5/1"))
        self.assertFalse(simplify("1/6", "2/1"))
        self.assertFalse(simplify("7/10", "10/2"))
        self.assertTrue(simplify("2/4", "4/2"))
        self.assertFalse(simplify("1/2", "3/4"))
        self.assertTrue(simplify("3/6", "6/3"))
        self.assertFalse(simplify("1/3", "2/4"))
        self.assertTrue(simplify("2/2", "2/2"))
        self.assertFalse(simplify("1/2", "3/6"))

if __name__ == '__main__':
    unittest.main()


This script includes 9 test cases to cover different scenarios. The `assertTrue` method is used to check if the function returns `True` for the expected inputs, and the `assertFalse` method is used to check if the function returns `False` for the expected inputs.