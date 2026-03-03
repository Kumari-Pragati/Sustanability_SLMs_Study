You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is a complete unittest test suite for the `double_the_difference` function:


import unittest
from HumanEval_151_code import double_the_difference

class TestDoubleTheDifference(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(double_the_difference([]), 0)

    def test_positive_odd_numbers(self):
        self.assertEqual(double_the_difference([1, 3, 5]), 36)
        self.assertEqual(double_the_difference([1, 3, 5, 7]), 100)

    def test_negative_odd_numbers(self):
        self.assertEqual(double_the_difference([-1, -3, -5]), 0)
        self.assertEqual(double_the_difference([-1, -3, -5, -7]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(double_the_difference([1, -3, 5, -7, 0]), 36)
        self.assertEqual(double_the_difference([0, -3, 5, -7]), 0)

    def test_floats(self):
        self.assertEqual(double_the_difference([1.5, -3.2, 5.0, -7.1]), 0)
        self.assertEqual(double_the_difference([1.5, -3.2, 5.0]), 9)

    def test_single_number(self):
        self.assertEqual(double_the_difference([0]), 0)
        self.assertEqual(double_the_difference([1]), 1)
        self.assertEqual(double_the_difference([3]), 9)

    def test_large_list(self):
        self.assertEqual(double_the_difference([1, 3, 5, 7, 9, 11, 13, 15]), 385)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios such as empty lists, positive odd numbers, negative odd numbers, mixed numbers, floats, single numbers, and large lists. It uses the `assertEqual` method to compare the expected output with the actual output of the `double_the_difference` function.