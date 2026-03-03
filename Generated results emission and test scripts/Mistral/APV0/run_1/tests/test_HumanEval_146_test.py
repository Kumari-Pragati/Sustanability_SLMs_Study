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

 Here is a unittest test script for the `specialFilter` function:


import unittest
from HumanEval_146_code import specialFilter

class TestSpecialFilter(unittest.TestCase):
    def test_special_filter(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)
        self.assertEqual(specialFilter([11, 13, 15, 17, 19]), 4)
        self.assertEqual(specialFilter([10, 11, 13, 15, 17]), 2)
        self.assertEqual(specialFilter([2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 0)
        self.assertEqual(specialFilter([]), 0)
        self.assertEqual(specialFilter([100, 101, 103, 105, 107]), 5)
        self.assertEqual(specialFilter([1000, 1001, 1003, 1005, 1007]), 5)
        self.assertEqual(specialFilter([1010, 1011, 1013, 1015, 1017]), 1)

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to ensure the function works correctly for various inputs. The test cases cover different scenarios such as empty lists, lists with numbers less than 10, lists with numbers greater than 1000, and lists with numbers that have odd digits at the beginning and end.