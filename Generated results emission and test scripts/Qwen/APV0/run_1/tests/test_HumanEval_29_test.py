system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return [x for x in strings if x.startswith(prefix)]


assistant

import unittest

# Importing the function to be tested
from HumanEval_29_code import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_single_element(self):
        self.assertEqual(filter_by_prefix(['abc'], 'a'), ['abc'])

    def test_multiple_elements(self):
        self.assertEqual(
            filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'),
            ['abc', 'array']
        )

    def test_prefix_in_middle(self):
        self.assertEqual(
            filter_by_prefix(['apple', 'banana', 'apricot', 'cherry'], 'ap'),
            ['apple', 'apricot']
        )

    def test_prefix_at_start(self):
        self.assertEqual(
            filter_by_prefix(['apple', 'banana', 'apricot', 'cherry'], ''),
            ['apple', 'banana', 'apricot', 'cherry']
        )

    def test_prefix_at_end(self):
        self.assertEqual(
            filter_by_prefix(['apple', 'banana', 'apricot', 'cherry'], 'y'),
            ['apple', 'banana', 'apricot', 'cherry']
        )

if __name__ == '__main__':
    unittest.main()


This script imports the `filter_by_prefix` function and defines several test cases using the `unittest` framework to ensure the function behaves as expected under various conditions.