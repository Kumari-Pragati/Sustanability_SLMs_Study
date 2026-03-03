system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Function to be tested
from HumanEval_103_code import rounded_avg

class TestRoundAvg(unittest.TestCase):

    def test_rounded_avg(self):
        self.assertEqual(rounded_avg(1, 5), '0b11')
        self.assertEqual(rounded_avg(7, 5), -1)
        self.assertEqual(rounded_avg(10, 20), '0b1111')
        self.assertEqual(rounded_avg(20, 33), '0b11010')

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines a class `TestRoundAvg` which inherits from `unittest.TestCase`. It contains a method `test_rounded_avg` that tests the `rounded_avg` function using assertions. The `assertEqual` methods check if the output of `rounded_avg` matches the expected results. Finally, it runs all the tests when executed directly.