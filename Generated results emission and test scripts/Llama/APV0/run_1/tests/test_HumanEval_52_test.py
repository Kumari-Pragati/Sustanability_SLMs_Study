user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return Trueassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_52_code import below_threshold

class TestBelowThreshold(unittest.TestCase):

    def test_below_threshold(self):
        self.assertTrue(below_threshold([1, 2, 4, 10], 100))
        self.assertFalse(below_threshold([1, 20, 4, 10], 5))
        self.assertTrue(below_threshold([1, 2, 3, 4], 5))
        self.assertFalse(below_threshold([1, 2, 3, 4, 5], 5))
        self.assertTrue(below_threshold([], 100))
        self.assertFalse(below_threshold([100], 100))
        self.assertFalse(below_threshold([100, 200, 300], 100))

    def test_empty_list(self):
        self.assertTrue(below_threshold([], 100))

    def test_single_element_list(self):
        self.assertTrue(below_threshold([1], 100))
        self.assertFalse(below_threshold([100], 100))

if __name__ == '__main__':
    unittest.main()


This script includes four test cases:

1. `test_below_threshold`: This test case checks the function with different inputs and expected outputs.
2. `test_empty_list`: This test case checks the function with an empty list as input.
3. `test_single_element_list`: This test case checks the function with a list containing a single element as input.

The `unittest.main()` function is used to run the test cases.