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
   - Include from HumanEval_29_code import filter_by_prefix
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
2. Include: from HumanEval_29_code import filter_by_prefix
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [x for x in strings if x.startswith(prefix)]


assistant

import unittest

# Importing the filter_by_prefix function from the module where it's defined
from HumanEval_29_code import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):
    
    # Test case for empty string input
    def test_empty_string_input(self):
        result = filter_by_prefix([], 'prefix')
        expected_result = []
        self.assertEqual(result, expected_result)
        
    # Test case for non-empty string input
    def test_non_empty_string_input(self):
        result = filter_by_prefix(['prefix', 'another_prefix', 'yet_another_prefix'], 'prefix')
        expected_result = ['prefix']
        self.assertEqual(result, expected_result)
        
    # Test case for mixed string types (strings and numbers)
    def test_mixed_string_types(self):
        result = filter_by_prefix(['prefix', 123, 'another_prefix'], 'prefix')
        expected_result = ['prefix']
        self.assertEqual(result, expected_result)
        
    # Test case for no matching prefixes
    def test_no_matching_prefixes(self):
        result = filter_by_prefix(['no_match', 'prefix', 'no_match'], 'not_a_prefix')
        expected_result = []
        self.assertEqual(result, expected_result)
        
    # Test case for one matching prefix
    def test_one_matching_prefix(self):
        result = filter_by_prefix(['prefix', 'no_match', 'prefix'], 'prefix')
        expected_result = ['prefix']
        self.assertEqual(result, expected_result)
        
    # Test case for two matching prefixes
    def test_two_matching_prefixes(self):
        result = filter_by_prefix(['prefix', 'prefix', 'prefix'], 'p')
        expected_result = ['prefix']
        self.assertEqual(result, expected_result)
        
    # Test case for three matching prefixes
    def test_three_matching_prefixes(self):
        result = filter_by_prefix(['prefix', 'prefix', 'prefix'], 'pr')
        expected_result = ['prefix']
        self.assertEqual(result, expected_result)
        
    # Test case for four matching prefixes
    def test_four_matching_prefixes(self):
        result = filter_by_prefix(['prefix', 'prefix', 'prefix', 'prefix'], 'pre')
        expected_result = ['prefix']
        self.assertEqual(result, expected_result)
        
    # Test case for five matching prefixes
    def test_five_matching_prefixes(self):
        result = filter_by_prefix(['prefix', 'prefix', 'prefix', 'prefix', 'prefix'], 'pref')
        expected_result = ['prefix']
        self.assertEqual(result, expected_result)
        
    # Test case for six matching prefixes
    def test_six_matching_prefixes(self):
        result = filter_by_prefix(['prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix'], 'pref')
        expected_result = ['prefix']
        self.assertEqual(result, expected_result)
        
    # Test case for seven matching prefixes
    def test_seven_matching_prefixes(self):
        result = filter_by_prefix(['prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix'], 'prefi')
        expected_result = ['prefix']
        self.assertEqual(result, expected_result)
        
    # Test case for eight matching prefixes
    def test_eight_matching_prefixes(self):
        result = filter_by_prefix(['prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix'], 'prefi')
        expected_result = ['prefix']
        self.assertEqual(result, expected_result)
        
    # Test case for nine matching prefixes
    def test_nine_matching_prefixes(self):
        result = filter_by_prefix(['prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix'], 'prefi')
        expected_result = ['prefix']
        self.assertEqual(result, expected_result)
        
    # Test case for ten matching prefixes
    def test_ten_matching_prefixes(self):
        result = filter_by_prefix(['prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix'], 'prefi')
        expected_result = ['prefix']
        self.assertEqual(result, expected_result)
        
    # Test case for eleven matching prefixes
    def test_eleven_matching_prefixes(self):
        result = filter_by_prefix(['prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix'], 'prefi')
        expected_result = ['prefix']
        self.assertEqual(result, expected_result)
        
    # Test case for twelve matching prefixes
    def test_twelve_matching_prefixes(self):
        result = filter_by_prefix(['prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix', 'prefix'], 'prefi')
        expected_result = ['prefix']
        self.assertEqual(result, expected_result