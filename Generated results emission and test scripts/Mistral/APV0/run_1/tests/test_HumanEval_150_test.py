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

 Here is a unittest test script for the `x_or_y` function:


import unittest
from HumanEval_150_code import x_or_y

class TestXOrY(unittest.TestCase):

    def test_x_or_y(self):
        self.assertEqual(x_or_y(7, 34, 12), 34)
        self.assertEqual(x_or_y(15, 8, 5), 5)
        self.assertEqual(x_or_y(2, 10, 20), 20)
        self.assertEqual(x_or_y(1, 10, 20), 20)
        self.assertEqual(x_or_y(29, 30, 40), 30)
        self.assertEqual(x_or_y(3, 10, 20), 10)
        self.assertEqual(x_or_y(4, 10, 20), 20)
        self.assertEqual(x_or_y(6, 10, 20), 10)

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the examples provided in the function documentation, as well as additional test cases to ensure the function works correctly for prime numbers, non-prime numbers, and edge cases (e.g., n=1). You can run this script directly by saving it as a .py file and executing it using the command `python filename.py`.