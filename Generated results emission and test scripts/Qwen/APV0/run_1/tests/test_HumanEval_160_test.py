system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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


assistant

import unittest

# Importing the function to be tested
from HumanEval_160_code import do_algebra

class TestDoAlgebra(unittest.TestCase):

    def test_addition(self):
        operator = ['+']
        operand = [1, 2, 3]
        self.assertEqual(do_algebra(operator, operand), 6)

    def test_subtraction(self):
        operator = ['-']
        operand = [10, 2, 3]
        self.assertEqual(do_algebra(operator, operand), 5)

    def test_multiplication(self):
        operator = ['*']
        operand = [2, 3, 4]
        self.assertEqual(do_algebra(operator, operand), 24)

    def test_floor_division(self):
        operator = ['//']
        operand = [8, 2, 3]
        self.assertEqual(do_algebra(operator, operand), 2)

    def test_exponentiation(self):
        operator = ['**']
        operand = [2, 3, 4]
        self.assertEqual(do_algebra(operator, operand), 16)

    def test_multiple_operators(self):
        operator = ['+', '**', '//']
        operand = [2, 3, 4, 5]
        self.assertEqual(do_algebra(operator, operand), 9)

    def test_empty_operator(self):
        operator = []
        operand = [1, 2, 3]
        with self.assertRaises(ValueError):
            do_algebra(operator, operand)

    def test_incorrect_length(self):
        operator = ['+', '*']
        operand = [1, 2, 3]
        with self.assertRaises(AssertionError):
            do_algebra(operator, operand)

    def test_negative_operand(self):
        operator = ['-', '+']
        operand = [-1, 2, 3]
        with self.assertRaises(ValueError):
            do_algebra(operator, operand)

if __name__ == '__main__':
    unittest.main()


This script defines a `unittest` test case class named `TestDoAlgebra`. It includes several test methods that cover various scenarios of the `do_algebra` function, such as addition, subtraction, multiplication, floor division, exponentiation, handling multiple operators, empty operator list, incorrect length, and negative operands. Each method uses assertions to check if the function behaves as expected under different conditions. If any assertion fails, it will raise an exception indicating which condition was not met.