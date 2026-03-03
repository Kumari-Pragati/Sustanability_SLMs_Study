You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_26_code import remove_duplicates
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_26_code import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_no_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_one_duplicate(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 4]), [1, 3, 4])

    def test_multiple_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 2, 3, 4]), [1, 3, 4])

    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_all_duplicates(self):
        self.assertEqual(remove_duplicates([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])

    def test_negative_numbers(self):
        self.assertEqual(remove_duplicates([-1, -2, -2, -3, -3]), [-1, -2, -3])

    def test_mixed_numbers(self):
        self.assertEqual(remove_duplicates([1, -2, 2, -2, 3]), [1, 3])

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure that the function is working correctly. It tests the function with lists that have no duplicates, one duplicate, multiple duplicates, an empty list, lists with all duplicates, negative numbers, and a mix of positive and negative numbers.