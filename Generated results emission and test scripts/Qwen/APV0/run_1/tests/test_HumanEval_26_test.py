system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Importing the function to be tested
from HumanEval_26_code import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):
    
    def test_remove_duplicates(self):
        # Test case 1: Basic usage
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4], "Test Case 1 Failed")
        
        # Test case 2: Single element list
        self.assertEqual(remove_duplicates([5]), [5], "Test Case 2 Failed")
        
        # Test case 3: Empty list
        self.assertEqual(remove_duplicates([]), [], "Test Case 3 Failed")
        
        # Test case 4: Duplicate elements only
        self.assertEqual(remove_duplicates([1, 1, 1, 1]), [1], "Test Case 4 Failed")
        
        # Test case 5: Mixed duplicates and unique elements
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Test Case 5 Failed")

if __name__ == '__main__':
    unittest.main()


This script imports the `remove_duplicates` function and defines several test cases using the `assertEqual` method to verify its correctness against expected outcomes. The `unittest.main()` call at the end makes the tests executable when run directly.