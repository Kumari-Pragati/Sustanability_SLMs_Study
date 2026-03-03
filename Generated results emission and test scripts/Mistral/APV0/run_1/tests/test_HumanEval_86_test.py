Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_86_code import anti_shuffle
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string is a string where all words (separated by space)
    are replaced by a new word where all the characters are arranged in
    ascending order based on ASCII value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """

    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])

 Here is a unittest test script for the `anti_shuffle` function:


import unittest
from HumanEval_86_code import anti_shuffle

class TestAntiShuffle(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(anti_shuffle(''), '')

    def test_single_word(self):
        self.assertEqual(anti_shuffle('Hi'), 'Hi')
        self.assertEqual(anti_shuffle('hello'), 'ehllo')
        self.assertEqual(anti_shuffle('World'), 'dlorlW')

    def test_multiple_words(self):
        self.assertEqual(anti_shuffle('Hello World!!!'), 'Hello !!!Wdlor')
        self.assertEqual(anti_shuffle('This is a test'), 'This is atse')
        self.assertEqual(anti_shuffle('The quick brown fox jumps over the lazy dog'), 'The qibck brown fox jumps over the dgolazy l')

    def test_punctuation(self):
        self.assertEqual(anti_shuffle('Hello, World!'), 'Hello, !Wldo')
        self.assertEqual(anti_shuffle('Hello!'), 'Hello!')
        self.assertEqual(anti_shuffle('Hello?'), 'Hello?')

    def test_special_characters(self):
        self.assertEqual(anti_shuffle('Hello@World'), 'Hello@Wldo')
        self.assertEqual(anti_shuffle('Hello$World'), 'Hello$Wldo')
        self.assertEqual(anti_shuffle('Hello%World'), 'Hello%Wldo')

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as an empty string, single words, multiple words, punctuation, and special characters. It uses the `assertEqual` method to verify the expected and actual outputs.