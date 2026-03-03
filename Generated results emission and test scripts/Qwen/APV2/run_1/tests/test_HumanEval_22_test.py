system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_22_code import filter_integers
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """Filter given list of any Python values only for integers.
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]


assistant

import unittest

# Provided function
from HumanEval_22_code import filter_integers

class TestFilterIntegers(unittest.TestCase):
    
    def test_filter_integers(self):
        # Test case 1
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])
        
        # Test case 2
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()


This test suite includes two test cases that cover different scenarios as specified in the docstring. The `assertEqual` method checks if the output of `filter_integers` matches the expected result.