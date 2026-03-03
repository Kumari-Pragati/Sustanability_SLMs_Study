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
    return sum([i**2 for i in lst if i > 0 and i % 2 != 0 and "." not in str(i)])

 Here is a unittest test script for the `double_the_difference` function:


import unittest
from HumanEval_151_code import double_the_difference

class TestDoubleTheDifference(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(double_the_difference([]), 0)

    def test_positive_odd_numbers(self):
        self.assertEqual(double_the_difference([1, 3, 5]), 34)
        self.assertEqual(double_the_difference([1, 3, 5, 7]), 158)

    def test_negative_odd_numbers(self):
        self.assertEqual(double_the_difference([-1, -3, -5]), 0)
        self.assertEqual(double_the_difference([-1, -3, -5, -7]), 0)

    def test_zero(self):
        self.assertEqual(double_the_difference([0]), 0)
        self.assertEqual(double_the_difference([0, 0]), 0)

    def test_floats(self):
        self.assertEqual(double_the_difference([1.5, 3.5]), 0)
        self.assertEqual(double_the_difference([1.5, 3.5, 5.5]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(double_the_difference([1, -3.5, 5]), 34)
        self.assertEqual(double_the_difference([1, -3.5, 5, 0.5]), 34.25)

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as an empty list, positive odd numbers, negative odd numbers, zero, floats, and mixed numbers. It uses the `unittest.TestCase.assertEqual` method to verify the expected output of the `double_the_difference` function.