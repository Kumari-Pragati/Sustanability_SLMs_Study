Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `filter_by_substring` function:


import unittest
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(filter_by_substring([], 'abc'), [])

    def test_no_substring(self):
        self.assertListEqual(filter_by_substring(['abc', 'def', 'ab'], 'xyz'), [''])

    def test_substring_not_in_string(self):
        self.assertListEqual(filter_by_substring(['abc', 'def', 'ab'], 'cd'), [''])

    def test_substring_in_string(self):
        self.assertListEqual(filter_by_substring(['abc', 'def', 'ab'], 'ab'), ['abc', 'ab'])

    def test_multiple_strings_with_substring(self):
        self.assertListEqual(filter_by_substring(['abc', 'def', 'xyzab', 'abcdef'], 'ab'), ['abc', 'xyzab'])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as an empty list, no substring in the strings, substring not in any string, substring in some strings, and multiple strings with the substring. The test cases use the `assertListEqual` method to check if the expected output matches the actual output of the `filter_by_substring` function.