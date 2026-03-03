Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 import unittest
from HumanEval_142_code import sum_squares

class TestSumSquares(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_squares([]), 0)

    def test_single_element_list(self):
        self.assertEqual(sum_squares([1]), 1)

    def test_list_with_index_multiple_of_3(self):
        self.assertEqual(sum_squares([1, 2, 3]), 6)

    def test_list_with_index_multiple_of_4_but_not_3(self):
        self.assertEqual(sum_squares([1, 2, 3, 4]), 77)

    def test_list_with_index_multiple_of_3_and_4(self):
        self.assertEqual(sum_squares([1, 2, 3, 4, 5, 6]), 99)

    def test_list_with_index_not_multiple_of_3_or_4(self):
        self.assertEqual(sum_squares([1, 2, 3, 5, 6]), 29)

    def test_list_with_negative_numbers(self):
        self.assertEqual(sum_squares([-1, -2, -3]), -14)

    def test_list_with_mixed_numbers(self):
        self.assertEqual(sum_squares([-1, -2, 3, 4, -5, 6]), -126)

if __name__ == '__main__':
    unittest.main()