You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_18_code import how_many_times

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def how_many_times(string: str, substring: str) -> int:
    """Find how many times a given substring can be found in the original string. Count overlapping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    times = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            times += 1
    return times

 import unittest
from HumanEval_18_code import how_many_times

class TestHowManyTimes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_character_substring(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_multiple_occurrences(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_no_occurrences(self):
        self.assertEqual(how_many_times('abcdef', 'xyz'), 0)

    def test_overlapping_occurrences(self):
        self.assertEqual(how_many_times('aaabaaa', 'aa'), 3)

    def test_substring_longer_than_string(self):
        self.assertEqual(how_many_times('abc', 'abcd'), 0)

    def test_substring_empty(self):
        self.assertEqual(how_many_times('abc', ''), 0)

    def test_substring_same_as_string(self):
        self.assertEqual(how_many_times('aaa', 'aaa'), 1)

    def test_substring_not_found(self):
        self.assertEqual(how_many_times('abc', 'ab'), 0)

if __name__ == '__main__':
    unittest.main()