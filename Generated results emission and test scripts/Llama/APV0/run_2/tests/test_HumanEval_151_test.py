user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_151_code import double_the_difference
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    return sum([i**2 for i in lst if i > 0 and i % 2!= 0 and "." not in str(i)])assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_151_code import double_the_difference

class TestDoubleTheDifference(unittest.TestCase):

    def test_double_the_difference(self):
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)
        self.assertEqual(double_the_difference([9, -2]), 81)
        self.assertEqual(double_the_difference([0]), 0)
        self.assertEqual(double_the_difference([]), 0)
        self.assertEqual(double_the_difference([1, 2, 3, 4, 5]), 50)
        self.assertEqual(double_the_difference([-1, -2, -3, -4, -5]), 0)
        self.assertEqual(double_the_difference([1.5, 2.5, 3.5, 4.5, 5.5]), 0)
        self.assertEqual(double_the_difference([1, 2, 3, 4, 5.5]), 30)

if __name__ == '__main__':
    unittest.main()


This script includes 8 test cases to cover different scenarios, including edge cases like an empty list, a list with only one element, and a list with both positive and negative numbers. The `assertEqual` method is used to compare the output of the function with the expected output.