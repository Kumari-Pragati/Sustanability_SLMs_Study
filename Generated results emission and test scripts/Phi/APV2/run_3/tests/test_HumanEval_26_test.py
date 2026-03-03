You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

 
import unittest
from HumanEval_26_code import remove_duplicates
from typing import List

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates(self):
        # Test case 1: Basic functionality
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

        # Test case 2: Empty list
        self.assertEqual(remove_duplicates([]), [])

        # Test case 3: List with all unique elements
        self.assertEqual(remove_duplicates([5, 6, 7, 8]), [5, 6, 7, 8])

        # Test case 4: List with all elements being duplicates
        self.assertEqual(remove_duplicates([2, 2, 2, 2]), [])

        # Test case 5: List with one element
        self.assertEqual(remove_duplicates([9]), [9])

        # Test case 6: List with negative numbers
        self.assertEqual(remove_duplicates([-1, -2, -3, -2, -1]), [-1, -3])

        # Test case 7: List with mixed types
        with self.assertRaises(TypeError):
            remove_duplicates([1, "2", 3, "3"])

        # Test case 8: List with floating-point numbers
        self.assertEqual(remove_duplicates([1.1, 2.2, 3.3, 2.2]), [1.1, 3.3])

        # Test case 9: List with None values
        with self.assertRaises(TypeError):
            remove_duplicates([None, 1, None, 2])

        # Test case 10: List with complex numbers
        with self.assertRaises(TypeError):
            remove_duplicates([1+2j, 2+3j, 1+2j])

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios to ensure that the `remove_duplicates` function behaves as expected. It includes tests for basic functionality, edge cases (empty list, all unique elements, all duplicates), and error handling (mixed types, None values, complex numbers). The `assertRaises` method is used to check that the function raises a `TypeError` when encountering inappropriate input types.