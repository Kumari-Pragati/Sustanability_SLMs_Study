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
    return ret

 import unittest
from HumanEval_44_code import change_base

class TestChangeBase(unittest.TestCase):

    def test_change_base_to_3(self):
        self.assertEqual(change_base(8, 3), '22')

    def test_change_base_to_2(self):
        self.assertEqual(change_base(8, 2), '1000')

    def test_change_base_to_2_with_smaller_number(self):
        self.assertEqual(change_base(7, 2), '111')

    def test_change_base_with_zero(self):
        self.assertEqual(change_base(0, 3), '0')

    def test_change_base_with_negative_number(self):
        with self.assertRaises(ValueError):
            change_base(-1, 3)

    def test_change_base_with_base_greater_than_10(self):
        with self.assertRaises(ValueError):
            change_base(8, 11)

if __name__ == '__main__':
    unittest.main()