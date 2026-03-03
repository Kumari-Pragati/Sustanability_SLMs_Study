You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is a complete unittest test suite for the `split_words` function:


import unittest
from HumanEval_125_code import split_words

class TestSplitWords(unittest.TestCase):

    def test_split_on_whitespace(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])
        self.assertEqual(split_words("   Hello world!   "), ["Hello", "world!"])

    def test_split_on_comma(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])
        self.assertEqual(split_words("Hello,,world!"), ["Hello", "", "world!"])

    def test_split_on_odd_letters(self):
        self.assertEqual(split_words("abcdef"), 3)
        self.assertEqual(split_words("zyxwvut"), 5)
        self.assertEqual(split_words("qwertyuiop"), 0)

    def test_empty_string(self):
        self.assertEqual(split_words(""), 0)

    def test_single_letter(self):
        self.assertEqual(split_words("a"), 0)
        self.assertEqual(split_words("A"), 0)
        self.assertEqual(split_words("z"), 0)

    def test_single_odd_letter(self):
        self.assertEqual(split_words("b"), 1)
        self.assertEqual(split_words("c"), 1)
        self.assertEqual(split_words("e"), 1)
        self.assertEqual(split_words("o"), 1)
        self.assertEqual(split_words("i"), 1)
        self.assertEqual(split_words("u"), 1)
        self.assertEqual(split_words("y"), 1)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as splitting on whitespace, splitting on commas, splitting on odd letters, handling empty strings, and single letters.