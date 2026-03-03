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

 Here is a comprehensive unittest test suite for the `filter_by_substring` function:


import unittest
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(filter_by_substring([], 'abc'), [])

    def test_single_string(self):
        self.assertListEqual(filter_by_substring(['abc'], 'abc'), ['abc'])
        self.assertListEqual(filter_by_substring(['abc'], 'def'), [])

    def test_multiple_strings(self):
        self.assertListEqual(filter_by_substring(['abc', 'def', 'ab'], 'ab'), ['abc', 'ab'])
        self.assertListEqual(filter_by_substring(['abc', 'def', 'ab'], 'xyz'), [])

    def test_substring_at_beginning(self):
        self.assertListEqual(filter_by_substring(['abcd', 'xyzab', 'abc'], 'ab'), ['abcd', 'xyzab', 'abc'])

    def test_substring_in_middle(self):
        self.assertListEqual(filter_by_substring(['abcdef', 'xyzabcd', 'abc'], 'abc'), ['abcdef', 'abc'])

    def test_substring_at_end(self):
        self.assertListEqual(filter_by_substring(['abcdef', 'xyzabcd', 'abc'], 'abc'), ['abcdef', 'abc'])

    def test_substring_case_insensitive(self):
        self.assertListEqual(filter_by_substring(['AbCd', 'xyzABC', 'abc'], 'abc'), ['AbCd', 'xyzABC', 'abc'])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to check the function's behavior with empty lists, single strings, multiple strings, substrings at the beginning, in the middle, and at the end of the strings, case-insensitive substrings, and edge cases.