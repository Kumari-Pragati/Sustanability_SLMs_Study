system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


assistant

import unittest

# Provided function to be tested
from HumanEval_86_code import anti_shuffle

class TestAntiShuffle(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(anti_shuffle(""), "")

    def test_single_word(self):
        self.assertEqual(anti_shuffle("Hi"), "Hi")

    def test_multiple_words(self):
        self.assertEqual(anti_shuffle("hello world!"), "ehllo dlor!")

    def test_with_numbers(self):
        self.assertEqual(anti_shuffle("Hello 123 World!"), "Hello dlro W123!")

    def test_with_punctuation(self):
        self.assertEqual(anti_shuffle("Hello, World!"), "Hello, !dlrow!")

    def test_with_special_characters(self):
        self.assertEqual(anti_shuffle("Special @#$%^&*() Characters"), "Special &^%$#@!cHters")

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to ensure the `anti_shuffle` function behaves as expected across different scenarios, including empty strings, single-word strings, multiple-word strings, numbers, punctuation, and special characters.