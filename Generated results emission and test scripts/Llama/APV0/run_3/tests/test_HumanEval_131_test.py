user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_131_code import digits
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    odd_count = 0
    for digit in str(n):
        int_digit = int(digit)
        if int_digit % 2 == 1:
            product = product * int_digit
            odd_count += 1
    if odd_count == 0:
        return 0
    else:
        return productassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_131_code import digits

class TestDigitsFunction(unittest.TestCase):

    def test_digits(self):
        self.assertEqual(digits(1), 1)
        self.assertEqual(digits(4), 0)
        self.assertEqual(digits(235), 15)
        self.assertEqual(digits(12345), 45)
        self.assertEqual(digits(24680), 0)
        self.assertEqual(digits(111), 111)
        self.assertEqual(digits(222), 0)
        self.assertEqual(digits(123456789), 315)

if __name__ == '__main__':
    unittest.main()


This script includes 8 test cases to cover different scenarios:

- Test cases 1 and 2: Test the function with single-digit and two-digit numbers.
- Test case 3: Test the function with a three-digit number.
- Test case 4: Test the function with a five-digit number.
- Test case 5: Test the function with a six-digit number where all digits are even.
- Test case 6: Test the function with a three-digit number where all digits are odd.
- Test case 7: Test the function with a two-digit number where all digits are even.
- Test case 8: Test the function with a nine-digit number.