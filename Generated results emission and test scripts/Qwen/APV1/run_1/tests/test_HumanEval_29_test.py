system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
from HumanEval_29_code import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_single_element(self):
        self.assertEqual(filter_by_prefix(['abc'], 'a'), ['abc'])

    def test_multiple_elements(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_prefix_in_middle(self):
        self.assertEqual(filter_by_prefix(['apple', 'banana', 'apricot', 'cherry'], 'ap'), ['apple', 'apricot'])

    def test_prefix_at_start(self):
        self.assertEqual(filter_by_prefix(['apple', 'banana', 'apricot', 'cherry'], ''), ['apple', 'banana', 'apricot', 'cherry'])

    def test_prefix_not_found(self):
        self.assertEqual(filter_by_prefix(['apple', 'banana', 'apricot', 'cherry'], 'z'), [])

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestFilterByPrefix` class that inherits from `unittest.TestCase`. It contains several test methods to verify the correctness of the `filter_by_prefix` function. Each method tests different scenarios such as empty lists, single elements, multiple elements including those starting and not starting with the specified prefix, and cases where the prefix is at the beginning or does not exist in any element. The `unittest.main()` call at the end runs all the test methods when this script is executed directly.