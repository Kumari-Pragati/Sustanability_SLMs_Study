Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_35_code import max_element
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m

 Here is a unittest test script for the `max_element` function:


import unittest
from HumanEval_35_code import max_element

class TestMaxElement(unittest.TestCase):
    def test_max_element(self):
        self.assertEqual(max_element([1, 2, 3]), 3)
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)
        self.assertEqual(max_element([-5, -3, -2, -1]), -1)
        self.assertEqual(max_element([0]), 0)
        self.assertEqual(max_element([]), None)
        self.assertEqual(max_element([-5]), -5)
        self.assertEqual(max_element([5]), 5)
        self.assertEqual(max_element([-5, 5]), 5)
        self.assertEqual(max_element([5, -5]), 5)
        self.assertEqual(max_element([-5, -5]), -5)
        self.assertEqual(max_element([-5, -5, -5]), -5)
        self.assertEqual(max_element([5, 5, 5]), 5)
        self.assertEqual(max_element([5, 5, 5, 5]), 5)

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases to ensure the function works correctly for different input lists, including empty lists, lists with negative numbers, and lists with duplicates. It also tests the edge cases where the list contains only one element or no elements.