You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

    def test_split_words_with_no_lowercase_odd_order_letters(self):
        self.assertEqual(split_words("ABCDEF"), 0)

    def test_split_words_with_lowercase_odd_order_letters(self):
        self.assertEqual(split_words("aBcdeF"), 3)

    def test_split_words_with_mixed_case_and_whitespace(self):
        self.assertEqual(split_words("Hello World!"), ["Hello", "World!"])

    def test_split_words_with_mixed_case_and_commas(self):
        self.assertEqual(split_words("Hello,World!"), ["Hello", "World!"])

    def test_split_words_with_mixed_case_and_no_whitespace_or_commas(self):
        self.assertEqual(split_words("aBcdeF"), 3)

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios for the `split_words` function, including cases with whitespace, commas, and no whitespace or commas. It also tests the function's behavior when encountering lowercase letters with odd order in the alphabet. The test cases are designed to ensure that the function behaves as expected in each scenario.