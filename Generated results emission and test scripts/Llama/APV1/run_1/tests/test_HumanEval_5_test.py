user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

Here is a comprehensive unittest test suite for the given Python function:

Python
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

    def test_list_with_multiple_elements(self):
        self.assertEqual(intersperse([1, 2, 3, 4, 5], 4), [1, 4, 2, 4, 3, 4, 5])

    def test_list_with_negative_numbers(self):
        self.assertEqual(intersperse([-1, -2, -3], 4), [-1, 4, -2, 4, -3])

    def test_list_with_zero(self):
        self.assertEqual(intersperse([0, 1, 2], 4), [0, 4, 1, 4, 2])

    def test_list_with_duplicates(self):
        self.assertEqual(intersperse([1, 1, 2, 2, 3], 4), [1, 4, 1, 4, 2, 4, 2, 4, 3])

    def test_list_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            intersperse([1, 2, 'a'], 4)

    def test_non_integer_delimeter(self):
        with self.assertRaises(TypeError):
            intersperse([1, 2, 3], 'a')

if __name__ == '__main__':
    unittest.main()


This test suite covers various edge cases, including empty lists, single-element lists, lists with multiple elements, lists with negative numbers, lists with zero, lists with duplicates, and lists with non-integer elements. It also tests the function with a non-integer delimeter.