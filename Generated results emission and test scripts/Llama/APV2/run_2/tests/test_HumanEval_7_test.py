system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
    return [x for x in strings if substring in x]assistant

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):

    def test_filter_by_substring(self):
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], 'ab'), ['abc', 'ab'])
        self.assertEqual(filter_by_substring(['abc', 'def', 'ghi'], 'def'), ['def'])
        self.assertEqual(filter_by_substring(['abc', 'def', 'ghi'], 'xyz'), [])
        self.assertEqual(filter_by_substring(['abc', 'def', 'ghi'], ''), [])
        self.assertEqual(filter_by_substring([], 'abc'), [])
        self.assertEqual(filter_by_substring(['abc'], 'xyz'), [])

if __name__ == '__main__':
    unittest.main()