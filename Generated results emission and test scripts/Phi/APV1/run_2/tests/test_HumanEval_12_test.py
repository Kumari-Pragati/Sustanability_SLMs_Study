You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_12_code import longest

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s

 import unittest
from HumanEval_12_code import longest

class TestLongestFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_string(self):
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_strings_same_length(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_multiple_strings_different_lengths(self):
        self.assertEqual(longest(['a', 'bb', 'c']), 'bb')

    def test_longest_string_at_beginning(self):
        self.assertEqual(longest(['bb', 'a', 'ccc']), 'bb')

    def test_longest_string_at_end(self):
        self.assertEqual(longest(['a', 'ccc', 'bb']), 'ccc')

    def test_longest_string_in_middle(self):
        self.assertEqual(longest(['a', 'ccc', 'bbb']), 'ccc')

    def test_longest_string_with_spaces(self):
        self.assertEqual(longest(['a ', 'bbb', 'ccc ']), 'ccc ')

    def test_longest_string_with_special_characters(self):
        self.assertEqual(longest(['a!', 'bbb', 'ccc@']), 'ccc@')

    def test_longest_string_with_numbers(self):
        self.assertEqual(longest(['a1', 'bbb2', 'ccc3']), 'ccc3')

    def test_longest_string_with_mixed_case(self):
        self.assertEqual(longest(['aB', 'bbb', 'CCC']), 'CCC')

if __name__ == '__main__':
    unittest.main()