You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given function:


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
        self.assertEqual(solve(11), "100")
        self.assertEqual(solve(100), "1")
        self.assertEqual(solve(10000), "1")

if __name__ == '__main__':
    unittest.main()


This script creates a test class `TestSolve` that inherits from `unittest.TestCase`. Inside this class, there is a method `test_solve` that tests the `solve` function with different inputs. The `assertEqual` method is used to check if the output of the `solve` function is as expected.

The script ends with `if __name__ == '__main__': unittest.main()`, which means that the tests will be run when the script is executed directly.

Please note that the function `solve` is expected to be in a file named `HumanEval_84_code.py` in the same directory as the test script. If the function is in a different location, you will need to import it accordingly.