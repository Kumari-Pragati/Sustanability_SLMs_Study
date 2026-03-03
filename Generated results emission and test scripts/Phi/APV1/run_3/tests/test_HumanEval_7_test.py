You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
        # Test case where all strings contain the substring
        self.assertEqual(
            filter_by_substring(['abc', 'def', 'ab'], 'ab'),
            ['abc', 'ab']
        )

    def test_filter_by_substring_with_no_matching_strings(self):
        # Test case where no strings contain the substring
        self.assertEqual(
            filter_by_substring(['xyz', '123', 'abc'], 'ab'),
            []
        )

    def test_filter_by_substring_with_partial_matching_strings(self):
        # Test case where some strings contain the substring
        self.assertEqual(
            filter_by_substring(['abcde', 'abcd', 'efgh'], 'ab'),
            ['abcde', 'abcd']
        )

    def test_filter_by_substring_with_empty_list(self):
        # Test case where the input list is empty
        self.assertEqual(
            filter_by_substring([], 'ab'),
            []
        )

    def test_filter_by_substring_with_empty_substring(self):
        # Test case where the substring is empty
        self.assertEqual(
            filter_by_substring(['abc', 'def', 'ab'], ''),
            []
        )

    def test_filter_by_substring_with_single_string(self):
        # Test case where the input list contains only one string
        self.assertEqual(
            filter_by_substring(['abc'], 'ab'),
            ['abc']
        )

    def test_filter_by_substring_with_non_string_elements(self):
        # Test case where the input list contains non-string elements
        self.assertEqual(
            filter_by_substring(['abc', 123, 'ab'], 'ab'),
            ['abc', 'ab']
        )

if __name__ == '__main__':
    unittest.main()