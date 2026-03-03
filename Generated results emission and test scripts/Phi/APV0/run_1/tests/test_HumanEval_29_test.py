Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 import unittest
from HumanEval_29_code import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_filter_with_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_no_matching_prefix(self):
        self.assertEqual(filter_by_prefix(['xyz', 'bcd', 'cde', 'array'], 'a'), [])

    def test_single_string_list(self):
        self.assertEqual(filter_by_prefix(['abc'], 'a'), ['abc'])

    def test_multiple_prefixes(self):
        self.assertEqual(filter_by_prefix(['abc', 'abd', 'bcd', 'array'], 'ab'), ['abc', 'abd'])

    def test_case_insensitive(self):
        self.assertEqual(filter_by_prefix(['Abc', 'bcd', 'cde', 'array'], 'a'), ['Abc', 'array'])

if __name__ == '__main__':
    unittest.main()