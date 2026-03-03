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
    return bin(round(summation / (m - n + 1)))assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_103_code import rounded_avg

class TestRoundAvg(unittest.TestCase):

    def test_rounded_avg(self):
        self.assertEqual(rounded_avg(1, 5), "0b11")
        self.assertEqual(rounded_avg(7, 5), -1)
        self.assertEqual(rounded_avg(10, 20), "0b1111")
        self.assertEqual(rounded_avg(20, 33), "0b11010")
        self.assertEqual(rounded_avg(5, 5), "0b1")
        self.assertEqual(rounded_avg(10, 10), "0b1010")
        self.assertEqual(rounded_avg(1, 1), "0b1")
        self.assertEqual(rounded_avg(2, 2), "0b10")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rounded_avg("a", 5)
        with self.assertRaises(TypeError):
            rounded_avg(1, "b")
        with self.assertRaises(TypeError):
            rounded_avg("a", "b")

if __name__ == '__main__':
    unittest.main()


This script includes two test cases: `test_rounded_avg` and `test_invalid_input`. 

- `test_rounded_avg` tests the function with different inputs and checks if the output is as expected. It also includes some edge cases like when `n` and `m` are equal, or when `n` is greater than `m`.

- `test_invalid_input` tests the function with invalid inputs like strings instead of integers. It checks if the function raises a `TypeError` when given invalid inputs.