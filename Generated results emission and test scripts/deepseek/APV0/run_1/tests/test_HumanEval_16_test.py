You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_16_code import count_distinct_characters

class TestCountDistinctCharacters(unittest.TestCase):

    def test_all_lowercase(self):
        self.assertEqual(count_distinct_characters('abc'), 3)

    def test_all_uppercase(self):
        self.assertEqual(count_distinct_characters('ABC'), 3)

    def test_mixed_case(self):
        self.assertEqual(count_distinct_characters('AbC'), 3)

    def test_repeated_characters(self):
        self.assertEqual(count_distinct_characters('aabbcc'), 3)

    def test_single_character(self):
        self.assertEqual(count_distinct_characters('a'), 1)

    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(''), 0)

    def test_special_characters(self):
        self.assertEqual(count_distinct_characters('!@#$%^&*()'), 10)

    def test_whitespace(self):
        self.assertEqual(count_distinct_characters(' '), 1)

    def test_string_with_whitespace(self):
        self.assertEqual(count_distinct_characters('Hello World'), 2)

if __name__ == '__main__':
    unittest.main()


This script tests the function with different types of inputs, including all lowercase, all uppercase, mixed case, repeated characters, single character, empty string, special characters, whitespace, and strings with whitespace. The expected results are also provided.