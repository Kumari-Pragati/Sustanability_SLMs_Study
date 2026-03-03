user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
        if i!= len(numbers) - 1:
            result.append(delimeter)
    return resultassistant

Here is the unittest test script for the `intersperse` function:

import unittest
from HumanEval_5_code import intersperse

class TestIntersperse(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element_list(self):
        self.assertEqual(intersperse([1], 4), [1])

    def test_two_element_list(self):
        self.assertEqual(intersperse([1, 2], 4), [1, 4, 2])

    def test_three_element_list(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_long_list(self):
        numbers = list(range(10))
        expected = [x for x in numbers] + [4] * (len(numbers) - 1)
        self.assertEqual(intersperse(numbers, 4), expected)

    def test_negative_delimeter(self):
        self.assertEqual(intersperse([1, 2, 3], -4), [1, -4, 2, -4, 3])

    def test_zero_delimeter(self):
        self.assertEqual(intersperse([1, 2, 3], 0), [1, 0, 2, 0, 3])

if __name__ == '__main__':
    unittest.main()

This script defines a `TestIntersperse` class with six test methods:

1. `test_empty_list`: Tests that the function returns an empty list when given an empty input list.
2. `test_single_element_list`: Tests that the function returns the input list unchanged when given a single-element list.
3. `test_two_element_list`: Tests that the function inserts the delimeter between two elements.
4. `test_three_element_list`: Tests that the function inserts the delimeter between every two consecutive elements.
5. `test_long_list`: Tests that the function works correctly for longer lists.
6. `test_negative_delimeter` and `test_zero_delimeter`: Test that the function works correctly with negative and zero delimeter values.

The `unittest.main()` call at the end runs all the test methods and reports any failures or errors.