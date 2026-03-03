user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return Falseassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_75_code import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):

    def test_is_multiply_prime(self):
        self.assertTrue(is_multiply_prime(30))  # 30 = 2 * 3 * 5
        self.assertTrue(is_multiply_prime(42))  # 42 = 2 * 3 * 7
        self.assertTrue(is_multiply_prime(60))  # 60 = 2 * 3 * 10
        self.assertFalse(is_multiply_prime(1))  # 1 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(2))  # 2 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(3))  # 3 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(4))  # 4 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(5))  # 5 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(6))  # 6 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(7))  # 7 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(8))  # 8 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(9))  # 9 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(10))  # 10 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(11))  # 11 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(12))  # 12 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(13))  # 13 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(14))  # 14 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(15))  # 15 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(16))  # 16 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(17))  # 17 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(18))  # 18 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(19))  # 19 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(20))  # 20 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(21))  # 21 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(22))  # 22 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(23))  # 23 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(24))  # 24 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(25))  # 25 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(26))  # 26 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(27))  # 27 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(28))  # 28 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(29))  # 29 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(31))  # 31 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(32))  # 32 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(33))  # 33 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(34))  # 34 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(35))  # 35 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(36))  # 36 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(37))  # 37 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(38))  # 38 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(39))  # 39 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(40))  # 40 is not a multiplication of 3 prime numbers
        self.assertFalse(is_multiply_prime(41))  # 41