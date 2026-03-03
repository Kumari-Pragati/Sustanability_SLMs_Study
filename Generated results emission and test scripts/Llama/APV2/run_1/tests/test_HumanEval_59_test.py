system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_59_code import largest_prime_factor
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, k - 1):
            if k % i == 0:
                return False
        return True

    largest = 1
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    return largestassistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_59_code import largest_prime_factor

class TestLargestPrimeFactor(unittest.TestCase):

    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)
        self.assertEqual(largest_prime_factor(100), 1)
        self.assertEqual(largest_prime_factor(2), 2)
        self.assertEqual(largest_prime_factor(3), 3)
        self.assertEqual(largest_prime_factor(4), 2)
        self.assertEqual(largest_prime_factor(5), 5)
        self.assertEqual(largest_prime_factor(6), 3)
        self.assertEqual(largest_prime_factor(7), 7)
        self.assertEqual(largest_prime_factor(8), 2)
        self.assertEqual(largest_prime_factor(9), 3)
        self.assertEqual(largest_prime_factor(10), 2)
        self.assertEqual(largest_prime_factor(11), 11)
        self.assertEqual(largest_prime_factor(12), 2)
        self.assertEqual(largest_prime_factor(13), 13)
        self.assertEqual(largest_prime_factor(14), 2)
        self.assertEqual(largest_prime_factor(15), 2)
        self.assertEqual(largest_prime_factor(16), 2)
        self.assertEqual(largest_prime_factor(17), 17)
        self.assertEqual(largest_prime_factor(18), 2)
        self.assertEqual(largest_prime_factor(19), 19)
        self.assertEqual(largest_prime_factor(20), 2)
        self.assertEqual(largest_prime_factor(21), 2)
        self.assertEqual(largest_prime_factor(22), 2)
        self.assertEqual(largest_prime_factor(23), 23)
        self.assertEqual(largest_prime_factor(24), 2)
        self.assertEqual(largest_prime_factor(25), 2)
        self.assertEqual(largest_prime_factor(26), 2)
        self.assertEqual(largest_prime_factor(27), 2)
        self.assertEqual(largest_prime_factor(28), 2)
        self.assertEqual(largest_prime_factor(29), 2)
        self.assertEqual(largest_prime_factor(30), 2)
        self.assertEqual(largest_prime_factor(31), 2)
        self.assertEqual(largest_prime_factor(32), 2)
        self.assertEqual(largest_prime_factor(33), 2)
        self.assertEqual(largest_prime_factor(34), 2)
        self.assertEqual(largest_prime_factor(35), 2)
        self.assertEqual(largest_prime_factor(36), 2)
        self.assertEqual(largest_prime_factor(37), 2)
        self.assertEqual(largest_prime_factor(38), 2)
        self.assertEqual(largest_prime_factor(39), 2)
        self.assertEqual(largest_prime_factor(40), 2)
        self.assertEqual(largest_prime_factor(41), 2)
        self.assertEqual(largest_prime_factor(42), 2)
        self.assertEqual(largest_prime_factor(43), 2)
        self.assertEqual(largest_prime_factor(44), 2)
        self.assertEqual(largest_prime_factor(45), 2)
        self.assertEqual(largest_prime_factor(46), 2)
        self.assertEqual(largest_prime_factor(47), 2)
        self.assertEqual(largest_prime_factor(48), 2)
        self.assertEqual(largest_prime_factor(49), 2)
        self.assertEqual(largest_prime_factor(50), 2)
        self.assertEqual(largest_prime_factor(51), 2)
        self.assertEqual(largest_prime_factor(52), 2)
        self.assertEqual(largest_prime_factor(53), 2)
        self.assertEqual(largest_prime_factor(54), 2)
        self.assertEqual(largest_prime_factor(55), 2)
        self.assertEqual(largest_prime_factor(56), 2)
        self.assertEqual(largest_prime_factor(57), 2)
        self.assertEqual(largest_prime_factor(58), 2)
        self.assertEqual(largest_prime_factor(59), 2)
        self.assertEqual(largest_prime_factor(60), 2)
        self.assertEqual(largest_prime_factor(61), 2)
        self.assertEqual(largest_prime_factor(62), 2)
        self.assertEqual(largest_prime_factor(63), 2)
        self.assertEqual(largest_prime_factor(64), 2)
        self.assertEqual(largest_prime_factor(65), 2)
        self.assertEqual(largest_prime_factor(66), 2)
        self.assertEqual(largest_prime_factor(67), 2)
        self.assertEqual(largest_prime_factor(68), 2)
        self.assertEqual(largest_prime_factor(69), 2)
        self.assertEqual(largest_prime_factor(70), 2)
        self.assertEqual(largest_prime_factor(71), 2)
        self.assertEqual(largest_prime_factor(72), 2)
        self.assertEqual(largest_prime_factor(73), 2