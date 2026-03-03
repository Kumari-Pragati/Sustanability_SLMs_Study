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

 Here is a comprehensive unittest test suite for the `split_words` function:


import unittest
from HumanEval_125_code import split_words

class TestSplitWords(unittest.TestCase):

    def test_split_on_whitespace(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])
        self.assertEqual(split_words("   Hello world!   "), ["Hello", "world!"])
        self.assertEqual(split_words("   "), [])

    def test_split_on_comma(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])
        self.assertEqual(split_words("Hello,,world!"), ["Hello", "", "world!"])
        self.assertEqual(split_words(","), [])

    def test_split_on_odd_letters(self):
        self.assertEqual(split_words("abcdef"), 3)
        self.assertEqual(split_words("abcd"), 1)
        self.assertEqual(split_words("z"), 0)
        self.assertEqual(split_words("a"), 1)
        self.assertEqual(split_words(""), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_split_on_whitespace` checks if the function correctly splits the input string on whitespace.
2. `test_split_on_comma` checks if the function correctly splits the input string on commas.
3. `test_split_on_odd_letters` checks if the function correctly returns the number of lower-case letters with odd order in the alphabet when there are no whitespaces or commas in the input string.