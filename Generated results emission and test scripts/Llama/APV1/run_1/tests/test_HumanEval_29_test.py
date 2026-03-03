user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
    return [x for x in strings if x.startswith(prefix)]assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_29_code import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_no_match(self):
        self.assertEqual(filter_by_prefix(['bcd', 'cde', 'def'], 'a'), [])

    def test_single_match(self):
        self.assertEqual(filter_by_prefix(['abc'], 'a'), ['abc'])

    def test_multiple_matches(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_case_insensitive_match(self):
        self.assertEqual(filter_by_prefix(['Abc', 'AbC', 'abc'], 'a'), ['Abc', 'AbC', 'abc'])

    def test_prefix_with_characters(self):
        self.assertEqual(filter_by_prefix(['abc123', 'abc456', 'def789'], 'abc'), ['abc123', 'abc456'])

    def test_prefix_with_digits(self):
        self.assertEqual(filter_by_prefix(['123abc', '456def', '789ghi'], '123'), ['123abc'])

    def test_prefix_with_special_characters(self):
        self.assertEqual(filter_by_prefix(['abc@def', 'ghi#jkl','mno$xyz'], 'abc@'), ['abc@def'])

    def test_empty_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde'], ''), ['abc', 'bcd', 'cde'])

    def test_none_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde'], None), [])

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios, including:

- Filtering an empty list
- Filtering a list with no matches
- Filtering a list with a single match
- Filtering a list with multiple matches
- Filtering a list with case-insensitive matches
- Filtering a list with a prefix containing characters, digits, and special characters
- Filtering a list with an empty prefix
- Filtering a list with a None prefix