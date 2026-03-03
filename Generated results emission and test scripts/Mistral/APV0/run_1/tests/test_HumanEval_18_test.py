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
    return times

 Here is a unittest test script for the `how_many_times` function:


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
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)
        self.assertEqual(how_many_times('banana', 'ana'), 3)

    def test_substring_not_found(self):
        self.assertEqual(how_many_times('apple', 'pear'), 0)
        self.assertEqual(how_many_times('abcdefgh', 'ijk'), 0)

    def test_substring_at_beginning(self):
        self.assertEqual(how_many_times('aa', 'a'), 2)
        self.assertEqual(how_many_times('banana', 'ana'), 1)

    def test_substring_at_end(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)
        self.assertEqual(how_many_times('banana', 'ana'), 1)

    def test_substring_in_middle(self):
        self.assertEqual(how_many_times('aaabbb', 'abb'), 2)
        self.assertEqual(how_many_times('bananabana', 'ana'), 2)

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases to ensure the function works correctly for different scenarios, such as an empty string, single character strings, multiple occurrences, substring not found, substring at the beginning, substring at the end, and substring in the middle.