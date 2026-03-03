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

 import unittest
from HumanEval_44_code import change_base

class TestChangeBase(unittest.TestCase):

    def test_base_3(self):
        self.assertEqual(change_base(8, 3), '22')

    def test_base_2(self):
        self.assertEqual(change_base(8, 2), '1000')

    def test_base_7(self):
        self.assertEqual(change_base(7, 2), '111')

    def test_base_10(self):
        self.assertEqual(change_base(10, 10), '10')

    def test_base_negative(self):
        with self.assertRaises(ValueError):
            change_base(10, -1)

    def test_base_zero(self):
        with self.assertRaises(ValueError):
            change_base(10, 0)

    def test_base_greater_than_10(self):
        with self.assertRaises(ValueError):
            change_base(10, 11)

    def test_base_zero_input(self):
        with self.assertRaises(ValueError):
            change_base(0, 10)

if __name__ == '__main__':
    unittest.main()