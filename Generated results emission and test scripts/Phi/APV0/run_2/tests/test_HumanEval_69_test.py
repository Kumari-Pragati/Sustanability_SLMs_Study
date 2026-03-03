Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 import unittest
from HumanEval_69_code import search

class TestSearchFunction(unittest.TestCase):

    def test_search_with_positive_integers(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)

    def test_search_with_empty_list(self):
        self.assertEqual(search([]), -1)

    def test_search_with_single_element(self):
        self.assertEqual(search([1]), 1)

    def test_search_with_all_unique_elements(self):
        self.assertEqual(search([1, 2, 3, 4]), -1)

    def test_search_with_all_same_elements(self):
        self.assertEqual(search([5, 5, 5, 5]), -1)

    def test_search_with_no_greater_frequency(self):
        self.assertEqual(search([1, 2, 3, 4, 5]), -1)

    def test_search_with_negative_integers(self):
        with self.assertRaises(ValueError):
            search([-1, -2, -3])

if __name__ == '__main__':
    unittest.main()