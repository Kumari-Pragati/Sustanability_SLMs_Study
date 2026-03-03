You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_101_code import words_string

class TestWordsString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(words_string(""), [])

    def test_single_word(self):
        self.assertEqual(words_string("Hello"), ["Hello"])

    def test_multiple_words_with_commas(self):
        self.assertEqual(words_string("Hello,World,Python"), ["Hello", "World", "Python"])

    def test_multiple_words_with_spaces(self):
        self.assertEqual(words_string("Hello World Python"), ["Hello", "World", "Python"])

    def test_multiple_words_with_both_commas_and_spaces(self):
        self.assertEqual(words_string("Hello, World, Python"), ["Hello", "World", "Python"])

    def test_multiple_words_with_trailing_comma(self):
        self.assertEqual(words_string("Hello,World,Python,"), ["Hello", "World", "Python"])

    def test_multiple_words_with_leading_comma(self):
        self.assertEqual(words_string(",Hello,World,Python"), ["Hello", "World", "Python"])

    def test_multiple_words_with_leading_and_trailing_comma(self):
        self.assertEqual(words_string(",Hello,World,Python,"), ["Hello", "World", "Python"])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios such as an empty string, a string with a single word, a string with multiple words separated by commas, a string with multiple words separated by spaces, a string with multiple words separated by both commas and spaces, a string with trailing comma, a string with leading comma, and a string with leading and trailing comma.