user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_133_code import sum_squares
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    """
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i) ** 2
    return squaredassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_133_code import sum_squares

class TestSumSquares(unittest.TestCase):

    def test_sum_squares(self):
        self.assertEqual(sum_squares([1,2,3]), 14)
        self.assertEqual(sum_squares([1,4,9]), 98)
        self.assertEqual(sum_squares([1,3,5,7]), 84)
        self.assertEqual(sum_squares([1.4,4.2,0]), 29)
        self.assertEqual(sum_squares([-2.4,1,1]), 6)

    def test_sum_squares_negative(self):
        self.assertEqual(sum_squares([-1,2,3]), 14)
        self.assertEqual(sum_squares([-1,4,9]), 98)
        self.assertEqual(sum_squares([-1,3,5,7]), 84)
        self.assertEqual(sum_squares([-1.4,4.2,0]), 29)
        self.assertEqual(sum_squares([-2.4,1,1]), 6)

    def test_sum_squares_zero(self):
        self.assertEqual(sum_squares([0,0,0]), 0)
        self.assertEqual(sum_squares([0,1,0]), 1)
        self.assertEqual(sum_squares([0,1,2]), 5)

if __name__ == '__main__':
    unittest.main()


This script includes three test cases: `test_sum_squares`, `test_sum_squares_negative`, and `test_sum_squares_zero`. Each test case checks the function with different inputs to ensure it works correctly.