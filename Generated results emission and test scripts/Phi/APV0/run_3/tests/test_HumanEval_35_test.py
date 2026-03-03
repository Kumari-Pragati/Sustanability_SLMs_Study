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

 import unittest
from HumanEval_35_code import max_element

class TestMaxElement(unittest.TestCase):

    def test_max_element_positive_numbers(self):
        self.assertEqual(max_element([1, 2, 3]), 3)

    def test_max_element_negative_numbers(self):
        self.assertEqual(max_element([-5, -3, -10]), -3)

    def test_max_element_mixed_numbers(self):
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

    def test_max_element_empty_list(self):
        with self.assertRaises(IndexError):
            max_element([])

    def test_max_element_single_element_list(self):
        self.assertEqual(max_element([1]), 1)

    def test_max_element_all_elements_same(self):
        self.assertEqual(max_element([5, 5, 5, 5]), 5)

    def test_max_element_all_elements_negative(self):
        self.assertEqual(max_element([-10, -10, -10, -10]), -10)

if __name__ == '__main__':
    unittest.main()