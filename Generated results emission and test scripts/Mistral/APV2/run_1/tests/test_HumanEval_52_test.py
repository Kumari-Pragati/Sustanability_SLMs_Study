You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_52_code import below_threshold
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for e in l:
        if e >= t:
            return False
    return True

 Here is a complete unittest test suite for the `below_threshold` function:


import unittest
from HumanEval_52_code import below_threshold

class TestBelowThreshold(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(below_threshold([], 100))

    def test_single_element(self):
        self.assertTrue(below_threshold([1], 2))
        self.assertFalse(below_threshold([101], 100))

    def test_multiple_elements(self):
        self.assertTrue(below_threshold([1, 2, 4, 10], 100))
        self.assertFalse(below_threshold([1, 20, 4, 10], 5))
        self.assertFalse(below_threshold([10, 20, 40, 100], 5))

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. An empty list should return True for any threshold.
2. A single element list should return True if the element is below the threshold and False if it's above.
3. A list with multiple elements should return True if all elements are below the threshold and False if any element is above.

Each test case is a method within the `TestBelowThreshold` class, and the test suite is run using `unittest.main()`.