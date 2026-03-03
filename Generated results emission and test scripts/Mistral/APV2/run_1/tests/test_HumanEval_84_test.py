You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the provided Python function:


import unittest
from HumanEval_84_code import solve

class TestSolve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(1), "1")
        self.assertEqual(solve(2), "10")
        self.assertEqual(solve(3), "11")
        self.assertEqual(solve(4), "100")
        self.assertEqual(solve(5), "101")
        self.assertEqual(solve(10), "1010")
        self.assertEqual(solve(15), "1111")
        self.assertEqual(solve(100), "1100100")
        self.assertEqual(solve(1000), "1")
        self.assertEqual(solve(150), "110")
        self.assertEqual(solve(147), "1100")
        self.assertEqual(solve(148), "1101")
        self.assertEqual(solve(149), "1101")
        self.assertEqual(solve(1500), "11001000")
        self.assertEqual(solve(5000), "11110100000")
        self.assertEqual(solve(10000), "1000000000")

if __name__ == '__main__':
    unittest.main()


This test suite includes a test function `test_solve` that checks the function `solve` for various input values within the given constraints. The test suite uses the `assertEqual` method to compare the expected output with the actual output of the function.