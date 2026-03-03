You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

 import unittest
from HumanEval_160_code import do_algebra

class TestDoAlgebra(unittest.TestCase):

    def test_addition(self):
        operator = ['+']
        operand = [2, 3]
        result = do_algebra(operator, operand)
        self.assertEqual(result, 5)

    def test_multiplication(self):
        operator = ['*']
        operand = [2, 3, 4]
        result = do_algebra(operator, operand)
        self.assertEqual(result, 24)

    def test_subtraction(self):
        operator = ['-']
        operand = [5, 2, 3]
        result = do_algebra(operator, operand)
        self.assertEqual(result, 0)

    def test_floor_division(self):
        operator = ['//']
        operand = [8, 3, 2]
        result = do_algebra(operator, operand)
        self.assertEqual(result, 1)

    def test_exponentiation(self):
        operator = ['**']
        operand = [2, 3, 2]
        result = do_algebra(operator, operand)
        self.assertEqual(result, 8)

    def test_invalid_length(self):
        operator = ['+', '*']
        operand = [2, 3]
        with self.assertRaises(ValueError):
            do_algebra(operator, operand)

    def test_invalid_operand(self):
        operator = ['+']
        operand = [2, 'a', 3]
        with self.assertRaises(TypeError):
            do_algebra(operator, operand)

    def test_empty_operand(self):
        operator = ['+']
        operand = []
        with self.assertRaises(IndexError):
            do_algebra(operator, operand)

if __name__ == '__main__':
    unittest.main()