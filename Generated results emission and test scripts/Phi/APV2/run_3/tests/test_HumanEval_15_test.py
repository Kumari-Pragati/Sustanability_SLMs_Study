You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 import unittest
from HumanEval_15_code import string_sequence

class TestStringSequence(unittest.TestCase):

    def test_string_sequence_zero(self):
        self.assertEqual(string_sequence(0), '0')

    def test_string_sequence_positive(self):
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')

    def test_string_sequence_negative(self):
        with self.assertRaises(ValueError):
            string_sequence(-1)

    def test_string_sequence_large_number(self):
        self.assertEqual(string_sequence(100), '0 1 2 3 4 ... 99 100')

if __name__ == '__main__':
    unittest.main()