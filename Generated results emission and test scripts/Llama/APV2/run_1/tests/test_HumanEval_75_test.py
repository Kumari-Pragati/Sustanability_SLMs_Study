system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
    return Falseassistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_75_code import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):

    def test_is_multiply_prime_true(self):
        self.assertTrue(is_multiply_prime(30))
        self.assertTrue(is_multiply_prime(60))
        self.assertTrue(is_multiply_prime(90))
        self.assertTrue(is_multiply_prime(210))

    def test_is_multiply_prime_false(self):
        self.assertFalse(is_multiply_prime(1))
        self.assertFalse(is_multiply_prime(2))
        self.assertFalse(is_multiply_prime(3))
        self.assertFalse(is_multiply_prime(4))
        self.assertFalse(is_multiply_prime(5))
        self.assertFalse(is_multiply_prime(6))
        self.assertFalse(is_multiply_prime(7))
        self.assertFalse(is_multiply_prime(8))
        self.assertFalse(is_multiply_prime(9))
        self.assertFalse(is_multiply_prime(10))
        self.assertFalse(is_multiply_prime(11))
        self.assertFalse(is_multiply_prime(12))
        self.assertFalse(is_multiply_prime(13))
        self.assertFalse(is_multiply_prime(14))
        self.assertFalse(is_multiply_prime(15))
        self.assertFalse(is_multiply_prime(16))
        self.assertFalse(is_multiply_prime(17))
        self.assertFalse(is_multiply_prime(18))
        self.assertFalse(is_multiply_prime(19))
        self.assertFalse(is_multiply_prime(20))
        self.assertFalse(is_multiply_prime(21))
        self.assertFalse(is_multiply_prime(22))
        self.assertFalse(is_multiply_prime(23))
        self.assertFalse(is_multiply_prime(24))
        self.assertFalse(is_multiply_prime(25))
        self.assertFalse(is_multiply_prime(26))
        self.assertFalse(is_multiply_prime(27))
        self.assertFalse(is_multiply_prime(28))
        self.assertFalse(is_multiply_prime(29))
        self.assertFalse(is_multiply_prime(31))
        self.assertFalse(is_multiply_prime(32))
        self.assertFalse(is_multiply_prime(33))
        self.assertFalse(is_multiply_prime(34))
        self.assertFalse(is_multiply_prime(35))
        self.assertFalse(is_multiply_prime(36))
        self.assertFalse(is_multiply_prime(37))
        self.assertFalse(is_multiply_prime(38))
        self.assertFalse(is_multiply_prime(39))
        self.assertFalse(is_multiply_prime(40))
        self.assertFalse(is_multiply_prime(41))
        self.assertFalse(is_multiply_prime(42))
        self.assertFalse(is_multiply_prime(43))
        self.assertFalse(is_multiply_prime(44))
        self.assertFalse(is_multiply_prime(45))
        self.assertFalse(is_multiply_prime(46))
        self.assertFalse(is_multiply_prime(47))
        self.assertFalse(is_multiply_prime(48))
        self.assertFalse(is_multiply_prime(49))
        self.assertFalse(is_multiply_prime(50))
        self.assertFalse(is_multiply_prime(51))
        self.assertFalse(is_multiply_prime(52))
        self.assertFalse(is_multiply_prime(53))
        self.assertFalse(is_multiply_prime(54))
        self.assertFalse(is_multiply_prime(55))
        self.assertFalse(is_multiply_prime(56))
        self.assertFalse(is_multiply_prime(57))
        self.assertFalse(is_multiply_prime(58))
        self.assertFalse(is_multiply_prime(59))
        self.assertFalse(is_multiply_prime(60))
        self.assertFalse(is_multiply_prime(61))
        self.assertFalse(is_multiply_prime(62))
        self.assertFalse(is_multiply_prime(63))
        self.assertFalse(is_multiply_prime(64))
        self.assertFalse(is_multiply_prime(65))
        self.assertFalse(is_multiply_prime(66))
        self.assertFalse(is_multiply_prime(67))
        self.assertFalse(is_multiply_prime(68))
        self.assertFalse(is_multiply_prime(69))
        self.assertFalse(is_multiply_prime(70))
        self.assertFalse(is_multiply_prime(71))
        self.assertFalse(is_multiply_prime(72))
        self.assertFalse(is_multiply_prime(73))
        self.assertFalse(is_multiply_prime(74))
        self.assertFalse(is_multiply_prime(75))
        self.assertFalse(is_multiply_prime(76))
        self.assertFalse(is_multiply_prime(77))
        self.assertFalse(is_multiply_prime(78))
        self.assertFalse(is_multiply_prime(79))
        self.assertFalse(is_multiply_prime(80))
        self.assertFalse(is_multiply_prime(81))
        self.assertFalse(is_multiply_prime(82))
        self.assertFalse(is_multiply_prime(83))
        self.assertFalse(is_multiply_prime(84))
        self.assertFalse(is_multiply_prime(85))
        self.assertFalse(is_multiply_prime(86))
        self.assertFalse(is_multiply_prime(87))
        self.assertFalse(is_multiply_prime(88))
        self.assertFalse(is_multiply_prime(89))
        self.assertFalse(is_multiply_prime(90))
        self.assertFalse(is_multiply_prime(91))
        self.assertFalse(is_multiply_prime(92))
        self.assertFalse(is_multiply_prime(93))
        self.assertFalse(is_multiply_prime(94))
        self.assertFalse(is_multiply_prime(95))
        self.assertFalse(is_multiply_prime(96))
        self.assertFalse(is_multiply_prime(97))
        self.assertFalse(is_multiply_prime(98))
        self.assertFalse(is_multiply_prime(99))
        self.assertFalse(is_multiply_prime(100))

    def test_is_multiply_prime_edge_cases(self):
        self.assertTrue(is_multiply_prime(2))
        self.assertTrue(is_multiply_prime(3))
        self.assertTrue(is_multiply_prime(5))
        self.assertTrue(is