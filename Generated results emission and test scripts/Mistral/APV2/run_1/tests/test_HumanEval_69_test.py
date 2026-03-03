You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is a complete unittest test suite for the provided `search` function:


import unittest
from HumanEval_69_code import search

class TestSearchFunction(unittest.TestCase):

    def test_search_with_examples(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)

    def test_empty_list(self):
        self.assertEqual(search([]), -1)

    def test_list_with_only_one_element(self):
        self.assertEqual(search([1]), -1)

    def test_list_with_only_one_element_greater_than_zero(self):
        self.assertEqual(search([2]), 2)

    def test_list_with_multiple_elements_equal_to_one(self):
        self.assertEqual(search([1, 1, 1]), -1)

    def test_list_with_multiple_elements_equal_to_one_and_one_greater(self):
        self.assertEqual(search([1, 1, 2]), 2)

    def test_list_with_multiple_elements_equal_to_one_and_one_greater_and_one_less(self):
        self.assertEqual(search([1, 1, 2, 0]), 2)

    def test_list_with_multiple_elements_greater_than_one(self):
        self.assertEqual(search([2, 2, 3, 3, 3]), 3)

    def test_list_with_multiple_elements_greater_than_one_and_one_less(self):
        self.assertEqual(search([2, 2, 3, 2, 3]), 3)

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to cover different scenarios, such as empty lists, lists with only one element, lists with multiple elements equal to one, lists with multiple elements greater than one, and lists with multiple elements greater than one and one less. It also tests the edge case where the greatest integer is less than one.