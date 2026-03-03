You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the `count_distinct_characters` function:


import unittest
from HumanEval_16_code import count_distinct_characters

class TestCountDistinctCharacters(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(''), 0)

    def test_single_character(self):
        self.assertEqual(count_distinct_characters('a'), 1)
        self.assertEqual(count_distinct_characters('A'), 1)

    def test_multiple_characters(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)
        self.assertEqual(count_distinct_characters('12345'), 5)
        self.assertEqual(count_distinct_characters('!@#$%^&*()'), 10)

    def test_special_characters(self):
        self.assertEqual(count_distinct_characters('!@#$%^&*()'), 10)
        self.assertEqual(count_distinct_characters('abc!@#$%^&*()'), 11)

    def test_punctuation_only(self):
        self.assertEqual(count_distinct_characters('!@#$%^&*()'), 10)

    def test_whitespace(self):
        self.assertEqual(count_distinct_characters(' '), 1)
        self.assertEqual(count_distinct_characters('  '), 1)
        self.assertEqual(count_distinct_characters(' abc  '), 5)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios such as an empty string, single characters, multiple characters, special characters, punctuation only, and whitespace.