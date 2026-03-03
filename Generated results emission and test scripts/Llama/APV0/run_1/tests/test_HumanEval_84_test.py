user

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

    return bin(sum(int(i) for i in str(N)))[2:]assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_84_code import solve

class TestSolveFunction(unittest.TestCase):

    def test_solve_function(self):
        # Test case 1: N = 1000
        self.assertEqual(solve(1000), "1")

        # Test case 2: N = 150
        self.assertEqual(solve(150), "110")

        # Test case 3: N = 147
        self.assertEqual(solve(147), "1100")

        # Test case 4: N = 0
        self.assertEqual(solve(0), "0")

        # Test case 5: N = 1
        self.assertEqual(solve(1), "1")

        # Test case 6: N = 10000
        self.assertEqual(solve(10000), "1111")

        # Test case 7: N = 12345
        self.assertEqual(solve(12345), "10011")

        # Test case 8: N = 98765
        self.assertEqual(solve(98765), "1111011")

if __name__ == '__main__':
    unittest.main()


This script includes 8 test cases to cover different scenarios, including edge cases like N = 0 and N = 1. The `assertEqual` method is used to compare the output of the `solve` function with the expected output. If the output does not match the expected output, the test case will fail and an error message will be displayed.