user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
    return [n for n in numbers if c[n] <= 1]assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_26_code import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])
        self.assertEqual(remove_duplicates([1, 1, 2, 2, 3, 3]), [1, 2, 3])
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), [1, 2, 3, 4])
        self.assertEqual(remove_duplicates([]), [])
        self.assertEqual(remove_duplicates([1]), [1])
        self.assertEqual(remove_duplicates([1, 1]), [1])
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_remove_duplicates_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_remove_duplicates_single_element(self):
        self.assertEqual(remove_duplicates([1]), [1])

    def test_remove_duplicates_all_duplicates(self):
        self.assertEqual(remove_duplicates([1, 1, 1, 1, 1]), [1])

    def test_remove_duplicates_no_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_remove_duplicates_duplicates_at_end(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 4]), [1, 2, 3, 4])

    def test_remove_duplicates_duplicates_in_middle(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 4]), [1, 2, 3, 4])

    def test_remove_duplicates_duplicates_at_start(self):
        self.assertEqual(remove_duplicates([2, 2, 3, 4, 5]), [3, 4, 5])

    def test_remove_duplicates_duplicates_everywhere(self):
        self.assertEqual(remove_duplicates([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()


This test suite covers a variety of scenarios, including:

- Testing the function with different lists of integers
- Testing the function with an empty list
- Testing the function with a single-element list
- Testing the function with a list containing all duplicates
- Testing the function with a list containing no duplicates
- Testing the function with a list containing duplicates at the end
- Testing the function with a list containing duplicates in the middle
- Testing the function with a list containing duplicates at the start
- Testing the function with a list containing duplicates everywhere