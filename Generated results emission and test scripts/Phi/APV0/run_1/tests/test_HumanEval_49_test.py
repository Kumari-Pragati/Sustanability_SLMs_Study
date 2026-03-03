Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

    def test_modp_positive_integers(self):
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(3, 11), 8)
        self.assertEqual(modp(100, 101), 1)

    def test_modp_edge_cases(self):
        self.assertEqual(modp(1, 1), 1)
        self.assertEqual(modp(0, 0), 0)
        self.assertEqual(modp(-1, 1), 0)
        self.assertEqual(modp(-1, 2), 1)

    def test_modp_large_numbers(self):
        # Test with large numbers to check for potential overflow issues
        self.assertEqual(modp(1000, 1000000007), 1000)
        self.assertEqual(modp(1000000000, 1000000007), 1000000000)

    def test_modp_zero_input(self):
        # Test with zero input
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(100, 0), 0)

    def test_modp_negative_input(self):
        # Test with negative input
        self.assertEqual(modp(-1, 101), 1)
        self.assertEqual(modp(-1, 2), 1)

if __name__ == '__main__':
    unittest.main()