You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
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


### Response:
Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_18_code import how_many_times

class TestHowManyTimes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_char_substring(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_double_char_substring(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_substring_not_in_string(self):
        self.assertEqual(how_many_times('abc', 'd'), 0)

    def test_substring_at_end_of_string(self):
        self.assertEqual(how_many_times('abcde', 'de'), 1)

    def test_substring_at_start_of_string(self):
        self.assertEqual(how_many_times('abcde', 'ab'), 1)

    def test_substring_in_middle_of_string(self):
        self.assertEqual(how_many_times('abcabc', 'bc'), 2)

    def test_substring_with_spaces(self):
        self.assertEqual(how_many_times('abc abc', 'abc'), 2)

    def test_substring_with_same_chars(self):
        self.assertEqual(how_many_times('abcabcabc', 'abc'), 3)

    def test_substring_with_same_chars_and_spaces(self):
        self.assertEqual(how_many_times('abc abc abc', 'abc'), 3)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various edge cases, such as an empty string, a single character substring, a double character substring, a substring not in the string, a substring at the end of the string, a substring at the start of the string, a substring in the middle of the string, a substring with spaces, a substring with the same characters, and a substring with the same characters and spaces.