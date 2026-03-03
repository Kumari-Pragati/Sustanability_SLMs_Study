You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is the unittest test script for the given Python function:


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

    def test_empty_substring(self):
        self.assertEqual(how_many_times('abc', ''), 3)

if __name__ == '__main__':
    unittest.main()


This script includes a test class `TestHowManyTimes` that inherits from `unittest.TestCase`. Each method in this class is a test case that tests a specific scenario. The `assertEqual` method is used to check if the output of the `how_many_times` function matches the expected result.

To run the tests, you can simply execute this script. If you're using a command line, you can do this by typing `python test_script.py` (replace `test_script.py` with the name of this file). If you're using an IDE, you can usually run the script by right-clicking on it and selecting "Run".

Please note that the `HumanEval_18_code` module and the `how_many_times` function should be defined in a separate file named `HumanEval_18_code.py` for this script to work.