system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Function to be tested
from HumanEval_18_code import how_many_times

class TestHowManyTimes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_char_substring(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_multiple_occurrences(self):
        self.assertEqual(how_many_times('ababa', 'aba'), 2)

    def test_overlapping_substrings(self):
        self.assertEqual(how_many_times('hello', 'l'), 2)

    def test_case_insensitive(self):
        self.assertEqual(how_many_times('Hello World!', 'o'), 2)

    def test_edge_cases(self):
        self.assertEqual(how_many_times('', ''), 0)
        self.assertEqual(how_many_times('abcde', ''), 0)
        self.assertEqual(how_many_times('abcde', 'fgh'), 0)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestHowManyTimes` class that inherits from `unittest.TestCase`. It contains several test methods to verify different scenarios of the `how_many_times` function. The `assertEqual` method checks if the output of the function matches the expected result. If any test fails, it will raise an assertion error and print the failure message.