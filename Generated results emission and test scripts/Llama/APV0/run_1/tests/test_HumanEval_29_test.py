user

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
    return [x for x in strings if x.startswith(prefix)]assistant

Here is the unittest test script for the `filter_by_prefix` function:

import unittest
from HumanEval_29_code import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_no_matches(self):
        self.assertEqual(filter_by_prefix(['bcd', 'cde', 'def'], 'a'), [])

    def test_single_match(self):
        self.assertEqual(filter_by_prefix(['abc'], 'a'), ['abc'])

    def test_multiple_matches(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_case_insensitive_match(self):
        self.assertEqual(filter_by_prefix(['Abc', 'Abd', 'Acd'], 'a'), ['Abc', 'Abd', 'Acd'])

    def test_prefix_with_spaces(self):
        self.assertEqual(filter_by_prefix(['abc def', 'bcd efg', 'cde fgh'], 'abc '), ['abc def'])

    def test_prefix_with_special_chars(self):
        self.assertEqual(filter_by_prefix(['abc!def', 'bcd?ghi', 'cde*jkl'], 'abc!'), ['abc!def'])

if __name__ == '__main__':
    unittest.main()

This script defines a `TestFilterByPrefix` class with six test methods:

1. `test_empty_input`: Tests that an empty input list returns an empty output list.
2. `test_no_matches`: Tests that a list with no matches returns an empty output list.
3. `test_single_match`: Tests that a list with a single match returns a list with that match.
4. `test_multiple_matches`: Tests that a list with multiple matches returns a list with all those matches.
5. `test_case_insensitive_match`: Tests that the function is case-insensitive by testing a list with uppercase and lowercase matches.
6. `test_prefix_with_spaces`: Tests that the function works with prefixes that contain spaces.
7. `test_prefix_with_special_chars`: Tests that the function works with prefixes that contain special characters.

Each test method uses the `assertEqual` method to check that the output of the `filter_by_prefix` function matches the expected output.