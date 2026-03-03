You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_133_code import sum_squares

class TestSumSquares(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(sum_squares([1,2,3]), 14)
        self.assertEqual(sum_squares([1,4,9]), 98)
        self.assertEqual(sum_squares([1,3,5,7]), 84)

    def test_decimal_numbers(self):
        self.assertEqual(sum_squares([1.4,4.2,0]), 29)

    def test_negative_numbers(self):
        self.assertEqual(sum_squares([-2.4,1,1]), 6)

    def test_empty_list(self):
        self.assertEqual(sum_squares([]), 0)

    def test_single_number(self):
        self.assertEqual(sum_squares([5]), 30)

    def test_large_numbers(self):
        self.assertEqual(sum_squares([100, 200, 300]), 130300)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different types of inputs, including positive numbers, decimal numbers, negative numbers, an empty list, a list with a single number, and a list with large numbers. The `assertEqual` method is used to check if the output of the `sum_squares` function matches the expected output.