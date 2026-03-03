user

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

    return ansassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_69_code import search

class TestSearchFunction(unittest.TestCase):

    def test_search_function(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)
        self.assertEqual(search([1, 1, 1, 1, 1]), 1)
        self.assertEqual(search([2, 2, 2, 2, 2]), 2)
        self.assertEqual(search([3, 3, 3, 3, 3]), -1)
        self.assertEqual(search([1, 2, 3, 4, 5]), -1)
        self.assertEqual(search([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), 2)

if __name__ == '__main__':
    unittest.main()


This script includes 8 test cases to cover different scenarios. The `assertEqual` method is used to compare the output of the `search` function with the expected output. If the output is not as expected, the test case will fail and an error message will be displayed.