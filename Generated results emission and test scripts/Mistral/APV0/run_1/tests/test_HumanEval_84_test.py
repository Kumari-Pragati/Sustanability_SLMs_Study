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

 Here is a unittest test script for the provided function `solve(N)`. I've added several test cases to cover different scenarios, including edge cases and negative numbers.


import unittest
from HumanEval_84_code import solve

class TestSolveFunction(unittest.TestCase):

    def test_solve_positive_numbers(self):
        self.assertEqual(solve(1), "1")
        self.assertEqual(solve(3), "11")
        self.assertEqual(solve(10), "1010")
        self.assertEqual(solve(100), "1100100")
        self.assertEqual(solve(1000), "1000")
        self.assertEqual(solve(150), "1101010")
        self.assertEqual(solve(147), "11001111")
        self.assertEqual(solve(9876), "11110010110")

    def test_solve_large_numbers(self):
        self.assertEqual(solve(5000), "11111000100")
        self.assertEqual(solve(9999), "111111110111")
        self.assertEqual(solve(10000), "10000000000")

    def test_solve_zero(self):
        self.assertEqual(solve(0), "0")

    def test_solve_negative_numbers(self):
        self.assertEqual(solve(-1), "10")
        self.assertEqual(solve(-3), "11")
        self.assertEqual(solve(-10), "1010")
        self.assertEqual(solve(-100), "1100100")
        self.assertEqual(solve(-1000), "1000")
        self.assertEqual(solve(-150), "1101010")
        self.assertEqual(solve(-147), "11001111")
        self.assertEqual(solve(-9876), "11110010110")

    def test_solve_out_of_range(self):
        self.assertRaises(ValueError, solve, -10001)
        self.assertRaises(ValueError, solve, 10001)

if __name__ == '__main__':
    unittest.main()


This test script includes tests for positive numbers, large numbers, zero, negative numbers, and out-of-range numbers. Make sure to save this script as `test_solve.py` and run it using the command `python test_solve.py`.