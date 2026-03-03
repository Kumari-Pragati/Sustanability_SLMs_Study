Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_16_code import count_distinct_characters
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    return len(set(string.lower()))

 import unittest
from HumanEval_16_code import count_distinct_characters

class TestCountDistinctCharacters(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(''), 0)

    def test_single_character(self):
        self.assertEqual(count_distinct_characters('a'), 1)

    def test_multiple_characters(self):
        self.assertEqual(count_distinct_characters('abc'), 3)

    def test_case_insensitive(self):
        self.assertEqual(count_distinct_characters('ABC'), 1)
        self.assertEqual(count_distinct_characters('aBc'), 1)

    def test_repeated_characters(self):
        self.assertEqual(count_distinct_characters('aabbcc'), 3)
        self.assertEqual(count_distinct_characters('AABBC'), 3)

    def test_special_characters(self):
        self.assertEqual(count_distinct_characters('!@#$%^&*()'), 10)

    def test_whitespace(self):
        self.assertEqual(count_distinct_characters('   '), 0)
        self.assertEqual(count_distinct_characters('   '), 0)

if __name__ == '__main__':
    unittest.main()