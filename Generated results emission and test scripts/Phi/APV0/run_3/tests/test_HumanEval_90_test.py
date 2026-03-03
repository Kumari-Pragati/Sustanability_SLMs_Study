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

 import unittest
from HumanEval_90_code import next_smallest

class TestNextSmallest(unittest.TestCase):

    def test_next_smallest_with_unique_elements(self):
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 2)

    def test_next_smallest_with_no_second_smallest(self):
        self.assertIsNone(next_smallest([1]))
        self.assertIsNone(next_smallest([1, 1]))

    def test_next_smallest_with_empty_list(self):
        self.assertIsNone(next_smallest([]))

    def test_next_smallest_with_all_same_elements(self):
        self.assertIsNone(next_smallest([1, 1, 1, 1, 1]))

    def test_next_smallest_with_negative_numbers(self):
        self.assertEqual(next_smallest([-3, -1, -2, -4, -5]), -2)
        self.assertEqual(next_smallest([-5, -1, -4, -3, -2]), -2)

if __name__ == '__main__':
    unittest.main()