You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_29_code import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_no_matching_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'z'), [])

    def test_single_matching_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_multiple_matching_prefixes(self):
        self.assertEqual(filter_by_prefix(['abc', 'abcd', 'bcd', 'cde', 'array'], 'a'), ['abc', 'abcd', 'array'])

    def test_case_sensitivity(self):
        self.assertEqual(filter_by_prefix(['Abc', 'abcd', 'bcd', 'cde', 'array'], 'a'), [])

if __name__ == '__main__':
    unittest.main()


This script includes five test cases:

1. `test_empty_list`: Tests the function with an empty list and a prefix. The expected output is also an empty list.
2. `test_no_matching_prefix`: Tests the function with a list of strings and a prefix that doesn't match any of the strings. The expected output is an empty list.
3. `test_single_matching_prefix`: Tests the function with a list of strings and a prefix that matches one of the strings. The expected output is a list containing the matching string.
4. `test_multiple_matching_prefixes`: Tests the function with a list of strings and a prefix that matches multiple of the strings. The expected output is a list containing all matching strings.
5. `test_case_sensitivity`: Tests the function with a list of strings and a prefix that matches some of the strings, but in a different case. The expected output is an empty list, because the function is case-sensitive.

To run the script, save it in a file named `test_filter_by_prefix.py` and run it using Python.