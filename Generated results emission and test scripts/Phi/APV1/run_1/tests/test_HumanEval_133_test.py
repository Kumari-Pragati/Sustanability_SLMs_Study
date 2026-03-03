You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 import unittest
from HumanEval_133_code import sum_squares

class TestSumSquares(unittest.TestCase):

    def test_sum_squares_with_integers(self):
        self.assertEqual(sum_squares([1, 2, 3]), 14)
        self.assertEqual(sum_squares([1, 4, 9]), 98)
        self.assertEqual(sum_squares([1, 3, 5, 7]), 84)

    def test_sum_squares_with_floats(self):
        self.assertEqual(sum_squares([1.4, 4.2, 0]), 29)

    def test_sum_squares_with_mixed_types(self):
        self.assertEqual(sum_squares([-2.4, 1, 1]), 6)

    def test_sum_squares_with_empty_list(self):
        self.assertEqual(sum_squares([]), 0)

    def test_sum_squares_with_single_element(self):
        self.assertEqual(sum_squares([5]), 25)

    def test_sum_squares_with_negative_numbers(self):
        self.assertEqual(sum_squares([-2, -3, -4]), 29)

    def test_sum_squares_with_zero(self):
        self.assertEqual(sum_squares([0]), 0)

if __name__ == '__main__':
    unittest.main()