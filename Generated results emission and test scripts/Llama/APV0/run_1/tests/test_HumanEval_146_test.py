user

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
    return countassistant

Here is the unittest test script for the `specialFilter` function:

import unittest
from HumanEval_146_code import specialFilter

class TestSpecialFilter(unittest.TestCase):
    def test_special_filter(self):
        # Test case 1: single element array
        self.assertEqual(specialFilter([15]), 1)

        # Test case 2: multiple elements array
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)

        # Test case 3: multiple elements array with multiple matches
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)

        # Test case 4: empty array
        self.assertEqual(specialFilter([]), 0)

        # Test case 5: array with no numbers greater than 10
        self.assertEqual(specialFilter([-10, -5, 0, 5]), 0)

        # Test case 6: array with numbers that are not odd in first or last digit
        self.assertEqual(specialFilter([12, 24, 36, 48]), 0)

        # Test case 7: array with numbers that are not greater than 10
        self.assertEqual(specialFilter([-1, 0, 1, 2, 3]), 0)

if __name__ == '__main__':
    unittest.main()

This script defines a `TestSpecialFilter` class that contains seven test cases for the `specialFilter` function. Each test case uses the `assertEqual` method to verify that the output of the function matches the expected output.

You can run this script directly to execute the tests. If all tests pass, you should see a message indicating that the tests were successful. If any tests fail, you will see an error message indicating which test failed and why.