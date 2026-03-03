You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

class TestXOrYFunction(unittest.TestCase):

    def test_prime_number(self):
        self.assertEqual(x_or_y(7, 34, 12), 34)

    def test_non_prime_number(self):
        self.assertEqual(x_or_y(15, 8, 5), 5)

    def test_number_one(self):
        self.assertEqual(x_or_y(1, 8, 5), 5)

    def test_small_prime_number(self):
        self.assertEqual(x_or_y(2, 8, 5), 8)

    def test_large_prime_number(self):
        self.assertEqual(x_or_y(11, 8, 5), 8)

    def test_even_number(self):
        self.assertEqual(x_or_y(4, 8, 5), 5)

    def test_odd_number(self):
        self.assertEqual(x_or_y(9, 8, 5), 5)

    def test_zero(self):
        self.assertEqual(x_or_y(0, 8, 5), 5)

    def test_negative_number(self):
        self.assertEqual(x_or_y(-1, 8, 5), 5)

if __name__ == '__main__':
    unittest.main()