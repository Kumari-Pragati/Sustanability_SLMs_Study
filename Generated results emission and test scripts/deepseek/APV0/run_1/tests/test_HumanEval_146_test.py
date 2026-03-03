You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_146_code import specialFilter

class TestSpecialFilter(unittest.TestCase):
    def test_specialFilter(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)
        self.assertEqual(specialFilter([10, 20, 30, 40, 50]), 0)
        self.assertEqual(specialFilter([11, 22, 33, 44, 55]), 0)
        self.assertEqual(specialFilter([13, 23, 31, 45, 57]), 3)
        self.assertEqual(specialFilter([1, 2, 3, 4, 5]), 0)
        self.assertEqual(specialFilter([101, 111, 121, 131, 141]), 5)
        self.assertEqual(specialFilter([-11, -21, -31, -41, -51]), 0)
        self.assertEqual(specialFilter([-13, -23, -35, -47, -59]), 0)
        self.assertEqual(specialFilter([-15, -25, -35, -45, -55]), 0)

if __name__ == '__main__':
    unittest.main()


This script tests the `specialFilter` function with a variety of inputs to ensure it is working as expected. The `assertEqual` method is used to check that the output of the function matches the expected output. If the function is working correctly, all of these tests should pass.