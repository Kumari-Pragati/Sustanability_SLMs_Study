system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_142_code import sum_squares
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    result = []
    for i in range(len(lst)):
        if i % 3 == 0:
            result.append(lst[i] ** 2)
        elif i % 4 == 0 and i % 3!= 0:
            result.append(lst[i] ** 3)
        else:
            result.append(lst[i])
    return sum(result)assistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_142_code import sum_squares

class TestSumSquares(unittest.TestCase):

    def test_sum_squares_with_list(self):
        self.assertEqual(sum_squares([1,2,3]), 6)

    def test_sum_squares_with_empty_list(self):
        self.assertEqual(sum_squares([]), 0)

    def test_sum_squares_with_negative_numbers(self):
        self.assertEqual(sum_squares([-1,-5,2,-1,-5]), -126)

    def test_sum_squares_with_mixed_numbers(self):
        self.assertEqual(sum_squares([1,2,3,4,5]), 30)

    def test_sum_squares_with_single_element(self):
        self.assertEqual(sum_squares([1]), 1)

    def test_sum_squares_with_multiple_of_three(self):
        self.assertEqual(sum_squares([1,2,3,4,5,6,7,8,9]), 45)

    def test_sum_squares_with_multiple_of_four(self):
        self.assertEqual(sum_squares([1,2,3,4,5,6,7,8,9,10]), 55)

    def test_sum_squares_with_multiple_of_three_and_four(self):
        self.assertEqual(sum_squares([1,2,3,4,5,6,7,8,9,10,11,12]), 90)

if __name__ == '__main__':
    unittest.main()