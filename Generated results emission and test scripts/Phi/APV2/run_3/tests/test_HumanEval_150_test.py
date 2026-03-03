You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

 
import unittest
from HumanEval_150_code import x_or_y

class TestXOrY(unittest.TestCase):

    def test_prime_number(self):
        self.assertEqual(x_or_y(7, 34, 12), 34)

    def test_non_prime_number(self):
        self.assertEqual(x_or_y(15, 8, 5), 5)

    def test_one(self):
        self.assertEqual(x_or_y(1, 34, 12), 12)

    def test_zero(self):
        self.assertEqual(x_or_y(0, 34, 12), 12)

    def test_negative_number(self):
        self.assertEqual(x_or_y(-5, 34, 12), 12)

    def test_even_number(self):
        self.assertEqual(x_or_y(8, 34, 12), 12)

    def test_prime_number_smaller_than_two(self):
        self.assertEqual(x_or_y(1, 34, 12), 12)

    def test_prime_number_two(self):
        self.assertEqual(x_or_y(2, 34, 12), 12)

    def test_prime_number_large(self):
        self.assertEqual(x_or_y(17, 34, 12), 34)

    def test_non_prime_number_large(self):
        self.assertEqual(x_or_y(20, 8, 5), 5)

if __name__ == '__main__':
    unittest.main()


This test suite covers various cases for the `x_or_y` function, including prime and non-prime numbers, edge cases like 1, 0, negative numbers, and even numbers. It ensures that the function behaves as expected across a range of inputs.