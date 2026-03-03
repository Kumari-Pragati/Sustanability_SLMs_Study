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

 Here is a comprehensive unittest test suite for the given Python function `how_many_times`. I've included a variety of test cases to ensure the function works correctly for different input scenarios.


import unittest
from HumanEval_18_code import how_many_times

class TestHowManyTimes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_char_string(self):
        self.assertEqual(how_many_times('a', 'a'), 1)
        self.assertEqual(how_many_times('b', 'a'), 0)

    def test_multiple_occurrences(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)
        self.assertEqual(how_many_times('ababab', 'ab'), 3)

    def test_substring_at_beginning(self):
        self.assertEqual(how_many_times('abcdef', 'abc'), 1)

    def test_substring_in_middle(self):
        self.assertEqual(how_many_times('abcdef', 'def'), 1)

    def test_substring_at_end(self):
        self.assertEqual(how_many_times('abcdef', 'ef'), 1)

    def test_substring_overlapping(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)
        self.assertEqual(how_many_times('abcabc', 'bc'), 2)

    def test_case_insensitive(self):
        self.assertEqual(how_many_times('AbCdEf', 'ab'), 1)
        self.assertEqual(how_many_times('AbCdEf', 'cD'), 1)

if __name__ == '__main__':
    unittest.main()


This test suite covers the following scenarios:

1. Empty string
2. Single character string
3. Multiple occurrences of the substring
4. Substring at the beginning, in the middle, and at the end of the string
5. Substring with overlapping cases
6. Case-insensitive substring matching

You can run the test suite by executing the script in your terminal or command prompt. If the function works correctly, all test cases should pass. If any test case fails, you'll see an error message indicating which test case failed and the expected and actual results.