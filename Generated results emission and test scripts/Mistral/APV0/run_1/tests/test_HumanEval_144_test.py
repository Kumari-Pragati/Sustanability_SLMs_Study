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
    return False

 Here is a unittest test script for the `simplify` function:


import unittest
from HumanEval_144_code import simplify

class TestSimplifyFunction(unittest.TestCase):
    def test_simplify(self):
        self.assertTrue(simplify("1/5", "5/1"))
        self.assertFalse(simplify("1/6", "2/1"))
        self.assertFalse(simplify("7/10", "10/2"))
        self.assertFalse(simplify("1/3", "4/12"))
        self.assertTrue(simplify("2/3", "4/6"))
        self.assertFalse(simplify("5/8", "10/16"))
        self.assertTrue(simplify("3/4", "6/8"))
        self.assertFalse(simplify("7/8", "14/16"))
        self.assertTrue(simplify("1/2", "2/4"))

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the `simplify` function, which checks if the function returns the expected results for various input combinations. The test cases cover both true and false cases, as well as some edge cases where the numerator and denominator are not co-prime.

To run the test script, save it as `test_simplify.py` and execute it using the command `python test_simplify.py`. If all the tests pass, the function is working correctly. If any tests fail, you will see an error message indicating which test failed and the expected and actual results.