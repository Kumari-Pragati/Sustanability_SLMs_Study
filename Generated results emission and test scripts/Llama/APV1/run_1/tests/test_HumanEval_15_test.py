user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_15_code import string_sequence

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 up to n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return''.join(str(x) for x in range(n + 1))assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_15_code import string_sequence

class TestStringSequence(unittest.TestCase):

    def test_string_sequence_zero(self):
        self.assertEqual(string_sequence(0), '0')

    def test_string_sequence_one(self):
        self.assertEqual(string_sequence(1), '0 1')

    def test_string_sequence_five(self):
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')

    def test_string_sequence_negative(self):
        with self.assertRaises(ValueError):
            string_sequence(-1)

    def test_string_sequence_non_integer(self):
        with self.assertRaises(TypeError):
            string_sequence('a')

    def test_string_sequence_large(self):
        self.assertEqual(string_sequence(100), '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the following scenarios:

- Test the function with a zero input
- Test the function with a one input
- Test the function with a five input
- Test the function with a negative input (should raise a ValueError)
- Test the function with a non-integer input (should raise a TypeError)
- Test the function with a large input