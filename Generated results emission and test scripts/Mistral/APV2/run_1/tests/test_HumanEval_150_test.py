You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is a complete unittest test suite for the `x_or_y` function:


import unittest
from HumanEval_150_code import x_or_y

class TestXOrY(unittest.TestCase):

    def test_x_or_y(self):
        self.assertEqual(x_or_y(7, 34, 12), 34)
        self.assertEqual(x_or_y(15, 8, 5), 5)
        self.assertEqual(x_or_y(2, 1, 2), 1)
        self.assertEqual(x_or_y(4, 2, 3), 3)
        self.assertEqual(x_or_y(1, 1, 2), 2)
        self.assertEqual(x_or_y(19, 10, 20), 10)
        self.assertEqual(x_or_y(29, 30, 40), 40)
        self.assertEqual(x_or_y(31, 50, 60), 50)

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover different scenarios, such as prime numbers, non-prime numbers, edge cases (like n=1), and various input values for x and y. The test cases use the `assertEqual` method to compare the expected output with the actual output of the `x_or_y` function.