You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function `count_distinct_characters`. The test cases cover edge cases, empty strings, and strings with special characters.


import unittest
from HumanEval_16_code import count_distinct_characters

class TestCountDistinctCharacters(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(''), 0)

    def test_single_character(self):
        self.assertEqual(count_distinct_characters('a'), 1)
        self.assertEqual(count_distinct_characters('A'), 1)

    def test_multiple_characters(self):
        self.assertEqual(count_distinct_characters('abc'), 3)
        self.assertEqual(count_distinct_characters('ABC'), 3)
        self.assertEqual(count_distinct_characters('123'), 3)
        self.assertEqual(count_distinct_characters('!@#$%^&*()'), 10)

    def test_case_insensitive(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('jErRy'), 4)

    def test_special_characters(self):
        self.assertEqual(count_distinct_characters('!@#$%^&*()'), 10)
        self.assertEqual(count_distinct_characters('abc!@#$%^&*()'), 13)

if __name__ == '__main__':
    unittest.main()


This test suite includes 6 test cases covering various scenarios such as empty strings, single characters, multiple characters, case-insensitive strings, and strings with special characters.