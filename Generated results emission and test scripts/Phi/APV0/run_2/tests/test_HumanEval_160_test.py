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

 import unittest
from HumanEval_160_code import do_algebra

class TestDoAlgebra(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(do_algebra(['+', '+', '+'], [1, 2, 3, 4]), 10)

    def test_subtraction(self):
        self.assertEqual(do_algebra(['-', '-', '-'], [5, 4, 3, 2]), -10)

    def test_multiplication(self):
        self.assertEqual(do_algebra(['*', '*', '*'], [2, 3, 4, 5]), 120)

    def test_floor_division(self):
        self.assertEqual(do_algebra(['//', '//', '//'], [10, 2, 5, 1]), 1)

    def test_exponentiation(self):
        self.assertEqual(do_algebra(['**', '**', '**'], [2, 3, 4, 5]), 1024)

    def test_mixed_operations(self):
        self.assertEqual(do_algebra(['+', '-', '*', '//'], [1, 2, 3, 4, 5]), -3)

    def test_empty_operand(self):
        with self.assertRaises(IndexError):
            do_algebra(['+', '-', '*'], [1, 2])

    def test_invalid_operator(self):
        with self.assertRaises(SyntaxError):
            do_algebra(['+', 'invalid', '*'], [1, 2, 3])

    def test_non_integer_operand(self):
        with self.assertRaises(TypeError):
            do_algebra(['+', '*', '-'], [1, 'a', 3])

    def test_operator_length_mismatch(self):
        with self.assertRaises(ValueError):
            do_algebra(['+', '-'], [1, 2, 3])

if __name__ == '__main__':
    unittest.main()