You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_125_code import split_words

class TestSplitWords(unittest.TestCase):
    def test_split_words_with_space(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_split_words_with_comma(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_split_words_with_no_space_or_comma(self):
        self.assertEqual(split_words("abcdef"), 3)

    def test_split_words_with_only_comma(self):
        self.assertEqual(split_words("a,b,c"), ["a", "b", "c"])

    def test_split_words_with_only_space(self):
        self.assertEqual(split_words("a b c"), ["a", "b", "c"])

    def test_split_words_with_no_letters(self):
        self.assertEqual(split_words("123456"), 0)

    def test_split_words_with_mixed_case(self):
        self.assertEqual(split_words("AbCdEf"), 3)

    def test_split_words_with_special_characters(self):
        self.assertEqual(split_words("!@#$%^&*()"), 0)

if __name__ == '__main__':
    unittest.main()


This script includes a test for each of the possible input scenarios as described in the function's docstring. It uses the `assertEqual` method to check that the function's output matches the expected output for each test case.

Please note that the function `split_words` should be in a file named `HumanEval_125_code.py` in the same directory as the unittest script for it to work.