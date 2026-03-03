system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Function to be tested
from HumanEval_160_code import do_algebra

class TestDoAlgebra(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(do_algebra(['+'], [1, 2]), 3)

    def test_subtraction(self):
        self.assertEqual(do_algebra(['-', '*'], [1, 2, 3, 4]), 1)

    def test_multiplication(self):
        self.assertEqual(do_algebra(['*', '/'], [2, 3, 4, 5]), 8 / 5)

    def test_floor_division(self):
        self.assertEqual(do_algebra(['//', '+'], [7, 3, 2, 1]), 4)

    def test_exponentiation(self):
        self.assertEqual(do_algebra(['**', '+'], [2, 3, 4, 5]), 2 ** (3 + 4))

    def test_multiple_operands(self):
        self.assertEqual(
            do_algebra(['+', '-', '*'], [1, 2, 3, 4, 5]),
            1 + 2 * 3 - 4 * 5
        )

    def test_operator_length_mismatch(self):
        with self.assertRaises(AssertionError):
            do_algebra(['+', '*'], [1, 2, 3])

    def test_operand_non_integers(self):
        with self.assertRaises(TypeError):
            do_algebra(['+', '*'], [1.5, 2, 3, 4])

    def test_empty_operator(self):
        with self.assertRaises(ValueError):
            do_algebra([], [])

    def test_negative_operands(self):
        with self.assertRaises(ValueError):
            do_algebra(['+', '-'], [-1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various scenarios including addition, subtraction, multiplication, floor division, exponentiation, multiple operands, mismatched operators, non-integer operands, empty operator list, and negative operands. It uses `assertEqual` to check if the results match expected outcomes and raises appropriate exceptions when necessary.