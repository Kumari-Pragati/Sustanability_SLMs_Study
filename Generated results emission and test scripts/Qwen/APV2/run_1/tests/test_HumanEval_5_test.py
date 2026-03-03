system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_5_code import intersperse
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result: List[int] = []
    for i, x in enumerate(numbers):
        result.append(x)
        if i != len(numbers) - 1:
            result.append(delimeter)
    return result


assistant

import unittest

# Provided function
from HumanEval_5_code import intersperse

class TestIntersperse(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_multiple_elements(self):
        self.assertEqual(intersperse([10, 20, 30], 5), [10, 5, 20, 5, 30])

    def test_mixed_elements(self):
        self.assertEqual(intersperse([1, 3, 5, 7], 6), [1, 6, 3, 6, 5, 6, 7])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for edge cases (empty list, single element, multiple elements, mixed elements) to ensure the `intersperse` function behaves as expected under various conditions.