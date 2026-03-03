user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return timesassistant

Here is the unittest test script for the `how_many_times` function:

import unittest
from HumanEval_18_code import how_many_times

class TestHowManyTimes(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_char(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_multiple_chars(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_no_match(self):
        self.assertEqual(how_many_times('hello', 'abc'), 0)

    def test_overlap(self):
        self.assertEqual(how_many_times('abcabc', 'abc'), 2)

    def test_edge_case(self):
        self.assertEqual(how_many_times('a', 'a'), 1)

    def test_substring_empty(self):
        self.assertEqual(how_many_times('hello', ''), 1)

    def test_substring_longer_than_string(self):
        self.assertEqual(how_many_times('hello', 'world'), 0)

if __name__ == '__main__':
    unittest.main()

This script defines a `TestHowManyTimes` class that contains seven test methods:

1. `test_empty_string`: Tests that the function returns 0 when the input string is empty.
2. `test_single_char`: Tests that the function returns the correct count when the substring is a single character.
3. `test_multiple_chars`: Tests that the function returns the correct count when the substring is multiple characters.
4. `test_no_match`: Tests that the function returns 0 when the substring is not found in the input string.
5. `test_overlap`: Tests that the function counts overlapping occurrences of the substring.
6. `test_edge_case`: Tests that the function handles edge cases correctly (e.g., when the substring is the same as the input string).
7. `test_substring_empty`: Tests that the function returns 1 when the substring is empty.
8. `test_substring_longer_than_string`: Tests that the function returns 0 when the substring is longer than the input string.

Each test method uses the `assertEqual` method to verify that the output of the `how_many_times` function matches the expected result.

To run the tests, simply execute the script. The `unittest` module will automatically discover and run the test methods.