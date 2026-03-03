You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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
        elif i % 4 == 0 and i % 3 != 0:
            result.append(lst[i] ** 3)
        else:
            result.append(lst[i])
    return sum(result)

 Here is the complete unittest test suite for the `sum_squares` function:


import unittest
from HumanEval_142_code import sum_squares

class TestSumSquares(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_squares([]), 0)

    def test_simple_list(self):
        self.assertEqual(sum_squares([1, 2, 3]), 6)

    def test_list_with_multiples_of_3(self):
        self.assertEqual(sum_squares([1, 4, 9, 2, 3]), 34)

    def test_list_with_multiples_of_4_not_3(self):
        self.assertEqual(sum_squares([1, -8, 27, -1, -5]), -126)

    def test_list_with_negative_numbers(self):
        self.assertEqual(sum_squares([-1, -2, -3]), 30)

    def test_list_with_zero(self):
        self.assertEqual(sum_squares([0, 1, 4, 3, 0]), 25)

if __name__ == '__main__':
    unittest.main()


This test suite includes six test cases that cover various scenarios, such as an empty list, simple lists, lists with multiples of 3, lists with multiples of 4 not multiples of 3, lists with negative numbers, and lists with zero. The test suite uses the `unittest.TestCase` class to define test methods and the `unittest.main()` function to run the tests.