You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is a complete unittest test suite for the `do_algebra` function:


import unittest
from HumanEval_160_code import do_algebra

class TestDoAlgebra(unittest.TestCase):

    def test_basic_operations(self):
        self.assertEqual(do_algebra(['+', '*', '-'], [2, 3, 4, 5]), 9)
        self.assertEqual(do_algebra(['-', '*', '+'], [2, 3, 4, 5]), -5)
        self.assertEqual(do_algebra(['*', '/', '+'], [2, 3, 6, 4]), 10)
        self.assertEqual(do_algebra(['//', '**', '+'], [2, 3, 4, 2]), 5)

    def test_empty_operator_or_operand(self):
        with self.assertRaises(ValueError):
            do_algebra([], [1, 2, 3])
        with self.assertRaises(ValueError):
            do_algebra(['+'], [1])

    def test_non_integer_operand(self):
        with self.assertRaises(TypeError):
            do_algebra(['+', '*', '-'], [2, '3', 4, 5])

    def test_operator_length_mismatch(self):
        with self.assertRaises(ValueError):
            do_algebra(['+', '*', '-'], [2, 3])
        with self.assertRaises(ValueError):
            do_algebra(['+', '*', '-'], [2, 3, 4, 5, 6])

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases:

1. `test_basic_operations` checks the function's ability to perform basic algebra operations.
2. `test_empty_operator_or_operand` checks that the function raises a ValueError when the operator or operand is empty.
3. `test_non_integer_operand` checks that the function raises a TypeError when the operand contains non-integer values.
4. `test_operator_length_mismatch` checks that the function raises a ValueError when the length of the operator does not match the length of the operand minus one.