You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
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

 Here is the complete unittest test suite for the `filter_by_substring` function:


import unittest
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(filter_by_substring([], 'abc'), [])

    def test_single_element(self):
        self.assertListEqual(filter_by_substring(['abc'], 'abc'), ['abc'])
        self.assertListEqual(filter_by_substring(['abc'], 'def'), [])

    def test_multiple_elements(self):
        self.assertListEqual(filter_by_substring(['abc', 'def', 'ab'], 'ab'), ['abc', 'ab'])
        self.assertListEqual(filter_by_substring(['abc', 'def', 'ab'], 'xyz'), [])

    def test_case_insensitive(self):
        self.assertListEqual(filter_by_substring(['AbC', 'dEf', 'aB'], 'ab'), ['AbC', 'aB'])

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases:

1. An empty list should return an empty list for any substring.
2. A single-element list should return the element if it contains the substring, and an empty list otherwise.
3. A list with multiple elements should return only those that contain the substring.
4. The function should be case-insensitive.

Each test case uses the `assertListEqual` method to compare the expected output with the actual output of the `filter_by_substring` function.