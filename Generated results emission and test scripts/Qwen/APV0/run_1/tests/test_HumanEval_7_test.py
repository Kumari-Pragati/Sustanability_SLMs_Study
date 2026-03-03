system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return [x for x in strings if substring in x]


assistant

import unittest

# Define the function to be tested
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):
    def test_filter_by_substring(self):
        # Test case 1: Empty input list
        self.assertEqual(filter_by_substring([], "a"), [])

        # Test case 2: Single element list
        self.assertEqual(filter_by_substring(["hello"], "l"), ["hello"])

        # Test case 3: Multiple elements list containing the substring
        self.assertEqual(filter_by_substring(["apple", "banana", "cherry", "date"], "an"), ["banana"])

        # Test case 4: Multiple elements list not containing the substring
        self.assertEqual(filter_by_substring(["dog", "cat", "elephant"], "fish"), [])

        # Test case 5: Case-insensitive search (using lower() method)
        self.assertEqual(filter_by_substring(["Apple", "Banana", "Cherry"], "ban"), ["Banana"])

    def test_edge_cases(self):
        # Test case 6: Substring is empty string
        self.assertEqual(filter_by_substring(["test", "code", "testing"], ""), [])

        # Test case 7: Substring length greater than any string in the list
        self.assertEqual(filter_by_substring(["longerword", "shorterword"], "superlong"), [])

        # Test case 8: Substring appears multiple times in one string
        self.assertEqual(filter_by_substring(["multiple", "occurrences", "of", "the", "same", "substring"], "sub"), ["multiple", "occurrences", "of", "the", "same", "substring"])

if __name__ == '__main__':
    unittest.main()


This script defines a unit test class `TestFilterBySubstring` that tests various scenarios using the provided `filter_by_substring` function. It includes both positive and negative cases as well as edge cases to ensure comprehensive testing. The `unittest.main()` call at the end makes the tests executable when run directly.