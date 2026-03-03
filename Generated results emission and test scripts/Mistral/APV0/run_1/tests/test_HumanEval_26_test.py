Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `remove_duplicates` function:


import unittest
from HumanEval_26_code import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])
        self.assertEqual(remove_duplicates([1, 1, 2, 3, 2, 4]), [1, 2, 3, 4])
        self.assertEqual(remove_duplicates([]), [])
        self.assertEqual(remove_duplicates([1]), [1])
        self.assertEqual(remove_duplicates([1, 1]), [1])
        self.assertEqual(remove_duplicates([1, 1, 1]), [1])
        self.assertEqual(remove_duplicates([1, 1, 1, 1]), [1])
        self.assertEqual(remove_duplicates([1, 1, 1, 1, 1]), [1])
        self.assertEqual(remove_duplicates([1, 1, 1, 1, 1, 1]), [1])
        self.assertEqual(remove_duplicates([10, 20, 10, 20, 30]), [10, 20, 30])
        self.assertEqual(remove_duplicates([10, 20, 10, 20, 30, 30]), [10, 20, 30])
        self.assertEqual(remove_duplicates([10, 20, 10, 20, 30, 30, 30]), [10, 20, 30])

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the `remove_duplicates` function with various input examples, including edge cases and multiple occurrences of the same number. The test script can be run directly using the command `python test_remove_duplicates.py`.