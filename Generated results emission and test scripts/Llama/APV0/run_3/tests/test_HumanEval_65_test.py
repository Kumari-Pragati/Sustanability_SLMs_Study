user

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
        return s[len(s) - shift:] + s[:len(s) - shift]assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_65_code import circular_shift

class TestCircularShift(unittest.TestCase):

    def test_circular_shift(self):
        self.assertEqual(circular_shift(12, 1), "21")
        self.assertEqual(circular_shift(12, 2), "12")
        self.assertEqual(circular_shift(123, 1), "213")
        self.assertEqual(circular_shift(123, 2), "132")
        self.assertEqual(circular_shift(123, 3), "321")
        self.assertEqual(circular_shift(123, 4), "123")
        self.assertEqual(circular_shift(123, 5), "321")
        self.assertEqual(circular_shift(123, 6), "123")
        self.assertEqual(circular_shift(123, 7), "321")
        self.assertEqual(circular_shift(123, 8), "123")
        self.assertEqual(circular_shift(123, 9), "321")
        self.assertEqual(circular_shift(123, 10), "123")
        self.assertEqual(circular_shift(123456, 1), "2345671")
        self.assertEqual(circular_shift(123456, 2), "123456")
        self.assertEqual(circular_shift(123456, 3), "654321")
        self.assertEqual(circular_shift(123456, 4), "123456")
        self.assertEqual(circular_shift(123456, 5), "654321")
        self.assertEqual(circular_shift(123456, 6), "123456")
        self.assertEqual(circular_shift(123456, 7), "654321")
        self.assertEqual(circular_shift(123456, 8), "123456")
        self.assertEqual(circular_shift(123456, 9), "654321")
        self.assertEqual(circular_shift(123456, 10), "123456")
        self.assertEqual(circular_shift(123456, 11), "654321")
        self.assertEqual(circular_shift(123456, 12), "123456")
        self.assertEqual(circular_shift(123456, 13), "654321")
        self.assertEqual(circular_shift(123456, 14), "123456")
        self.assertEqual(circular_shift(123456, 15), "654321")
        self.assertEqual(circular_shift(123456, 16), "123456")
        self.assertEqual(circular_shift(123456, 17), "654321")
        self.assertEqual(circular_shift(123456, 18), "123456")
        self.assertEqual(circular_shift(123456, 19), "654321")
        self.assertEqual(circular_shift(123456, 20), "123456")
        self.assertEqual(circular_shift(123456, 21), "654321")
        self.assertEqual(circular_shift(123456, 22), "123456")
        self.assertEqual(circular_shift(123456, 23), "654321")
        self.assertEqual(circular_shift(123456, 24), "123456")
        self.assertEqual(circular_shift(123456, 25), "654321")
        self.assertEqual(circular_shift(123456, 26), "123456")
        self.assertEqual(circular_shift(123456, 27), "654321")
        self.assertEqual(circular_shift(123456, 28), "123456")
        self.assertEqual(circular_shift(123456, 29), "654321")
        self.assertEqual(circular_shift(123456, 30), "123456")
        self.assertEqual(circular_shift(123456, 31), "654321")
        self.assertEqual(circular_shift(123456, 32), "123456")
        self.assertEqual(circular_shift(123456, 33), "654321")
        self.assertEqual(circular_shift(123456, 34), "123456")
        self.assertEqual(circular_shift(123456, 35), "654321")
        self.assertEqual(circular_shift(123456, 36), "123456")
        self.assertEqual(circular_shift(123456, 37), "654321")
        self.assertEqual(circular_shift(123456, 38), "123456")
        self.assertEqual(circular_shift(123456, 39), "654321")
        self.assertEqual(circular_shift(123456, 40), "123456")
        self.assertEqual(circular_shift(123456, 41), "654321")
        self.assertEqual(circular_shift(123456, 42), "123456")
        self.assertEqual(circular_shift(123456, 43), "654321")
        self.assertEqual(circular_shift(123456, 44), "123456")
        self.assertEqual(circular_shift(123456, 45), "654321")
        self.assertEqual(circular_shift(123456, 46), "123456")
        self.assertEqual(circular_shift(123456, 47), "654321")