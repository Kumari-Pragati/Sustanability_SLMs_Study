Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_135_code import can_arrange
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    ind = -1
    i = 1
    while i < len(arr):
        if arr[i] < arr[i - 1]:
            ind = i
        i += 1
    return ind

 Here is a unittest test script for the `can_arrange` function:


import unittest
from HumanEval_135_code import can_arrange

class TestCanArrange(unittest.TestCase):

    def test_can_arrange(self):
        self.assertEqual(can_arrange([1, 2, 4, 3, 5]), 3)
        self.assertEqual(can_arrange([1, 2, 3]), -1)
        self.assertEqual(can_arrange([6, 3, 2, 1]), -1)
        self.assertEqual(can_arrange([5, 4, 3, 2, 1]), 4)
        self.assertEqual(can_arrange([10, 9, 8, 7, 6]), -1)

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the examples provided in the function documentation, as well as a few additional test cases to ensure the function works correctly for a variety of input arrays. You can run this script directly by saving it as a .py file and running it using the command `python filename.py`.