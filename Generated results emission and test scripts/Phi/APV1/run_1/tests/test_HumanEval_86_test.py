You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 import unittest
from HumanEval_86_code import anti_shuffle

class TestAntiShuffle(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(anti_shuffle(''), '')

    def test_single_word(self):
        self.assertEqual(anti_shuffle('Hi'), 'Hi')
        self.assertEqual(anti_shuffle('hello'), 'ehllo')

    def test_multiple_words(self):
        self.assertEqual(anti_shuffle('Hello World!!!'), 'Hello !!!Wdlor')
        self.assertEqual(anti_shuffle('Python is fun'), 'Phno !s i n')

    def test_special_characters(self):
        self.assertEqual(anti_shuffle('Hello, World!'), 'Hello , !Wdlor')
        self.assertEqual(anti_shuffle('Python3.8'), '3.8nopty')

    def test_case_sensitivity(self):
        self.assertEqual(anti_shuffle('Hello World'), 'Hello World')
        self.assertEqual(anti_shuffle('hello world'), 'ehllo dlorw')

    def test_whitespace(self):
        self.assertEqual(anti_shuffle('   '), '   ')
        self.assertEqual(anti_shuffle('  Hello World  '), '  Hello !Wdlor  ')

if __name__ == '__main__':
    unittest.main()