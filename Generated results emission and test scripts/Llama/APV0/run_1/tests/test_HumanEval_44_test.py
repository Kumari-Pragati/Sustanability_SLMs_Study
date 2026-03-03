user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_44_code import change_base
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return retassistant

Here is the unittest test script for the `change_base` function:

import unittest
from HumanEval_44_code import change_base

class TestChangeBase(unittest.TestCase):
    def test_change_base(self):
        # Test cases
        self.assertEqual(change_base(8, 3), '22')
        self.assertEqual(change_base(8, 2), '1000')
        self.assertEqual(change_base(7, 2), '111')
        self.assertEqual(change_base(10, 2), '1010')
        self.assertEqual(change_base(15, 8), '17')
        self.assertEqual(change_base(20, 5), '40')
        self.assertEqual(change_base(1, 10), '1')
        self.assertEqual(change_base(0, 10), '0')

        # Edge cases
        self.assertEqual(change_base(0, 0), '')  # Base 0 is not allowed
        self.assertEqual(change_base(10, 0), '')  # Base 0 is not allowed

    def test_invalid_input(self):
        # Test invalid inputs
        with self.assertRaises(TypeError):
            change_base('a', 2)
        with self.assertRaises(TypeError):
            change_base(8, 'a')
        with self.assertRaises(ValueError):
            change_base(8, 11)  # Base > 10 is not allowed

if __name__ == '__main__':
    unittest.main()

This script defines a `TestChangeBase` class that contains two test methods:

* `test_change_base`: This method tests the `change_base` function with various input values and expected output values. It covers both valid and edge cases.
* `test_invalid_input`: This method tests the `change_base` function with invalid input values, such as non-integer inputs, non-integer bases, and bases greater than 10. It uses the `assertRaises` method to verify that the function raises the expected exceptions.

The script can be run directly using the `unittest` module, and it will report any failures or errors.