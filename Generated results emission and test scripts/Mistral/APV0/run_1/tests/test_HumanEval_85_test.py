Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_85_code import add
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def add(lst):
    """Given a non-empty list of integers lst. Add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0])

 Here is a unittest test script for the provided function `add`:


import unittest
from HumanEval_85_code import add

class TestAddFunction(unittest.TestCase):

    def test_add_function(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)
        self.assertEqual(add([1, 2, 3, 4]), 2)
        self.assertEqual(add([0, 2, 4, 6]), 6)
        self.assertEqual(add([1, 3, 5, 7]), 0)
        self.assertEqual(add([-2, -4, -6]), 0)
        self.assertEqual(add([2, 4, 6, 8]), 6)
        self.assertEqual(add([10, 12, 14, 16]), 10)
        self.assertEqual(add([-10, -12, -14, -16]), 0)
        self.assertEqual(add([1, 3, 5, 7, 9]), 0)
        self.assertEqual(add([2, 4, 6, 8, 10]), 6)
        self.assertEqual(add([-2, -4, -6, -8]), 0)
        self.assertEqual(add([-1, -3, -5, -7]), 0)
        self.assertEqual(add([-2, -4, -6, -8, -10]), 0)
        self.assertEqual(add([1, 3, 5, 7, 9, 11]), 0)
        self.assertEqual(add([2, 4, 6, 8, 10, 12]), 6)
        self.assertEqual(add([-2, -4, -6, -8, -10, -12]), 0)

if __name__ == '__main__':
    unittest.main()


This test script includes multiple test cases to ensure the function works correctly for various input lists. You can run this script directly by saving it as a .py file and executing it using the command `python filename.py`.