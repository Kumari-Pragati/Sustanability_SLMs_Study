You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 import unittest
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):

    def test_filter_by_substring_with_matching_strings(self):
        input_strings = ['abc', 'def', 'ab']
        substring = 'ab'
        expected_output = ['abc', 'ab']
        self.assertEqual(filter_by_substring(input_strings, substring), expected_output)

    def test_filter_by_substring_with_no_matching_strings(self):
        input_strings = ['xyz', '123', 'abc']
        substring = 'ab'
        expected_output = []
        self.assertEqual(filter_by_substring(input_strings, substring), expected_output)

    def test_filter_by_substring_with_empty_list(self):
        input_strings = []
        substring = 'ab'
        expected_output = []
        self.assertEqual(filter_by_substring(input_strings, substring), expected_output)

    def test_filter_by_substring_with_empty_substring(self):
        input_strings = ['abc', 'def', 'ab']
        substring = ''
        expected_output = []
        self.assertEqual(filter_by_substring(input_strings, substring), expected_output)

    def test_filter_by_substring_with_case_insensitive_matching(self):
        input_strings = ['Abc', 'def', 'aB']
        substring = 'ab'
        expected_output = ['Abc', 'aB']
        self.assertEqual(filter_by_substring(input_strings, substring), expected_output)

if __name__ == '__main__':
    unittest.main()