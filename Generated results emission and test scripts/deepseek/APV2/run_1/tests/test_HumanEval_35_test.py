You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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
    return m


### Response:
Here is a complete unittest test suite for the given function:


import unittest
from HumanEval_35_code import max_element

class TestMaxElement(unittest.TestCase):

    def test_max_element(self):
        self.assertEqual(max_element([1, 2, 3]), 3)
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)
        self.assertEqual(max_element([-1, -2, -3]), -1)
        self.assertEqual(max_element([1]), 1)
        self.assertEqual(max_element([0, 0, 0]), 0)
        self.assertEqual(max_element([]), None)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

1. A list with positive numbers.
2. A list with both positive and negative numbers.
3. A list with only negative numbers.
4. A list with a single element.
5. A list with all zeros.
6. An empty list.

The function `max_element` is expected to return `None` for an empty list, which is why there's a test for that case.

Please note that the function `max_element` is expected to return `None` for an empty list, so the test for an empty list is included.

Also, please note that the function `max_element` is expected to return the first maximum element it finds in case of multiple maximum elements. If the function is expected to return all maximum elements, the test suite would need to be adjusted accordingly.