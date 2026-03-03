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

 import unittest
from HumanEval_125_code import split_words

class TestSplitWords(unittest.TestCase):

    def test_split_words_with_whitespace(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_split_words_with_commas(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_split_words_with_no_whitespace_or_commas(self):
        self.assertEqual(split_words("abcdef"), 3)

    def test_split_words_with_only_lowercase_letters(self):
        self.assertEqual(split_words("hello"), 5)

    def test_split_words_with_mixed_case_letters(self):
        self.assertEqual(split_words("HelloWorld"), 5)

    def test_split_words_with_uppercase_letters(self):
        self.assertEqual(split_words("HelloWorld"), 5)

    def test_split_words_with_numbers(self):
        self.assertEqual(split_words("Hello123"), 5)

    def test_split_words_with_special_characters(self):
        self.assertEqual(split_words("Hello!@#"), 5)

    def test_split_words_with_whitespace_and_commas(self):
        self.assertEqual(split_words("Hello, world!"), ["Hello", "world!"])

    def test_split_words_with_whitespace_and_numbers(self):
        self.assertEqual(split_words("Hello 123"), 3)

    def test_split_words_with_whitespace_and_special_characters(self):
        self.assertEqual(split_words("Hello!@#"), 3)

    def test_split_words_with_commas_and_numbers(self):
        self.assertEqual(split_words("Hello,123"), 3)

    def test_split_words_with_commas_and_special_characters(self):
        self.assertEqual(split_words("Hello,!@#"), 3)

    def test_split_words_with_whitespace_and_commas_and_numbers(self):
        self.assertEqual(split_words("Hello, 123"), 3)

    def test_split_words_with_whitespace_and_commas_and_special_characters(self):
        self.assertEqual(split_words("Hello!,@#"), 3)

if __name__ == '__main__':
    unittest.main()