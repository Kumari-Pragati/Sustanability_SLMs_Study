You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

 import unittest
from HumanEval_75_code import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):

    def test_is_multiply_prime_true(self):
        self.assertTrue(is_multiply_prime(30))
        self.assertTrue(is_multiply_prime(21))
        self.assertTrue(is_multiply_prime(35))

    def test_is_multiply_prime_false(self):
        self.assertFalse(is_multiply_prime(1))
        self.assertFalse(is_multiply_prime(4))
        self.assertFalse(is_multiply_prime(100))
        self.assertFalse(is_multiply_prime(101))
        self.assertFalse(is_multiply_prime(102))

    def test_is_multiply_prime_edge_cases(self):
        self.assertTrue(is_multiply_prime(2))
        self.assertTrue(is_multiply_prime(3))
        self.assertTrue(is_multiply_prime(5))
        self.assertTrue(is_multiply_prime(7))
        self.assertTrue(is_multiply_prime(11))
        self.assertTrue(is_multiply_prime(13))
        self.assertTrue(is_multiply_prime(17))
        self.assertTrue(is_multiply_prime(19))
        self.assertTrue(is_multiply_prime(23))
        self.assertTrue(is_multiply_prime(29))
        self.assertTrue(is_multiply_prime(31))
        self.assertTrue(is_multiply_prime(37))
        self.assertTrue(is_multiply_prime(41))
        self.assertTrue(is_multiply_prime(43))
        self.assertTrue(is_multiply_prime(47))
        self.assertTrue(is_multiply_prime(53))
        self.assertTrue(is_multiply_prime(59))
        self.assertTrue(is_multiply_prime(61))
        self.assertTrue(is_multiply_prime(67))
        self.assertTrue(is_multiply_prime(71))
        self.assertTrue(is_multiply_prime(73))
        self.assertTrue(is_multiply_prime(79))
        self.assertTrue(is_multiply_prime(83))
        self.assertTrue(is_multiply_prime(89))
        self.assertTrue(is_multiply_prime(97))

if __name__ == '__main__':
    unittest.main()