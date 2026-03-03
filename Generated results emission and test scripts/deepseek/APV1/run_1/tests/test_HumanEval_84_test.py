You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_84_code import solve

class TestSolve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(1000), "1")
        self.assertEqual(solve(150), "110")
        self.assertEqual(solve(147), "1100")
        self.assertEqual(solve(0), "0")
        self.assertEqual(solve(1), "1")
        self.assertEqual(solve(10), "1")
        self.assertEqual(solve(11), "10")
        self.assertEqual(solve(12), "11")
        self.assertEqual(solve(100), "1")
        self.assertEqual(solve(101), "10")
        self.assertEqual(solve(110), "10")
        self.assertEqual(solve(111), "11")
        self.assertEqual(solve(9999), "1111001001")

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure that the function is working correctly. It tests the function with a variety of input values, including both small and large numbers, as well as numbers that are powers of 10. It also tests the function with the edge cases of 0 and 1, as well as numbers that are close to the maximum allowed value of 10000.