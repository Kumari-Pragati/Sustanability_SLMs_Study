You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_125_code import split_words

class TestSplitWords(unittest.TestCase):

    def test_split_words_with_space(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_split_words_with_comma(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_split_words_with_no_space_or_comma(self):
        self.assertEqual(split_words("abcdef"), 3)

    def test_split_words_with_only_space(self):
        self.assertEqual(split_words("Hello   world!"), ["Hello", "world!"])

    def test_split_words_with_only_comma(self):
        self.assertEqual(split_words("Hello,,world!"), ["Hello", "world!"])

    def test_split_words_with_mixed_space_and_comma(self):
        self.assertEqual(split_words("Hello, world!"), ["Hello", "world!"])

    def test_split_words_with_lowercase_letters(self):
        self.assertEqual(split_words("abcdefghijklmnopqrstuvwxyz"), 13)

    def test_split_words_with_uppercase_letters(self):
        self.assertEqual(split_words("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 0)

    def test_split_words_with_mixed_case_letters(self):
        self.assertEqual(split_words("AbCdEfGhIjKlMnOpQrStUvWxYz"), 13)

    def test_split_words_with_special_characters(self):
        self.assertEqual(split_words("!@#$%^&*()"), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios, including:

- Text with spaces
- Text with commas
- Text with no spaces or commas
- Text with only spaces
- Text with only commas
- Text with a mix of spaces and commas
- Text with all lowercase letters
- Text with all uppercase letters
- Text with a mix of lowercase and uppercase letters
- Text with special characters

Each test checks that the output of the `split_words` function matches the expected result.