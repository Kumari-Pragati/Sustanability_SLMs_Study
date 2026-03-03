You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function `next_smallest`.


import unittest
from HumanEval_90_code import next_smallest

class TestNextSmallest(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(next_smallest([]), None)

    def test_single_element_list(self):
        self.assertEqual(next_smallest([1]), None)
        self.assertEqual(next_smallest([5]), None)

    def test_list_with_one_unique_element(self):
        self.assertEqual(next_smallest([1]), None)
        self.assertEqual(next_smallest([5]), None)

    def test_list_with_duplicates(self):
        self.assertEqual(next_smallest([1, 1]), None)
        self.assertEqual(next_smallest([5, 5]), None)

    def test_list_with_multiple_elements(self):
        self.assertEqual(next_smallest([1, 2, 3, 4, 5]), 2)
        self.assertEqual(next_smallest([5, 1, 4, 3, 2]), 3)
        self.assertEqual(next_smallest([10, 2, 3, 4, 5, 6]), 3)
        self.assertEqual(next_smallest([10, 2, 3, 4, 5, 6, 7]), 4)

if __name__ == '__main__':
    unittest.main()


This test suite covers various edge cases and different scenarios of the input list. It tests the function's behavior when the input list is empty, contains a single element, has duplicates, and has multiple elements.