user

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
    return massistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_35_code import max_element

class TestMaxElement(unittest.TestCase):

    def test_max_element(self):
        self.assertEqual(max_element([1, 2, 3]), 3)
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)
        self.assertEqual(max_element([-1, -2, -3]), -1)
        self.assertEqual(max_element([1]), 1)
        self.assertEqual(max_element([-1, 0, 1]), 1)
        self.assertEqual(max_element([1, 1, 1]), 1)
        self.assertEqual(max_element([-1, -1, -1]), -1)
        self.assertEqual(max_element([]), None)  # Edge case: empty list

    def test_max_element_edge_cases(self):
        with self.assertRaises(IndexError):
            max_element([])  # Edge case: empty list
        with self.assertRaises(TypeError):
            max_element("Hello")  # Edge case: non-list input

if __name__ == '__main__':
    unittest.main()


This script includes two test methods: `test_max_element` and `test_max_element_edge_cases`. The `test_max_element` method tests the function with various inputs, including edge cases. The `test_max_element_edge_cases` method tests the function with edge cases, such as an empty list and a non-list input.