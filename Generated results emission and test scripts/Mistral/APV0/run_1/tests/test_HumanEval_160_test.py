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

 Here is a unittest test script for the `do_algebra` function:


import unittest
from HumanEval_160_code import do_algebra

class TestDoAlgebra(unittest.TestCase):

    def test_basic_operations(self):
        self.assertEqual(do_algebra(['+', '*', '-'], [2, 3, 4, 5]), 9)
        self.assertEqual(do_algebra(['-', '*', '+'], [7, 2, 3, 4]), 11)
        self.assertEqual(do_algebra(['*', '/', '+'], [8, 9, 2, 3]), 13.5)
        self.assertEqual(do_algebra(['**', '+'], [2, 3]), 8)

    def test_empty_operator_or_operand(self):
        with self.assertRaises(ValueError):
            do_algebra([], [1, 2, 3])
        with self.assertRaises(ValueError):
            do_algebra([1], [1])
        with self.assertRaises(ValueError):
            do_algebra([1, 2], [1])
        with self.assertRaises(ValueError):
            do_algebra([1, 2], [1, 2, 3, 4, 5])

    def test_non_integer_operand(self):
        with self.assertRaises(TypeError):
            do_algebra(['+', '*', '-'], [2, '3', 4, 5])

    def test_negative_operand(self):
        with self.assertRaises(ValueError):
            do_algebra(['+', '*', '-'], [-2, 3, 4, 5])

    def test_incorrect_operator_length(self):
        with self.assertRaises(ValueError):
            do_algebra(['+', '*', '-'], [2, 3, 4])
        with self.assertRaises(ValueError):
            do_algebra(['+', '*', '-'], [2, 3, 4, 5, 6])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to check the function's behavior for basic algebra operations, empty operator or operand, non-integer operand, negative operand, and incorrect operator length.