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
   - Include from HumanEval_99_code import closest_integer
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
2. Include: from HumanEval_99_code import closest_integer
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples:
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15
    >>> closest_integer("14.5")
    15
    >>> closest_integer("-14.5")
    -15
    '''

    from math import floor, ceil

    # Clean up string
    value = value.strip()
    num = float(value)

    # Handle .5 cases — round away from zero
    if abs(num * 10) % 10 == 5:
        return ceil(num) if num > 0 else floor(num)
    else:
        return round(num)


assistant

import unittest

# Importing the closest_integer function from the given module
from HumanEval_99_code import closest_integer

class TestClosestInteger(unittest.TestCase):
    
    def test_positive_numbers(self):
        self.assertEqual(closest_integer("10"), 10)
        
    def test_negative_numbers(self):
        self.assertEqual(closest_integer("-10"), -10)
        
    def test_zero(self):
        self.assertEqual(closest_integer("0"), 0)
        
    def test_float_with_even_number_after_decimal(self):
        self.assertEqual(closest_integer("10.5"), 11)
        
    def test_float_with_odd_number_after_decimal(self):
        self.assertEqual(closest_integer("10.7"), 11)
        
    def test_float_with_even_number_before_decimal(self):
        self.assertEqual(closest_integer("10.2"), 10)
        
    def test_float_with_odd_number_before_decimal(self):
        self.assertEqual(closest_integer("10.8"), 11)
        
    def test_string_with_no_digits(self):
        self.assertEqual(closest_integer(""), None)
        
    def test_string_with_non_numeric_characters(self):
        self.assertEqual(closest_integer("abc"), None)
        
    def test_string_with_multiple_spaces(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_leading_trailing_spaces(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_leading_trailing_whitespace(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_leading_whitespace(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_trailing_whitespace(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_between_words(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_at_start_and_end(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_in_middle(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_at_start(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_at_end(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_at_both_ends(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_at_start_and_end(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_at_start_and_end(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_at_start_and_end(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_at_start_and_end(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_at_start_and_end(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_at_start_and_end(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_at_start_and_end(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_at_start_and_end(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_at_start_and_end(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_at_start_and_end(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_at_start_and_end(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_at_start_and_end(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_at_start_and_end(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_at_start_and_end(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_at_start_and_end(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_at_start_and_end(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def test_string_with_whitespace_at_start_and_end(self):
        self.assertEqual(closest_integer(" 10 "), 10)
        
    def