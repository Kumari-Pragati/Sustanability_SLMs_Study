You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_150_code import x_or_y
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n == 1:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
            break
    else:
        return x


### Response:
Here is a complete unittest test suite for the given function:


import unittest
from HumanEval_150_code import x_or_y

class TestXOrY(unittest.TestCase):

    def test_prime_number(self):
        self.assertEqual(x_or_y(7, 34, 12), 34)
        self.assertEqual(x_or_y(2, 8, 5), 8)
        self.assertEqual(x_or_y(3, 10, 20), 10)

    def test_non_prime_number(self):
        self.assertEqual(x_or_y(15, 8, 5), 5)
        self.assertEqual(x_or_y(10, 15, 25), 25)
        self.assertEqual(x_or_y(100, 10, 20), 20)

    def test_edge_cases(self):
        self.assertEqual(x_or_y(1, 34, 12), 12)
        self.assertEqual(x_or_y(0, 8, 5), 5)
        self.assertEqual(x_or_y(-1, 10, 20), 20)

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_prime_number`: This test case checks the function's behavior with prime numbers.
2. `test_non_prime_number`: This test case checks the function's behavior with non-prime numbers.
3. `test_edge_cases`: This test case checks the function's behavior with edge cases such as 1, 0, and negative numbers.

Please note that the function `x_or_y` is not defined in the provided code. You should define it in the `HumanEval_150_code` module for the test to work.