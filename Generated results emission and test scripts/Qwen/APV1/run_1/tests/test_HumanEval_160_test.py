system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

# Function to be tested
from HumanEval_160_code import do_algebra

class TestDoAlgebra(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(do_algebra(['+'], [1, 2]), 3)

    def test_subtraction(self):
        self.assertEqual(do_algebra(['-', '+', '*'], [1, 2, 3, 4]), 0)

    def test_multiplication(self):
        self.assertEqual(do_algebra(['*', '/'], [2, 3, 4, 5]), 8)

    def test_floor_division(self):
        self.assertEqual(do_algebra(['//'], [10, 3, 2]), 3)

    def test_exponentiation(self):
        self.assertEqual(do_algebra(['**'], [2, 3, 4, 5]), 32)

    def test_multiple_operators(self):
        self.assertEqual(do_algebra(['+', '-', '*'], [1, 2, 3, 4, 5]), 7)

    def test_empty_operator_list(self):
        with self.assertRaises(ValueError):
            do_algebra([], [])

    def test_invalid_operand_type(self):
        with self.assertRaises(TypeError):
            do_algebra(['+', 'x'], [1, 2])

    def test_negative_operand(self):
        with self.assertRaises(ValueError):
            do_algebra(['+', '*', '-'], [-1, 2, 3, 4])

    def test_zero_operand(self):
        with self.assertRaises(ValueError):
            do_algebra(['+', '*', '-'], [0])

    def test_incorrect_length(self):
        with self.assertRaises(AssertionError):
            do_algebra(['+', '*', '-'], [1, 2, 3])

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestDoAlgebra` class that inherits from `unittest.TestCase`. It includes several test cases to ensure the `do_algebra` function works correctly under various conditions as specified in the problem description. Each test case uses assertions to check if the function returns the expected results or raises appropriate exceptions.