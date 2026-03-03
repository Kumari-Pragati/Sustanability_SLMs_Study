user

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
    return retassistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_49_code import modp

class TestModpFunction(unittest.TestCase):

    def test_modp_with_small_numbers(self):
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(3, 11), 8)
        self.assertEqual(modp(100, 101), 1)

    def test_modp_with_large_numbers(self):
        self.assertEqual(modp(100000, 101), 1)
        self.assertEqual(modp(200000, 101), 1)
        self.assertEqual(modp(300000, 101), 1)

    def test_modp_with_edge_cases(self):
        self.assertEqual(modp(-1, 101), 1)
        self.assertEqual(modp(-100, 101), 1)
        self.assertEqual(modp(1000000, 101), 1)

    def test_modp_with_invalid_input(self):
        with self.assertRaises(TypeError):
            modp('a', 101)
        with self.assertRaises(TypeError):
            modp(100, 'a')
        with self.assertRaises(TypeError):
            modp('a', 'b')

if __name__ == '__main__':
    unittest.main()


This test suite includes four test methods:

- `test_modp_with_small_numbers`: Tests the function with small numbers.
- `test_modp_with_large_numbers`: Tests the function with large numbers.
- `test_modp_with_edge_cases`: Tests the function with edge cases (negative numbers, large numbers, etc.).
- `test_modp_with_invalid_input`: Tests the function with invalid input (non-integer numbers, non-integer modulus, etc.).

Each test method uses the `assertEqual` method to check if the output of the function is as expected. The `assertRaises` method is used to test the function with invalid input.