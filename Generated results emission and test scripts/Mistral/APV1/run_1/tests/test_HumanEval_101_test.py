You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_101_code import words_string

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """

    if not s:
        return []

    s_list = []

    for letter in s:
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)

    s_list = "".join(s_list)
    return s_list.split()

 Here is a comprehensive unittest test suite for the `words_string` function:


import unittest
from HumanEval_101_code import words_string

class TestWordsString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(words_string(""), [])

    def test_single_word(self):
        self.assertEqual(words_string("Hello"), ["Hello"])

    def test_multiple_words(self):
        self.assertEqual(words_string("Hi, my name is John"), ["Hi", "my", "name", "is", "John"])

    def test_commas_and_spaces(self):
        self.assertEqual(words_string("One, two, three, four, five, six"), ["One", "two", "three", "four", "five", "six"])

    def test_leading_trailing_spaces(self):
        self.assertEqual(words_string("   Hi, my name is John   "), ["Hi", "my", "name", "is", "John"])

    def test_punctuation(self):
        self.assertEqual(words_string("Hi!, my name is John."), ["Hi", "my", "name", "is", "John"])

    def test_special_characters(self):
        self.assertEqual(words_string("Hi#, my name is John%"), ["Hi", "my", "name", "is", "John"])

    def test_multiple_punctuation(self):
        self.assertEqual(words_string("Hi!, my name is John.?#"), ["Hi", "my", "name", "is", "John"])

if __name__ == '__main__':
    unittest.main()


This test suite includes various edge cases such as empty strings, single words, multiple words, commas and spaces, leading and trailing spaces, punctuation, multiple punctuation, and special characters. It ensures that the `words_string` function works correctly for all these cases.