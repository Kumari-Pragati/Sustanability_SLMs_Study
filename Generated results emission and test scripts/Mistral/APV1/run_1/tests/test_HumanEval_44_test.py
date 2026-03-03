You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the `change_base` function:


import unittest
from HumanEval_44_code import change_base

class TestChangeBase(unittest.TestCase):

    def test_change_base_positive(self):
        self.assertEqual(change_base(8, 3), '22')
        self.assertEqual(change_base(8, 2), '1000')
        self.assertEqual(change_base(7, 2), '111')
        self.assertEqual(change_base(10, 3), '1111')
        self.assertEqual(change_base(15, 2), '11111')
        self.assertEqual(change_base(25, 5), '2')
        self.assertEqual(change_base(100, 8), '12')
        self.assertEqual(change_base(1023, 3), '22102')
        self.assertEqual(change_base(1023, 2), '10000010101')

    def test_change_base_zero(self):
        self.assertEqual(change_base(0, 3), '0')
        self.assertEqual(change_base(0, 2), '0')
        self.assertEqual(change_base(0, 5), '0')
        self.assertEqual(change_base(0, 8), '0')

    def test_change_base_negative(self):
        self.assertEqual(change_base(-8, 3), '-22')
        self.assertEqual(change_base(-8, 2), '-1000')
        self.assertEqual(change_base(-7, 2), '-111')

    def test_change_base_base_out_of_range(self):
        with self.assertRaises(ValueError):
            change_base(10, 10)
        with self.assertRaises(ValueError):
            change_base(10, 11)
        with self.assertRaises(ValueError):
            change_base(10, 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes positive test cases, test cases for zero input, negative input, and edge cases where the base is out of range (less than 2 or greater than or equal to 10). The test cases are organized in separate methods for better readability and maintainability.