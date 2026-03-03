system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
from HumanEval_22_code import filter_integers

# Test cases for the filter_integers function
class TestFilterIntegers(unittest.TestCase):
    def test_filter_integers(self):
        # Test case 1: Filter out non-integer values
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])

        # Test case 2: Filter out mixed types and empty lists
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

        # Test case 3: Filter out all non-integers
        self.assertEqual(filter_integers(['hello', [], None, True, False, 0, -1]), [])

        # Test case 4: Filter out negative numbers
        self.assertEqual(filter_integers([-1, -2, -3, 4, 5]), [-1, -2, -3])

        # Test case 5: Filter out positive numbers
        self.assertEqual(filter_integers([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_empty_input(self):
        self.assertEqual(filter_integers([]), [])

    def test_single_element(self):
        self.assertEqual(filter_integers([7]), [7])

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestFilterIntegers` class that inherits from `unittest.TestCase`. It contains several test methods to verify the functionality of the `filter_integers` function. The tests cover various scenarios including filtering out non-integer values, handling mixed types, empty lists, negative numbers, positive numbers, and single-element inputs. The `unittest.main()` call at the end runs these tests when the script is executed directly.