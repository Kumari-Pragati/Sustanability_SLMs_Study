You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_49_code import modp

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret

 import unittest
from HumanEval_49_code import modp

class TestModPFunction(unittest.TestCase):

    def test_modp_positive_integers(self):
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(3, 11), 8)
        self.assertEqual(modp(100, 101), 1)

    def test_modp_edge_cases(self):
        self.assertEqual(modp(-1, 5), 1)
        self.assertEqual(modp(1, 5), 1)
        self.assertEqual(modp(0, 0), 1)

    def test_modp_large_numbers(self):
        self.assertEqual(modp(1000, 1000000007), 1000)
        self.assertEqual(modp(1000000000, 1000000007), 1000000000)

    def test_modp_zero_exponent(self):
        self.assertEqual(modp(0, 5), 1)

    def test_modp_zero_modulus(self):
        with self.assertRaises(ZeroDivisionError):
            modp(3, 0)

    def test_modp_negative_exponent(self):
        with self.assertRaises(ValueError):
            modp(1, -5)

    def test_modp_negative_modulus(self):
        with self.assertRaises(ValueError):
            modp(3, -5)

if __name__ == '__main__':
    unittest.main()