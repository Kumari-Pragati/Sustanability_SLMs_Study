You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

class TestModpFunction(unittest.TestCase):

    def test_modp_positive_exponents(self):
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(3, 11), 8)
        self.assertEqual(modp(100, 101), 1)

    def test_modp_negative_exponents(self):
        self.assertEqual(modp(-1, 5), 1)
        self.assertEqual(modp(-2, 101), 1)
        self.assertEqual(modp(-3, 11), 3)

    def test_modp_zero_exponent(self):
        self.assertEqual(modp(0, 5), 1)
        self.assertEqual(modp(0, 101), 1)

    def test_modp_large_exponents(self):
        self.assertEqual(modp(1000, 101), 1)
        self.assertEqual(modp(10000, 101), 1)

    def test_modp_small_exponents(self):
        self.assertEqual(modp(1, 5), 2)
        self.assertEqual(modp(1, 101), 2)

    def test_modp_edge_cases(self):
        self.assertEqual(modp(10, 1), 0)
        self.assertEqual(modp(10, 2), 0)
        self.assertEqual(modp(10, 3), 2)
        self.assertEqual(modp(10, 4), 4)
        self.assertEqual(modp(10, 5), 3)

if __name__ == '__main__':
    unittest.main()