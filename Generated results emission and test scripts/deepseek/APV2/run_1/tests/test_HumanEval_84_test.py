You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_84_code import solve

class TestSolve(unittest.TestCase):

    def test_solve(self):
        # Test cases
        test_cases = [
            (1000, '1'),
            (150, '110'),
            (147, '1100'),
            (0, '0'),
            (1, '1'),
            (10, '1010'),
            (100, '1100100'),
            (9999, '1001011001011')
        ]

        # Run test cases
        for N, expected in test_cases:
            with self.subTest(N=N):
                self.assertEqual(solve(N), expected)

if __name__ == '__main__':
    unittest.main()


This test suite includes a single test case `test_solve` that tests the `solve` function with a variety of input values. Each test case consists of an input value `N` and the expected output. The `with self.subTest(N=N):` line is used to make the test output more informative when a test case fails.

The `assertEqual` method is used to check if the output of the `solve` function is equal to the expected output for each test case. If the function's output does not match the expected output, the test will fail.

The `if __name__ == '__main__': unittest.main():` line is used to run the test suite when the script is executed.