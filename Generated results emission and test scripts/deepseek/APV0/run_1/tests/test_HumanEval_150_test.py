You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_150_code import x_or_y

class TestXOrY(unittest.TestCase):

    def test_prime_number(self):
        self.assertEqual(x_or_y(7, 34, 12), 34)
        self.assertEqual(x_or_y(13, 10, 20), 10)
        self.assertEqual(x_or_y(2, 50, 100), 50)

    def test_non_prime_number(self):
        self.assertEqual(x_or_y(15, 8, 5), 5)
        self.assertEqual(x_or_y(10, 200, 300), 300)
        self.assertEqual(x_or_y(12, 700, 800), 800)

    def test_edge_cases(self):
        self.assertEqual(x_or_y(1, 100, 200), 200)
        self.assertEqual(x_or_y(0, 300, 400), 400)
        self.assertEqual(x_or_y(-5, 500, 600), 600)

if __name__ == '__main__':
    unittest.main()


This script includes three test methods:

- `test_prime_number` tests the function with prime numbers.
- `test_non_prime_number` tests the function with non-prime numbers.
- `test_edge_cases` tests the function with edge cases like 1, 0, and negative numbers.

Please note that the function `x_or_y` should be in a file named `HumanEval_150_code.py` in the same directory as the test script for the test to work.