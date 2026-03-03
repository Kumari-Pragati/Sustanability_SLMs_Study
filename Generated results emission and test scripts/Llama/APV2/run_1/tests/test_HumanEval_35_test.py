system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_35_code import max_element

class TestMaxElement(unittest.TestCase):

    def test_max_element(self):
        self.assertEqual(max_element([1, 2, 3]), 3)
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)
        self.assertEqual(max_element([-10, -5, -3, -2, -1]), -1)
        self.assertEqual(max_element([1]), 1)
        self.assertEqual(max_element([-1]), -1)
        self.assertEqual(max_element([1, 1, 1, 1, 1]), 1)
        self.assertEqual(max_element([-1, -1, -1, -1, -1]), -1)
        self.assertEqual(max_element([0, 0, 0, 0, 0]), 0)
        self.assertEqual(max_element([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_element([-1, -2, -3, -4, -5]), -5)

if __name__ == '__main__':
    unittest.main()