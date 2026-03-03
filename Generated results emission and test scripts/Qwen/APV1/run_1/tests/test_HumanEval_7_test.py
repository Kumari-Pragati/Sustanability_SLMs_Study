system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):
    def test_filter_by_substring(self):
        # Test case 1: Substring present in all strings
        self.assertEqual(filter_by_substring(['hello', 'world', 'hell'], 'l'), ['hello', 'hell'])

        # Test case 2: Substring not present in any string
        self.assertEqual(filter_by_substring(['apple', 'banana', 'cherry'], 'kiwi'), [])

        # Test case 3: Single element input
        self.assertEqual(filter_by_substring(['test'], 't'), ['test'])

        # Test case 4: Empty input
        self.assertEqual(filter_by_substring([], 'a'), [])

        # Test case 5: All elements have the substring
        self.assertEqual(filter_by_substring(['sub', 'substr', 'substr'], 'sub'), ['sub', 'substr', 'substr'])

        # Test case 6: Case-insensitive search (should work as expected)
        self.assertEqual(filter_by_substring(['Sub', 'SUB', 'sUb'], 'sub'), ['Sub', 'SUB', 'sUb'])

if __name__ == '__main__':
    unittest.main()


This code snippet defines a unit test suite using the `unittest` framework to verify the correctness of the `filter_by_substring` function. The tests cover various scenarios including cases where the substring is found in some but not all strings, single-element inputs, empty lists, and both case-sensitive and case-insensitive searches.