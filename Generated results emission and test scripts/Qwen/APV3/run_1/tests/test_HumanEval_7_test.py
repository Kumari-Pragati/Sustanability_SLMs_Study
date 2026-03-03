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
   - Include from HumanEval_7_code import filter_by_substring
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
2. Include: from HumanEval_7_code import filter_by_substring
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter the list of strings and return only those that contain `substring`.
    >>> filter_by_substring(['abc', 'def', 'ab'], 'ab')
    ['abc', 'ab']
    """
    return [x for x in strings if substring in x]


assistant

import unittest

# Importing the function from the given context
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):
    
    # Test case for positive numbers
    def test_positive_numbers(self):
        result = filter_by_substring([1, 2, 3, 4], '3')
        expected_result = [3]
        self.assertEqual(result, expected_result)
        
    # Test case for negative numbers
    def test_negative_numbers(self):
        result = filter_by_substring([-1, -2, -3], '-2')
        expected_result = [-2]
        self.assertEqual(result, expected_result)
        
    # Test case for empty list
    def test_empty_list(self):
        result = filter_by_substring([], 'a')
        expected_result = []
        self.assertEqual(result, expected_result)
        
    # Test case with mixed types (should raise TypeError)
    def test_mixed_types(self):
        try:
            result = filter_by_substring(['abc', 123, True], 'b')
            self.fail("Expected TypeError")
        except TypeError as e:
            self.assertTrue(str(e).startswith('filter_by_substring() takes exactly 2 arguments (3 given)'))
            
    # Test case with no matching substring
    def test_no_matching_substring(self):
        result = filter_by_substring(['hello', 'world'], 'xyz')
        expected_result = []
        self.assertEqual(result, expected_result)
        
    # Test case with multiple matches
    def test_multiple_matches(self):
        result = filter_by_substring(['apple', 'banana', 'cherry', 'date'], 'an')
        expected_result = ['banana', 'ananas']
        self.assertEqual(result, expected_result)
        
    # Test case with string containing substring
    def test_string_with_substring(self):
        result = filter_by_substring(['test', 'sub', 'testcase'], 'te')
        expected_result = ['test', 'testcase']
        self.assertEqual(result, expected_result)
        
    # Test case with None input
    def test_none_input(self):
        with self.assertRaises(TypeError):
            filter_by_substring(None, 'n')

if __name__ == '__main__':
    unittest.main()