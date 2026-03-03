You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given function:


import unittest
from HumanEval_44_code import change_base

class TestChangeBase(unittest.TestCase):

    def test_change_base(self):
        self.assertEqual(change_base(8, 3), '22')
        self.assertEqual(change_base(8, 2), '1000')
        self.assertEqual(change_base(7, 2), '111')
        self.assertEqual(change_base(10, 10), '10')
        self.assertEqual(change_base(0, 2), '0')
        self.assertEqual(change_base(15, 16), 'F')
        self.assertEqual(change_base(255, 16), 'FF')
        self.assertEqual(change_base(1023, 8), '777')
        self.assertEqual(change_base(1023, 10), '1023')
        self.assertEqual(change_base(1023, 2), '1111111111')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different inputs and checks if the output matches the expected result. It covers a range of cases, including edge cases like 0 and numbers that are powers of the base.