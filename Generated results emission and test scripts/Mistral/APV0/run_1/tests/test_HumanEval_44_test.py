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

 Here is a unittest test script for the `change_base` function:


import unittest
from HumanEval_44_code import change_base

class TestChangeBase(unittest.TestCase):

    def test_change_base(self):
        self.assertEqual(change_base(8, 3), '22')
        self.assertEqual(change_base(8, 2), '1000')
        self.assertEqual(change_base(7, 2), '111')
        self.assertEqual(change_base(10, 3), '12')
        self.assertEqual(change_base(15, 2), '1111')
        self.assertEqual(change_base(25, 5), '2')
        self.assertEqual(change_base(0, 2), '0')
        self.assertEqual(change_base(-1, 2), '11')
        self.assertEqual(change_base(100, 7), '136')
        self.assertEqual(change_base(200, 8), '144')

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the given examples in the function documentation, as well as additional test cases to ensure the function works correctly for various inputs, including negative numbers and large numbers.