You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_160_code import do_algebra
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def do_algebra(operator, operand):
    """
    Given two lists — operator and operand — build an algebraic expression and return its evaluated result.

    The basic algebra operations:
        +  Addition  
        -  Subtraction  
        *  Multiplication  
        // Floor division  
        ** Exponentiation  

    Example:
        operator = ['+', '*', '-']
        operand = [2, 3, 4, 5]
        result = 2 + 3 * 4 - 5  → 9

    Notes:
        - len(operator) == len(operand) - 1
        - operand contains non-negative integers
        - operator has at least one element
    """
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression += oprt + str(oprn)
    return eval(expression)


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_160_code import do_algebra

class TestDoAlgebra(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(do_algebra(['+'], [2, 3]), 5)
        self.assertEqual(do_algebra(['+', '+'], [1, 2, 3]), 6)
        self.assertEqual(do_algebra(['+', '+', '+'], [1, 2, 3, 4]), 10)

    def test_subtraction(self):
        self.assertEqual(do_algebra(['-'], [5, 3]), 2)
        self.assertEqual(do_algebra(['-', '-'], [10, 2, 3]), 5)
        self.assertEqual(do_algebra(['-', '-', '-'], [10, 2, 3, 1]), 6)

    def test_multiplication(self):
        self.assertEqual(do_algebra(['*'], [2, 3]), 6)
        self.assertEqual(do_algebra(['*', '*'], [2, 3, 4]), 24)
        self.assertEqual(do_algebra(['*', '*', '*'], [2, 3, 4, 5]), 120)

    def test_floor_division(self):
        self.assertEqual(do_algebra(['//'], [10, 2]), 5)
        self.assertEqual(do_algebra(['//', '//'], [10, 2, 3]), 1)
        self.assertEqual(do_algebra(['//', '//', '//'], [10, 2, 3, 1]), 1)

    def test_exponentiation(self):
        self.assertEqual(do_algebra(['**'], [2, 3]), 8)
        self.assertEqual(do_algebra(['**', '**'], [2, 3, 2]), 16)
        self.assertEqual(do_algebra(['**', '**', '**'], [2, 3, 2, 2]), 64)

    def test_mixed_operations(self):
        self.assertEqual(do_algebra(['+', '-', '*'], [1, 2, 3, 4, 5]), -1)
        self.assertEqual(do_algebra(['*', '//', '+'], [10, 2, 3, 4, 5]), 11)
        self.assertEqual(do_algebra(['**', '-', '/'], [2, 3, 4, 5, 6]), -1)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for each of the basic algebra operations and also a test for a mixed set of operations. It covers all the requirements mentioned in the function's docstring.