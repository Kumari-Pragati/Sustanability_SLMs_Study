You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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
    return [x for x in strings if x.startswith(prefix)]

 Here is the complete unittest test suite for the `filter_by_prefix` function:


import unittest
from HumanEval_29_code import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_no_matching_strings(self):
        self.assertEqual(filter_by_prefix(['bcd', 'cde', 'efg'], 'a'), [])

    def test_single_matching_string(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_multiple_matching_strings(self):
        self.assertEqual(filter_by_prefix(['aaa', 'abcd', 'a', 'xyz', 'array', 'apple'], 'a'), ['aaa', 'a', 'array', 'apple'])

    def test_prefix_with_spaces(self):
        self.assertEqual(filter_by_prefix(['abc', 'def', 'ghi', 'array', 'apple'], 'ab '), ['abc'])

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases to cover different scenarios:

1. An empty list with a given prefix.
2. A list with no strings that start with the given prefix.
3. A list with one or more strings that start with the given prefix.
4. A list with strings that have a prefix with spaces.

Each test case uses the `assertEqual` method to compare the expected output with the actual output of the `filter_by_prefix` function.