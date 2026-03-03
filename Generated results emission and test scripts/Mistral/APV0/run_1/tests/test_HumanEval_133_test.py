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
    return squared

 Here is a unittest test script for the `sum_squares` function:


import unittest
from HumanEval_133_code import sum_squares

class TestSumSquares(unittest.TestCase):

    def test_sum_squares(self):
        self.assertEqual(sum_squares([1, 2, 3]), 14)
        self.assertEqual(sum_squares([1, 4, 9]), 98)
        self.assertEqual(sum_squares([1, 3, 5, 7]), 84)
        self.assertEqual(sum_squares([1.4, 4.2, 0]), 29)
        self.assertEqual(sum_squares([-2.4, 1, 1]), 6)
        self.assertEqual(sum_squares([-2.4, -1.1, 1]), 14)
        self.assertEqual(sum_squares([0, 0, 0]), 0)
        self.assertEqual(sum_squares([-0.5, 0, 0.5]), 1)
        self.assertEqual(sum_squares([math.pi, math.e, 0]), int(math.pi ** 2 + math.e ** 2))

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the given examples and some additional test cases to ensure the function works correctly with negative numbers, floating-point numbers, and the special cases of all zeros and numbers close to zero. The test case for the special case of all zeros uses the `assertEqual` function to check that the function returns 0, and the test case for numbers close to zero uses the `math.pi` and `math.e` constants to create a test case where the function needs to round the numbers to the nearest integer before squaring them.