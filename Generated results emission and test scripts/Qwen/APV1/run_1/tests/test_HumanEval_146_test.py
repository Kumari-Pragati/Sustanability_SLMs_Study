system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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


assistant

import unittest

from HumanEval_146_code import specialFilter

class TestSpecialFilter(unittest.TestCase):

    def test_special_filter(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)
        self.assertEqual(specialFilter([-1, -2, -3, -4, -5]), 0)
        self.assertEqual(specialFilter([10, 20, 30, 40, 50]), 0)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestSpecialFilter` class within the `unittest` module, which inherits from `unittest.TestCase`. The `specialFilter` function is imported at the beginning of this file. The `test_special_filter` method contains several assertions to check the correctness of the `specialFilter` function against various inputs. If any assertion fails, it will raise an error indicating which test failed. Finally, the `unittest.main()` call runs all tests defined in the `TestSpecialFilter` class.