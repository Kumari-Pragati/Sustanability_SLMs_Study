You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
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


### Response:
Here is a unittest test suite for the given function:


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
        self.assertEqual(split_words(", , ,"), [])

    def test_split_words_with_lowercase_letters(self):
        self.assertEqual(split_words("a,b,c,d,e,f"), ["a", "b", "c", "d", "e", "f"])

    def test_split_words_with_uppercase_letters(self):
        self.assertEqual(split_words("A,B,C,D,E,F"), ["A", "B", "C", "D", "E", "F"])

    def test_split_words_with_mixed_case_letters(self):
        self.assertEqual(split_words("a,B,c,D,e,F"), ["a", "B", "c", "D", "e", "F"])

    def test_split_words_with_special_characters(self):
        self.assertEqual(split_words("a,b,c,d,e,f!"), ["a", "b", "c", "d", "e", "f"])

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to cover all possible scenarios for the `split_words` function.