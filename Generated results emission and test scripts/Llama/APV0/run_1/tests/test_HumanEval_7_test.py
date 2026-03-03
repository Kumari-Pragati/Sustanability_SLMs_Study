user

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
    return [x for x in strings if substring in x]assistant

Here is the unittest test script for the `filter_by_substring` function:

import unittest
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'abc'), [])

    def test_no_matches(self):
        self.assertEqual(filter_by_substring(['xyz', 'uvw', 'pqr'], 'abc'), [])

    def test_one_match(self):
        self.assertEqual(filter_by_substring(['abc', 'def', 'ghi'], 'abc'), ['abc'])

    def test_multiple_matches(self):
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab', 'ghi'], 'ab'), ['abc', 'ab'])

    def test_substring_in_all_strings(self):
        self.assertEqual(filter_by_substring(['abc', 'abcd', 'abcde'], 'abc'), ['abc', 'abcd', 'abcde'])

    def test_substring_not_in_all_strings(self):
        self.assertEqual(filter_by_substring(['xyz', 'uvw', 'pqr'], 'abc'), [])

    def test_substring_in_first_string(self):
        self.assertEqual(filter_by_substring(['abc', 'def', 'ghi'], 'abc'), ['abc'])

    def test_substring_in_last_string(self):
        self.assertEqual(filter_by_substring(['ghi', 'def', 'abc'], 'abc'), ['abc'])

    def test_substring_in_middle_string(self):
        self.assertEqual(filter_by_substring(['def', 'abc', 'ghi'], 'abc'), ['abc'])

if __name__ == '__main__':
    unittest.main()

This script defines a `TestFilterBySubstring` class with 8 test methods, each testing a different scenario:

1. An empty list
2. No matches
3. One match
4. Multiple matches
5. Substring in all strings
6. Substring not in all strings
7. Substring in first string
8. Substring in last string
9. Substring in middle string

Each test method uses the `assertEqual` method to check that the output of the `filter_by_substring` function matches the expected output.

You can run this script directly to execute the tests.