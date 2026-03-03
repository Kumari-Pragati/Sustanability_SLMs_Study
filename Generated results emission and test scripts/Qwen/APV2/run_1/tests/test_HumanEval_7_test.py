system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Provided function
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):
    
    def test_filter_by_substring(self):
        # Test case 1
        result = filter_by_substring(['abc', 'def', 'ab'], 'ab')
        self.assertEqual(result, ['abc', 'ab'])
        
        # Test case 2
        result = filter_by_substring(['hello', 'world', 'hi'], 'lo')
        self.assertEqual(result, ['hello', 'world'])

        # Test case 3
        result = filter_by_substring([], 'test')
        self.assertEqual(result, [])
        
        # Test case 4
        result = filter_by_substring(['a', 'b', 'c'], '')
        self.assertEqual(result, ['a', 'b', 'c'])

        # Test case 5
        result = filter_by_substring(['one', 'two', 'three', 'four'], 't')
        self.assertEqual(result, ['two', 'three'])

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to ensure the `filter_by_substring` function behaves as expected under different conditions.