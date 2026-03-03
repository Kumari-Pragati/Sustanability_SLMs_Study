system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_125_code import split_words
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(',', ' ').split()
    else:
        return len([i for i in txt if i.islower() and ord(i) % 2 == 0])


assistant

import unittest

# Function to be tested
from HumanEval_125_code import split_words

class TestSplitWords(unittest.TestCase):

    def test_split_whitespace(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_split_comma(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_no_spaces_or_commas(self):
        self.assertEqual(split_words("abcdef"), 3)

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines a test case class `TestSplitWords`. It includes three test methods (`test_split_whitespace`, `test_split_comma`, and `test_no_spaces_or_commas`) that call the `split_words` function with different inputs and assert the expected outputs. The `unittest.main()` at the end runs all tests when this script is executed.