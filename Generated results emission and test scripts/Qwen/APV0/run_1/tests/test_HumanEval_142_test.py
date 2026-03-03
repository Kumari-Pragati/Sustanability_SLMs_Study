system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_142_code import sum_squares
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    result = []
    for i in range(len(lst)):
        if i % 3 == 0:
            result.append(lst[i] ** 2)
        elif i % 4 == 0 and i % 3 != 0:
            result.append(lst[i] ** 3)
        else:
            result.append(lst[i])
    return sum(result)


assistant

import unittest

# Importing the function to be tested
from HumanEval_142_code import sum_squares

class TestSumSquares(unittest.TestCase):

    def test_sum_squares(self):
        # Test case 1: List with multiples of 3 but no multiples of 4
        self.assertEqual(sum_squares([1, 2, 3]), 6)  # Expected output: 6 (1^2 + 2^2 + 3^2)

        # Test case 2: Empty list
        self.assertEqual(sum_squares([]), 0)  # Expected output: 0

        # Test case 3: List with both multiples of 3 and 4
        self.assertEqual(sum_squares([-1, -5, 2, -1, -5]), -126)  # Expected output: -126 (-1^2 - 5^2 + 2^3 - 1^3 - 5^3)

        # Test case 4: List with only multiples of 4
        self.assertEqual(sum_squares([4, 8, 12]), 792)  # Expected output: 792 (4^3 + 8^3 + 12^3)

        # Test case 5: List with mixed indices
        self.assertEqual(sum_squares([1, 2, 3, 4, 5]), 106)  # Expected output: 106 (1^2 + 2^2 + 3^3 + 4^2 + 5^2)

if __name__ == '__main__':
    unittest.main()


This script imports the `sum_squares` function and defines several test cases using the `assertEqual` method to verify that the function behaves as expected under different conditions. The `unittest.main()` call at the end makes the tests executable when run as a standalone script.