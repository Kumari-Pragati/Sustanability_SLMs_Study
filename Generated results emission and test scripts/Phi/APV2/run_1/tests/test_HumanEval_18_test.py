You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
        self.assertEqual(how_many_times('aaa', 'aa'), 2)

    def test_case_sensitivity(self):
        self.assertEqual(how_many_times('AaAa', 'a'), 2)

    def test_empty_substring(self):
        self.assertEqual(how_many_times('aaa', ''), 3)

    def test_substring_longer_than_string(self):
        self.assertEqual(how_many_times('aaa', 'aaa'), 1)

    def test_substring_longer_than_string_with_overlap(self):
        self.assertEqual(how_many_times('aaa', 'aaa'), 1)

if __name__ == '__main__':
    unittest.main()