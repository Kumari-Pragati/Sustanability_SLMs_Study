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
    return ' '.join(str(x) for x in range(n + 1))

 Here is a comprehensive unittest test suite for the `string_sequence` function:


import unittest
from HumanEval_15_code import string_sequence

class TestStringSequence(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(string_sequence(0), '0')

    def test_positive_numbers(self):
        self.assertEqual(string_sequence(1), '0')
        self.assertEqual(string_sequence(2), '0 1')
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')
        self.assertEqual(string_sequence(10), '0 1 2 3 4 5 6 7 8 9 10')

    def test_negative_numbers(self):
        self.assertEqual(string_sequence(-1), '')
        self.assertEqual(string_sequence(-2), '')
        self.assertEqual(string_sequence(-5), '')
        self.assertEqual(string_sequence(-10), '')

    def test_large_numbers(self):
        self.assertEqual(string_sequence(1000), '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 1000')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various edge cases, such as zero, positive numbers, negative numbers, and large numbers. It also includes a test for the empty string when a negative number is passed.