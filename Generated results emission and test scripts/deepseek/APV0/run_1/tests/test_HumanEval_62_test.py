You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_62_code import derivative
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def derivative(xs: list):
    """xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [(i * x) for i, x in enumerate(xs)][1:]


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_62_code import derivative

class TestDerivative(unittest.TestCase):
    def test_derivative(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])
        self.assertEqual(derivative([1, 2, 3]), [2, 6])
        self.assertEqual(derivative([]), [])
        self.assertEqual(derivative([0]), [])
        self.assertEqual(derivative([1]), [0])
        self.assertEqual(derivative([1, 0, 0, 0]), [0, 0, 0])
        self.assertEqual(derivative([0, 1, 0, 0]), [0, 0])
        self.assertEqual(derivative([0, 0, 1, 0]), [0])
        self.assertEqual(derivative([0, 0, 0, 1]), [])

if __name__ == '__main__':
    unittest.main()


This script includes a test case for the derivative function with various input lists. It checks that the function returns the correct output for each input.

Please note that the function `derivative` is expected to be in a file named `HumanEval_62_code.py` in the same directory as the test script. The function should be defined in the file as follows:


def derivative(xs: list):
    """xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Return derivative of this polynomial in the same form.
    """
    return [(i * x) for i, x in enumerate(xs)][1:]


The script can be run directly to execute the tests. If all tests pass, the script will exit without output. If any test fails, the script will output a message indicating which test failed and why.