You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is a complete unittest test suite for the `change_base` function:


import unittest
from HumanEval_44_code import change_base

class TestChangeBase(unittest.TestCase):
    def test_change_base(self):
        self.assertEqual(change_base(8, 3), '22')
        self.assertEqual(change_base(8, 2), '1000')
        self.assertEqual(change_base(7, 2), '111')
        self.assertEqual(change_base(10, 3), '2')
        self.assertEqual(change_base(15, 2), '1111')
        self.assertEqual(change_base(24, 4), '3f')
        self.assertEqual(change_base(100, 8), '124')
        self.assertEqual(change_base(255, 16), 'ff')
        self.assertEqual(change_base(1023, 3), '1001001')
        self.assertEqual(change_base(4095, 5), '100101')

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover different base numbers and input values. The `TestChangeBase` class inherits from `unittest.TestCase` and contains a single method `test_change_base` that tests the `change_base` function. The `assertEqual` method is used to compare the expected and actual results.