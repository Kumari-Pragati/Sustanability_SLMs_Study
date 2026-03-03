system
### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_160_code import do_algebra
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()

user
### Immediate Task
Write the complete unittest test suite for the following Python function.

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

from HumanEval_160_code import do_algebra

class TestDoAlgebra(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(do_algebra(['+'], [1, 2, 3, 4]), 7)

    def test_subtraction(self):
        self.assertEqual(do_algebra(['-', '+', '*'], [1, 2, 3, 4]), 2)

    def test_multiplication(self):
        self.assertEqual(do_algebra(['*', '/'], [1, 2, 3, 4]), 6)

    def test_floor_division(self):
        self.assertEqual(do_algebra(['//'], [10, 2, 5, 3]), 5)

    def test_exponentiation(self):
        self.assertEqual(do_algebra(['**'], [2, 3, 4, 5]), 8)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            do_algebra(['invalid_op'], [1, 2, 3])

    def test_invalid_operand(self):
        with self.assertRaises(TypeError):
            do_algebra(['+', 'invalid_op'], [1, 2, 3])

    def test_mismatched_operands(self):
        with self.assertRaises(AssertionError):
            do_algebra(['+', '+'], [1, 2, 3])

    def test_empty_operator(self):
        with self.assertRaises(AssertionError):
            do_algebra([], [1, 2, 3, 4])

    def test_single_operand(self):
        with self.assertRaises(AssertionError):
            do_algebra(['*'], [1, 2, 3, 4])

    def test_no_operands(self):
        with self.assertRaises(AssertionError):
            do_algebra(['**'], [])

    def test_zero_operand(self):
        with self.assertRaises(AssertionError):
            do_algebra(['**'], [0])

if __name__ == '__main__':
    unittest.main()