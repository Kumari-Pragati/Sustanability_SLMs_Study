user

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
        return xassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_150_code import x_or_y

class TestXorY(unittest.TestCase):

    def test_prime_number(self):
        self.assertEqual(x_or_y(7, 34, 12), 34)

    def test_non_prime_number(self):
        self.assertEqual(x_or_y(15, 8, 5), 5)

    def test_one(self):
        self.assertEqual(x_or_y(1, 34, 12), 12)

    def test_negative_number(self):
        self.assertEqual(x_or_y(-1, 34, 12), 12)

    def test_zero(self):
        self.assertEqual(x_or_y(0, 34, 12), 12)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            x_or_y('a', 34, 12)

if __name__ == '__main__':
    unittest.main()


This script includes five test cases:

1. `test_prime_number`: Tests the function with a prime number (7) and checks if it returns the value of x (34).
2. `test_non_prime_number`: Tests the function with a non-prime number (15) and checks if it returns the value of y (5).
3. `test_one`: Tests the function with the number 1 and checks if it returns the value of y (12).
4. `test_negative_number`: Tests the function with a negative number (-1) and checks if it returns the value of y (12).
5. `test_zero`: Tests the function with the number 0 and checks if it returns the value of y (12).
6. `test_non_integer`: Tests the function with a non-integer value ('a') and checks if it raises a TypeError.