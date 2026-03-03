Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_65_code import circular_shift
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]

 Here is a unittest test script for the `circular_shift` function:


import unittest
from HumanEval_65_code import circular_shift

class TestCircularShift(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(circular_shift(12, 1), "21")
        self.assertEqual(circular_shift(123, 2), "312")
        self.assertEqual(circular_shift(1024, 3), "4201")
        self.assertEqual(circular_shift(999, 4), "999")

    def test_zero(self):
        self.assertEqual(circular_shift(0, 1), "0")
        self.assertEqual(circular_shift(0, 2), "0")

    def test_negative_shift(self):
        self.assertEqual(circular_shift(12, -1), "2")
        self.assertEqual(circular_shift(123, -2), "31")
        self.assertEqual(circular_shift(1024, -3), "402")

    def test_shift_equal_to_length(self):
        self.assertEqual(circular_shift(123, 3), "321")
        self.assertEqual(circular_shift(1024, 10), "4201")

    def test_large_numbers(self):
        self.assertEqual(circular_shift(123456789, 1), "34567891")
        self.assertEqual(circular_shift(123456789, 10), "912345678")

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as basic usage, zero values, negative shifts, shifts equal to the length, and large numbers. It also includes a test for the edge case where the shift is greater than the number of digits, which is handled by returning the digits reversed.