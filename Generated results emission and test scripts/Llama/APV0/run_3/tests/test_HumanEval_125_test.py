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
    alphabet, ord('a') = 0, ord('b') = 1,... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(',','').split()
    else:
        return len([i for i in txt if i.islower() and ord(i) % 2 == 0])assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_125_code import split_words

class TestSplitWords(unittest.TestCase):

    def test_split_words_with_spaces(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_split_words_with_commas(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_split_words_with_no_spaces_or_commas(self):
        self.assertEqual(split_words("abcdef"), 3)

    def test_split_words_with_mixed_case(self):
        self.assertEqual(split_words("HelloWorld!"), ["Hello", "World!"])

    def test_split_words_with_numbers(self):
        self.assertEqual(split_words("Hello123world!"), ["Hello", "world!"])

    def test_split_words_with_punctuation(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_split_words_with_empty_string(self):
        self.assertEqual(split_words(""), [])

    def test_split_words_with_single_word(self):
        self.assertEqual(split_words("Hello"), ["Hello"])

    def test_split_words_with_multiple_spaces(self):
        self.assertEqual(split_words("Hello   world!"), ["Hello", "world!"])

    def test_split_words_with_commas_and_spaces(self):
        self.assertEqual(split_words("Hello, world!"), ["Hello", "world!"])

if __name__ == '__main__':
    unittest.main()


This script includes 9 test cases to cover different scenarios, including:

- Test cases for strings with spaces, commas, and no separators
- Test cases for strings with mixed case, numbers, and punctuation
- Test cases for empty strings, single words, and multiple spaces
- Test cases for strings with commas and spaces

Each test case uses the `assertEqual` method to compare the output of the `split_words` function with the expected result.