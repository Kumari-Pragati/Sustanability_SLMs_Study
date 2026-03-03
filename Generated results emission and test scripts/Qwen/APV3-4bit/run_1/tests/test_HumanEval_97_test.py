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
   - Include from HumanEval_97_code import multiply
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
2. Include: from HumanEval_97_code import multiply
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.

    Examples:
    multiply(148, 412) ➞ 16
    multiply(19, 28) ➞ 72
    multiply(2020, 1851) ➞ 0
    multiply(14, -15) ➞ 20
    """

    return abs(a % 10) * abs(b % 10)


assistant

import unittest

# Importing the function we want to test
from HumanEval_97_code import multiply

class TestMultiply(unittest.TestCase):
    
    # Test case for positive numbers
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(148, 412), 16)
        
    # Test case for negative numbers
    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-14, -15), 20)
        
    # Test case for zero multiplication (should return 0)
    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 0), 0)
        
    # Test case for large numbers
    def test_large_numbers(self):
        self.assertEqual(multiply(123456789, 987654321), 561782912)
        
    # Test case for floating point numbers (should raise an error)
    def test_floats(self):
        with self.assertRaises(TypeError):
            multiply(1.5, 2.5)
            
    # Test case for non-integer types (should raise an error)
    def test_non_integer_types(self):
        with self.assertRaises(TypeError):
            multiply('a', 'b')
            
    # Test case for empty tuple (should raise an error)
    def test_empty_tuple(self):
        with self.assertRaises(ValueError):
            multiply(*())
            
    # Test case for mixed data types (should raise an error)
    def test_mixed_data_types(self):
        with self.assertRaises(TypeError):
            multiply(1, [2])
            
    # Test case for string arguments (should raise an error)
    def test_string_arguments(self):
        with self.assertRaises(TypeError):
            multiply("a", "b")
            
    # Test case for None as first argument (should raise an error)
    def test_none_as_first_argument(self):
        with self.assertRaises(TypeError):
            multiply(None, 2)
            
    # Test case for None as second argument (should raise an error)
    def test_none_as_second_argument(self):
        with self.assertRaises(TypeError):
            multiply(1, None)
            
    # Test case for float as first argument (should raise an error)
    def test_float_as_first_argument(self):
        with self.assertRaises(TypeError):
            multiply(float('inf'), 2)
            
    # Test case for float as second argument (should raise an error)
    def test_float_as_second_argument(self):
        with self.assertRaises(TypeError):
            multiply(1, float('nan'))
            
    # Test case for complex number as first argument (should raise an error)
    def test_complex_number_as_first_argument(self):
        with self.assertRaises(TypeError):
            multiply(complex(1, 2), 2)
            
    # Test case for complex number as second argument (should raise an error)
    def test_complex_number_as_second_argument(self):
        with self.assertRaises(TypeError):
            multiply(1, complex(1, 2))
            
    # Test case for imaginary part as first argument (should raise an error)
    def test_imaginary_part_as_first_argument(self):
        with self.assertRaises(TypeError):
            multiply(1j, 2)
            
    # Test case for imaginary part as second argument (should raise an error)
    def test_imaginary_part_as_second_argument(self):
        with self.assertRaises(TypeError):
            multiply(1j, 2j)
            
    # Test case for complex number as both arguments (should raise an error)
    def test_complex_number_both_arguments(self):
        with self.assertRaises(TypeError):
            multiply(complex(1, 2), complex(3, 4))

if __name__ == '__main__':
    unittest.main()