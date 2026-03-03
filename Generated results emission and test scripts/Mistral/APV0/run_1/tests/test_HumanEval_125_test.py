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

 Here is a unittest test script for the `split_words` function:


import unittest
from HumanEval_125_code import split_words

class TestSplitWords(unittest.TestCase):

    def test_split_on_whitespace(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])
        self.assertEqual(split_words("   Hello world!   "), ["Hello", "world!"])

    def test_split_on_comma(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])
        self.assertEqual(split_words("a,b,c,d,e"), ["a", "b", "c", "d", "e"])

    def test_split_on_odd_letters(self):
        self.assertEqual(split_words("abcdef"), 3)
        self.assertEqual(split_words("zyxwvuts"), 5)
        self.assertEqual(split_words("qwertyuiop"), 0)

if __name__ == '__main__':
    unittest.main()


This test script includes three test cases:

1. Testing the function when the input string contains whitespace and the expected output is a list of words split on whitespace.
2. Testing the function when the input string contains commas and the expected output is a list of words split on commas.
3. Testing the function when the input string does not contain whitespace or commas, and the expected output is the number of lower-case letters with even order in the alphabet.

You can run this test script by saving it as a .py file and running it using the command `python filename.py` in your terminal.