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

 import unittest
from HumanEval_16_code import count_distinct_characters

class TestCountDistinctCharacters(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(''), 0)

    def test_single_character(self):
        self.assertEqual(count_distinct_characters('a'), 1)

    def test_all_same_characters(self):
        self.assertEqual(count_distinct_characters('aaaa'), 1)

    def test_case_insensitive(self):
        self.assertEqual(count_distinct_characters('ABCabc'), 3)

    def test_multiple_distinct_characters(self):
        self.assertEqual(count_distinct_characters('Jerry'), 4)
        self.assertEqual(count_distinct_characters('HelloWorld'), 8)

    def test_special_characters(self):
        self.assertEqual(count_distinct_characters('!@#$%^&*()'), 10)

    def test_whitespace(self):
        self.assertEqual(count_distinct_characters('   '), 0)

    def test_unicode_characters(self):
        self.assertEqual(count_distinct_characters('éèêë'), 4)

if __name__ == '__main__':
    unittest.main()