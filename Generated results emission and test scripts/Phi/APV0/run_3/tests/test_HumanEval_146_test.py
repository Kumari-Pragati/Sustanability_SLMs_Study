Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_146_code import specialFilter
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            odd_digits = (1, 3, 5, 7, 9)
            number_as_string = str(num)
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                count += 1
    return count

 import unittest
from HumanEval_146_code import specialFilter

class TestSpecialFilter(unittest.TestCase):

    def test_specialFilter_with_positive_numbers(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)

    def test_specialFilter_with_negative_numbers(self):
        self.assertEqual(specialFilter([-33, -2, -3, 45, 21, 109]), 2)

    def test_specialFilter_with_numbers_less_than_10(self):
        self.assertEqual(specialFilter([9, 8, 7, 6, 5]), 0)

    def test_specialFilter_with_no_qualifying_numbers(self):
        self.assertEqual(specialFilter([10, 20, 30, 40]), 0)

    def test_specialFilter_with_single_qualifying_number(self):
        self.assertEqual(specialFilter([31]), 1)

    def test_specialFilter_with_multiple_qualifying_numbers(self):
        self.assertEqual(specialFilter([33, 57, 11, 79, 13]), 4)

    def test_specialFilter_with_no_odd_digits(self):
        self.assertEqual(specialFilter([21, 23, 25]), 0)

    def test_specialFilter_with_all_odd_digits(self):
        self.assertEqual(specialFilter([11, 33, 55, 77, 99]), 5)

if __name__ == '__main__':
    unittest.main()