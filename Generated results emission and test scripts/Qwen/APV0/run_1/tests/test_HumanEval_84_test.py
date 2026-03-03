system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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

    return bin(sum(int(i) for i in str(N)))[2:]


assistant

import unittest

# Function to be tested
def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary."""
    return bin(sum(int(digit) for digit in str(N)))[2:]

class TestBinaryDigitSum(unittest.TestCase):

    def test_sanity(self):
        self.assertEqual(solve(1000), '1')
        self.assertEqual(solve(150), '110')
        self.assertEqual(solve(147), '1100')

    def test_edge_cases(self):
        # Edge case: N=0
        self.assertEqual(solve(0), '0')
        # Edge case: N=9999 (all digits)
        self.assertEqual(solve(9999), '1111111111')
        # Edge case: N=10000 (all digits except one is zero)
        self.assertEqual(solve(10000), '10000')

if __name__ == '__main__':
    unittest.main()


This script defines a `TestBinaryDigitSum` class that inherits from `unittest.TestCase`. It includes two methods:

- `test_sanity`: Tests the function with some common values to ensure it works as expected.
- `test_edge_cases`: Tests edge cases such as when `N` is 0 or when all digits of `N` are the same.

Finally, if this script is run directly (`if __name__ == '__main__':`), it runs all tests defined within the `TestBinaryDigitSum` class using `unittest.main()`.