system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_29_code import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_no_match(self):
        self.assertEqual(filter_by_prefix(['bcd', 'cde', 'def'], 'a'), [])

    def test_one_match(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde'], 'a'), ['abc'])

    def test_multiple_matches(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_case_insensitive(self):
        self.assertEqual(filter_by_prefix(['Abc', 'AbC', 'abc'], 'a'), ['Abc', 'abc'])

    def test_prefix_with_characters(self):
        self.assertEqual(filter_by_prefix(['abc', 'abcd', 'abcde'], 'abc'), ['abc', 'abcd', 'abcde'])

if __name__ == '__main__':
    unittest.main()