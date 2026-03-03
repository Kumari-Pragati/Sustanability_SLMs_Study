Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_90_code import next_smallest
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """

    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]

 Here is a unittest test script for the `next_smallest` function:


import unittest
from HumanEval_90_code import next_smallest

class TestNextSmallest(unittest.TestCase):
    def test_next_smallest(self):
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 2)
        self.assertEqual(next_smallest([]), None)
        self.assertEqual(next_smallest([1, 1]), None)
        self.assertEqual(next_smallest([-1, -2, -3, -4, -5]), -2)
        self.assertEqual(next_smallest([0, 0, 1]), 0)
        self.assertEqual(next_smallest([10, 10, 11]), 10)
        self.assertEqual(next_smallest([5, 3, 2, 1]), 2)
        self.assertEqual(next_smallest([2, 2]), None)
        self.assertEqual(next_smallest([1, 2, 2]), 1)

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to ensure the function works correctly for various inputs. The test cases cover the edge cases where the list is empty, contains duplicates, or has only one unique element. The test cases also cover the case where the list contains multiple instances of the same smallest element.