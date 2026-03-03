You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_155_code import even_odd_count
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_155_code import even_odd_count

class TestEvenOddCount(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(even_odd_count(123), (1, 2))
        self.assertEqual(even_odd_count(123456), (3, 3))
        self.assertEqual(even_odd_count(123456789), (4, 5))

    def test_negative_numbers(self):
        self.assertEqual(even_odd_count(-12), (1, 1))
        self.assertEqual(even_odd_count(-123456), (3, 3))
        self.assertEqual(even_odd_count(-123456789), (4, 5))

    def test_single_digit_numbers(self):
        self.assertEqual(even_odd_count(0), (1, 0))
        self.assertEqual(even_odd_count(1), (0, 1))
        self.assertEqual(even_odd_count(2), (1, 0))
        self.assertEqual(even_odd_count(3), (0, 1))

    def test_zero(self):
        self.assertEqual(even_odd_count(0), (1, 0))

if __name__ == '__main__':
    unittest.main()


This script includes 4 test cases:

1. `test_positive_numbers`: Tests the function with positive numbers.
2. `test_negative_numbers`: Tests the function with negative numbers.
3. `test_single_digit_numbers`: Tests the function with single digit numbers.
4. `test_zero`: Tests the function with zero.

Each test case checks if the function's output matches the expected output. If the function's output does not match the expected output, the test case will fail.

Please note that you need to have the function `even_odd_count` in a file named `HumanEval_155_code.py` in the same directory as this test script for the test cases to run successfully.