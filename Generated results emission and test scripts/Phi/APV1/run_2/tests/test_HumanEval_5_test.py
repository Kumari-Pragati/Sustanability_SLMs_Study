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
        if i != len(numbers) - 1:
            result.append(delimeter)
    return result

 import unittest
from HumanEval_5_code import intersperse
from typing import List

class TestIntersperse(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element_list(self):
        self.assertEqual(intersperse([1], 4), [1])

    def test_two_element_list(self):
        self.assertEqual(intersperse([1, 2], 4), [1, 4, 2])

    def test_three_element_list(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_four_element_list(self):
        self.assertEqual(intersperse([1, 2, 3, 4], 5), [1, 5, 2, 5, 3, 5, 4])

    def test_list_with_delimeter_at_start(self):
        self.assertEqual(intersperse([4, 1, 2, 3], 5), [4, 5, 1, 5, 2, 5, 3])

    def test_list_with_delimeter_at_end(self):
        self.assertEqual(intersperse([1, 2, 3, 4], 5), [1, 5, 2, 5, 3, 5, 4])

    def test_list_with_delimeter_multiple_elements(self):
        self.assertEqual(intersperse([1, 2, 3, 4, 5, 6], 7), [1, 7, 2, 7, 3, 7, 4, 7, 5, 7, 6])

    def test_delimeter_is_not_appended_after_last_element(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_delimeter_is_not_appended_after_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_delimeter_is_not_appended_after_single_element(self):
        self.assertEqual(intersperse([1], 4), [1])

if __name__ == '__main__':
    unittest.main()