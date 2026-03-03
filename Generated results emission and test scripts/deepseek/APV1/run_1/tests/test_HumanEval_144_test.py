You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_144_code import simplify

class TestSimplify(unittest.TestCase):

    def test_whole_number(self):
        self.assertTrue(simplify("1/5", "5/1"))
        self.assertTrue(simplify("1/6", "2/1"))
        self.assertTrue(simplify("7/10", "10/2"))

    def test_not_whole_number(self):
        self.assertFalse(simplify("1/6", "1/2"))
        self.assertFalse(simplify("7/10", "3/2"))
        self.assertFalse(simplify("1/5", "1/5"))

    def test_zero_denominator(self):
        with self.assertRaises(ZeroDivisionError):
            simplify("1/0", "1/1")
        with self.assertRaises(ZeroDivisionError):
            simplify("1/1", "1/0")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            simplify("1/a", "1/1")
        with self.assertRaises(TypeError):
            simplify("1/1", "1/a")
        with self.assertRaises(TypeError):
            simplify("1/0", "1/a")
        with self.assertRaises(TypeError):
            simplify("1/a", "1/0")

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for when the result is a whole number, when the result is not a whole number, when the denominator is zero, and when the input is invalid. It uses the `unittest` module's `unittest.TestCase` class to create test cases and the `unittest.main()` function to run the tests.

Please note that the function `simplify` from the `HumanEval_144_code` module is expected to be implemented correctly for these tests to pass.