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

 Here is a unittest test script for the `modp` function:


import unittest
from HumanEval_49_code import modp

class TestModP(unittest.TestCase):

    def test_modp(self):
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(3, 11), 8)
        self.assertEqual(modp(100, 101), 1)
        self.assertEqual(modp(0, 10), 0)
        self.assertEqual(modp(10, 10), 10)
        self.assertEqual(modp(2147483647, 10), 5)
        self.assertEqual(modp(-1, 5), 4)
        self.assertEqual(modp(10, -5), 4)
        self.assertEqual(modp(-10, -5), 1)

if __name__ == '__main__':
    unittest.main()


This test script includes additional test cases to cover edge cases such as negative numbers, large numbers, and numbers greater than the modulus. Make sure to save this script as a .py file and run it using the command `python3 test_modp.py` or `pytest test_modp.py` if you have pytest installed.