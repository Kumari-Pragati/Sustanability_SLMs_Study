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

 import unittest
from HumanEval_26_code import remove_duplicates
from typing import List

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates(self):
        # Test with a list containing duplicates
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

        # Test with a list containing no duplicates
        self.assertEqual(remove_duplicates([1, 2, 3, 4]), [1, 2, 3, 4])

        # Test with a list containing all duplicates
        self.assertEqual(remove_duplicates([1, 1, 1, 1]), [])

        # Test with an empty list
        self.assertEqual(remove_duplicates([]), [])

        # Test with a list containing a single element
        self.assertEqual(remove_duplicates([5]), [5])

        # Test with a list containing negative numbers
        self.assertEqual(remove_duplicates([-1, -2, -3, -2, -1]), [-3])

        # Test with a list containing floating-point numbers
        self.assertEqual(remove_duplicates([1.0, 2.0, 3.0, 2.0, 4.0]), [1.0, 3.0, 4.0])

        # Test with a list containing mixed types
        with self.assertRaises(TypeError):
            remove_duplicates([1, "2", 3.0, 3])

if __name__ == '__main__':
    unittest.main()