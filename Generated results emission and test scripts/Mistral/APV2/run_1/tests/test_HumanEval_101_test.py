You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the `words_string` function:


import unittest
from HumanEval_101_code import words_string

class TestWordsString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(words_string(""), [])

    def test_single_word(self):
        self.assertEqual(words_string("Hello"), ["Hello"])

    def test_multiple_words_spaces(self):
        self.assertEqual(words_string("Hi there how are you"), ["Hi", "there", "how", "are", "you"])

    def test_multiple_words_commas(self):
        self.assertEqual(words_string("Hi, there, how, are, you"), ["Hi", "there", "how", "are", "you"])

    def test_multiple_words_spaces_and_commas(self):
        self.assertEqual(words_string("Hi, there, how are you"), ["Hi", "there", "how are you"])

    def test_leading_trailing_spaces(self):
        self.assertEqual(words_string("   Hi, there, how are you   "), ["Hi", "there", "how are you"])

    def test_punctuation(self):
        self.assertEqual(words_string("Hi, there! How are you?"), ["Hi", "there", "How are you"])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios such as an empty string, single word, multiple words separated by spaces, multiple words separated by commas, multiple words with both spaces and commas, leading and trailing spaces, and punctuation.