You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the `max_element` function:


import unittest
from HumanEval_35_code import max_element

class TestMaxElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_element([]), None)

    def test_single_element(self):
        self.assertEqual(max_element([1]), 1)
        self.assertEqual(max_element([-1]), -1)

    def test_multiple_elements(self):
        self.assertEqual(max_element([1, 2, 3]), 3)
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)
        self.assertEqual(max_element([0, 0, 0]), 0)
        self.assertEqual(max_element([-100, -200, -300]), -100)

    def test_negative_numbers(self):
        self.assertEqual(max_element([-1, -2, -3]), -1)
        self.assertEqual(max_element([-5, -3, -2, -1]), -1)

    def test_all_negative_numbers(self):
        self.assertEqual(max_element([-5, -3, -2, -1]), -1)
        self.assertEqual(max_element([-100, -200, -300]), -100)

    def test_all_zeros(self):
        self.assertEqual(max_element([0, 0, 0]), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios such as an empty list, single element, multiple elements, negative numbers, all negative numbers, and all zeros. It uses the `assertEqual` method to compare the expected output with the actual output returned by the `max_element` function.