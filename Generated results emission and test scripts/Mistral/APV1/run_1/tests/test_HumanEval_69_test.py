You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_69_code import search

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such value exists, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    frq = [0] * (max(lst) + 1)
    for i in lst:
        frq[i] += 1

    ans = -1
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i

    return ans

 Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_69_code import search

class TestSearchFunction(unittest.TestCase):

    def test_search_simple_list(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)

    def test_search_list_with_multiple_occurrences(self):
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)

    def test_search_list_with_only_one_occurrence(self):
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)

    def test_search_empty_list(self):
        self.assertEqual(search([]), -1)

    def test_search_list_with_only_zero(self):
        self.assertEqual(search([0]), -1)

    def test_search_list_with_only_negative_numbers(self):
        self.assertEqual(search([-1, -2, -3]), -1)

    def test_search_list_with_duplicate_zero(self):
        self.assertEqual(search([0, 0, 1]), -1)

    def test_search_list_with_large_numbers(self):
        self.assertEqual(search([100, 100, 99, 99, 99]), 100)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios such as simple lists, lists with multiple occurrences, lists with only one occurrence, empty lists, lists with only zero, lists with only negative numbers, lists with duplicate zero, and lists with large numbers.