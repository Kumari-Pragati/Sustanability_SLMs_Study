You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_69_code import search

class TestSearch(unittest.TestCase):

    def test_search(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)
        self.assertEqual(search([1, 1, 1, 1, 1]), 1)
        self.assertEqual(search([1, 2, 3, 4, 5]), -1)
        self.assertEqual(search([1]), 1)
        self.assertEqual(search([]), -1)
        self.assertEqual(search([1, 1, 2, 2, 3, 3]), 2)
        self.assertEqual(search([1, 1, 1, 2, 2, 2]), 1)
        self.assertEqual(search([1, 1, 1, 1, 2, 2]), -1)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various edge cases and common scenarios. It checks the function's behavior with lists of different lengths and with numbers that appear more or less frequently.