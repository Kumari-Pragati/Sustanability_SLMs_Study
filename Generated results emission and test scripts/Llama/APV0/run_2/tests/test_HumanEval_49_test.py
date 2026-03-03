user

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
    return retassistant

Here is the unittest test script for the `modp` function:

import unittest
from HumanEval_49_code import modp

class TestModp(unittest.TestCase):
    def test_modp(self):
        # Test cases
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(3, 11), 8)
        self.assertEqual(modp(100, 101), 1)

        # Edge cases
        self.assertEqual(modp(1, 2), 2)
        self.assertEqual(modp(2, 2), 0)
        self.assertEqual(modp(0, 2), 1)
        self.assertEqual(modp(1, 1), 1)

        # Large inputs
        self.assertEqual(modp(10000, 101), 1)
        self.assertEqual(modp(20000, 101), 1)

if __name__ == '__main__':
    unittest.main()

This script defines a `TestModp` class that contains several test methods. Each test method uses the `assertEqual` method to check that the output of the `modp` function matches the expected result for a given input.

The test cases cover a variety of scenarios, including:

* The original test cases provided in the function docstring
* Edge cases, such as `n=1`, `n=2`, and `p=1`
* Large inputs to ensure that the function works correctly for large values of `n`

You can run this script directly using Python, and it will execute the tests and report any failures or errors.