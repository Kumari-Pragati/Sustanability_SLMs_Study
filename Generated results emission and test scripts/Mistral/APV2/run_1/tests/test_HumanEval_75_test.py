You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_75_code import is_multiply_prime
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less than 100. 
    Example:
        is_multiply_prime(30) == True
        30 = 2 * 3 * 5
    """

    def is_prime(n):
        for j in range(2, n):
            if n % j == 0:
                return False
        return True

    for i in range(2, 101):
        if not is_prime(i):
            continue
        for j in range(2, 101):
            if not is_prime(j):
                continue
            for k in range(2, 101):
                if not is_prime(k):
                    continue
                if i * j * k == a:
                    return True
    return False

 Here is a comprehensive unittest test suite for the `is_multiply_prime` function:


import unittest
from HumanEval_75_code import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):

    def test_is_multiply_prime(self):
        self.assertTrue(is_multiply_prime(30))
        self.assertTrue(is_multiply_prime(60))
        self.assertTrue(is_multiply_prime(90))
        self.assertFalse(is_multiply_prime(15))
        self.assertFalse(is_multiply_prime(20))
        self.assertFalse(is_multiply_prime(45))
        self.assertFalse(is_multiply_prime(75))
        self.assertFalse(is_multiply_prime(101))
        self.assertFalse(is_multiply_prime(102))

if __name__ == '__main__':
    unittest.main()


This test suite includes both positive and negative test cases for the `is_multiply_prime` function. The positive test cases are numbers that should return `True` according to the function's definition, and the negative test cases are numbers that should return `False`. The test cases cover a range of numbers from 15 to 102, including multiples of 3, 5, and 9, as well as numbers that are not multiples of any of these primes.