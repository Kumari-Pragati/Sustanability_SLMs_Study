You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is a complete unittest test suite for the given function:


import unittest
from HumanEval_146_code import specialFilter

class TestSpecialFilter(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)

    def test_negative_numbers(self):
        self.assertEqual(specialFilter([-15, -73, -14, -35]), 0)
        self.assertEqual(specialFilter([-33, -2, -3, -45, -21, -109]), 0)

    def test_zero(self):
        self.assertEqual(specialFilter([0, 0, 0, 0]), 0)

    def test_single_digit_numbers(self):
        self.assertEqual(specialFilter([1, 3, 5, 7, 9]), 1)
        self.assertEqual(specialFilter([2, 4, 6, 8, 0]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(specialFilter([15, -73, 14, -15, 0, 3, 5, 7, 9]), 2)
        self.assertEqual(specialFilter([-33, -2, -3, -45, -21, -109, 2, 4, 6, 8, 0]), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios: positive numbers, negative numbers, zero, single-digit numbers, and mixed numbers. It checks if the function returns the correct count of numbers that are greater than 10 and have both first and last digits as odd numbers.