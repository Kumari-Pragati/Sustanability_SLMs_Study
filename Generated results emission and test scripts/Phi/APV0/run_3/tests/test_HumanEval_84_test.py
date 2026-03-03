Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_84_code import solve
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.

    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".

    Variables:
        @N integer
            Constraints: 0 ≤ N ≤ 10000.
    Output:
        a string of binary number
    """

    return bin(sum(int(i) for i in str(N)))[2:]

 import unittest
from HumanEval_84_code import solve

class TestSolveFunction(unittest.TestCase):

    def test_sum_of_digits_binary_one(self):
        self.assertEqual(solve(1000), "1")

    def test_sum_of_digits_binary_six(self):
        self.assertEqual(solve(150), "110")

    def test_sum_of_digits_binary_twelve(self):
        self.assertEqual(solve(147), "1100")

    def test_sum_of_digits_binary_zero(self):
        self.assertEqual(solve(0), "0")

    def test_sum_of_digits_binary_ten_thousand(self):
        self.assertEqual(solve(10000), "11100010000")

    def test_sum_of_digits_binary_negative(self):
        with self.assertRaises(ValueError):
            solve(-1)

    def test_sum_of_digits_binary_out_of_range(self):
        with self.assertRaises(ValueError):
            solve(10001)

if __name__ == '__main__':
    unittest.main()