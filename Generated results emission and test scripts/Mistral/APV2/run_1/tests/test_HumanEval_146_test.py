You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is a complete unittest test suite for the `specialFilter` function:


import unittest
from HumanEval_146_code import specialFilter

class TestSpecialFilter(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(specialFilter([]), 0)

    def test_single_number(self):
        self.assertEqual(specialFilter([11]), 0)
        self.assertEqual(specialFilter([11]), 0)
        self.assertEqual(specialFilter([1]), 0)
        self.assertEqual(specialFilter([10]), 0)
        self.assertEqual(specialFilter([111]), 0)
        self.assertEqual(specialFilter([101]), 1)

    def test_multiple_numbers(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)
        self.assertEqual(specialFilter([101, 103, 105, 107, 109]), 5)
        self.assertEqual(specialFilter([1111, 1333, 1555, 1777, 1999]), 5)
        self.assertEqual(specialFilter([2111, 2333, 2555, 2777, 2999]), 0)
        self.assertEqual(specialFilter([-1111, -1333, -1555, -1777, -1999]), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for an empty list, single numbers, and multiple numbers. It covers various edge cases, such as negative numbers and numbers with odd digits that are not in the range 1-9. The test suite uses the `unittest.TestCase.assertEqual` method to verify the expected output of the `specialFilter` function.