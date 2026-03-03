You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_103_code import rounded_avg
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """

    if m < n:
        return -1
    summation = 0
    for i in range(n, m + 1):
        summation += i
    return bin(round(summation / (m - n + 1)))


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_103_code import rounded_avg

class TestRoundedAvg(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(rounded_avg(1, 5), "0b11")
        self.assertEqual(rounded_avg(10, 20), "0b1111")
        self.assertEqual(rounded_avg(20, 33), "0b11010")

    def test_invalid_input(self):
        self.assertEqual(rounded_avg(7, 5), -1)

    def test_edge_cases(self):
        self.assertEqual(rounded_avg(1, 1), "0b1")
        self.assertEqual(rounded_avg(100, 100), "0b1100100")

    def test_negative_input(self):
        self.assertEqual(rounded_avg(-1, 1), -1)
        self.assertEqual(rounded_avg(1, -1), -1)
        self.assertEqual(rounded_avg(-1, -1), -1)

if __name__ == '__main__':
    unittest.main()


This script includes four test cases:

1. `test_valid_input`: Tests the function with valid input.
2. `test_invalid_input`: Tests the function with invalid input (n > m).
3. `test_edge_cases`: Tests the function with edge cases (n = m, n and m are the same).
4. `test_negative_input`: Tests the function with negative input.

Please note that you need to have the function `rounded_avg` in a file named `HumanEval_103_code.py` in the same directory as the test script for the test to work.