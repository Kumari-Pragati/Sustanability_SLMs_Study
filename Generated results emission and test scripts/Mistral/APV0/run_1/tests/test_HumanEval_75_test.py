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
    return False

 Here is a unittest test script for the `is_multiply_prime` function. The test cases cover the edge cases and a range of numbers within the given limit.


import unittest
from HumanEval_75_code import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):

    def test_edge_cases(self):
        self.assertTrue(is_multiply_prime(1))
        self.assertFalse(is_multiply_prime(2))
        self.assertFalse(is_multiply_prime(3))
        self.assertFalse(is_multiply_prime(4))
        self.assertFalse(is_multiply_prime(5))
        self.assertFalse(is_multiply_prime(6))
        self.assertFalse(is_multiply_prime(7))
        self.assertFalse(is_multiply_prime(8))
        self.assertFalse(is_multiply_prime(9))
        self.assertFalse(is_multiply_prime(10))

    def test_multiples_of_primes(self):
        self.assertTrue(is_multiply_prime(6))
        self.assertTrue(is_multiply_prime(9))
        self.assertTrue(is_multiply_prime(10))
        self.assertTrue(is_multiply_prime(15))
        self.assertTrue(is_multiply_prime(20))
        self.assertTrue(is_multiply_prime(21))
        self.assertTrue(is_multiply_prime(22))
        self.assertTrue(is_multiply_prime(24))
        self.assertTrue(is_multiply_prime(25))
        self.assertTrue(is_multiply_prime(27))
        self.assertTrue(is_multiply_prime(30))
        self.assertTrue(is_multiply_prime(33))
        self.assertTrue(is_multiply_prime(36))
        self.assertTrue(is_multiply_prime(40))
        self.assertTrue(is_multiply_prime(42))
        self.assertTrue(is_multiply_prime(45))
        self.assertTrue(is_multiply_prime(48))
        self.assertTrue(is_multiply_prime(50))
        self.assertTrue(is_multiply_prime(54))
        self.assertTrue(is_multiply_prime(55))
        self.assertTrue(is_multiply_prime(56))
        self.assertTrue(is_multiply_prime(60))
        self.assertTrue(is_multiply_prime(63))
        self.assertTrue(is_multiply_prime(66))
        self.assertTrue(is_multiply_prime(70))
        self.assertTrue(is_multiply_prime(72))
        self.assertTrue(is_multiply_prime(75))
        self.assertTrue(is_multiply_prime(78))
        self.assertTrue(is_multiply_prime(80))
        self.assertTrue(is_multiply_prime(81))
        self.assertTrue(is_multiply_prime(84))
        self.assertTrue(is_multiply_prime(88))
        self.assertTrue(is_multiply_prime(90))
        self.assertTrue(is_multiply_prime(99))

    def test_other_numbers(self):
        self.assertFalse(is_multiply_prime(11))
        self.assertFalse(is_multiply_prime(12))
        self.assertFalse(is_multiply_prime(13))
        self.assertFalse(is_multiply_prime(14))
        self.assertFalse(is_multiply_prime(16))
        self.assertFalse(is_multiply_prime(17))
        self.assertFalse(is_multiply_prime(18))
        self.assertFalse(is_multiply_prime(19))
        self.assertFalse(is_multiply_prime(23))
        self.assertFalse(is_multiply_prime(26))
        self.assertFalse(is_multiply_prime(28))
        self.assertFalse(is_multiply_prime(29))