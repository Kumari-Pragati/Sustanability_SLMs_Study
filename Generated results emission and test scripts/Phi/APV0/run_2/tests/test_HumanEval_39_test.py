Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_39_code import prime_fib
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    import math

    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, min(int(math.sqrt(p)) + 1, p - 1)):
            if p % k == 0:
                return False
        return True

    f = [0, 1]
    while True:
        f.append(f[-1] + f[-2])
        if is_prime(f[-1]):
            n -= 1
        if n == 0:
            return f[-1]

 import unittest
from HumanEval_39_code import prime_fib

class TestPrimeFib(unittest.TestCase):

    def test_prime_fib_1(self):
        self.assertEqual(prime_fib(1), 2)

    def test_prime_fib_2(self):
        self.assertEqual(prime_fib(2), 3)

    def test_prime_fib_3(self):
        self.assertEqual(prime_fib(3), 5)

    def test_prime_fib_4(self):
        self.assertEqual(prime_fib(4), 13)

    def test_prime_fib_5(self):
        self.assertEqual(prime_fib(5), 89)

    def test_prime_fib_6(self):
        self.assertEqual(prime_fib(6), 233)

    def test_prime_fib_7(self):
        self.assertEqual(prime_fib(7), 1597)

    def test_prime_fib_8(self):
        self.assertEqual(prime_fib(8), 28657)

    def test_prime_fib_9(self):
        self.assertEqual(prime_fib(9), 514229)

    def test_prime_fib_10(self):
        self.assertEqual(prime_fib(10), 433494437)

    def test_prime_fib_11(self):
        self.assertEqual(prime_fib(11), 297121461)

    def test_prime_fib_12(self):
        self.assertEqual(prime_fib(12), 8626375709452795)

    def test_prime_fib_13(self):
        self.assertEqual(prime_fib(13), 28257526403710639)

    def test_prime_fib_14(self):
        self.assertEqual(prime_fib(14), 8626757127220303)

    def test_prime_fib_15(self):
        self.assertEqual(prime_fib(15), 4831308975912269)

    def test_prime_fib_16(self):
        self.assertEqual(prime_fib(16), 2005994029607079)

    def test_prime_fib_17(self):
        self.assertEqual(prime_fib(17), 99194853094755497)

    def test_prime_fib_18(self):
        self.assertEqual(prime_fib(18), 77787448707681395)

    def test_prime_fib_19(self):
        self.assertEqual(prime_fib(19), 6024282915587635)

    def test_prime_fib_20(self):
        self.assertEqual(prime_fib(20), 43149527688457750)

if __name__ == '__main__':
    unittest.main()