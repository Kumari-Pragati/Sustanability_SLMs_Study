user

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
    return s_list.split()assistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_101_code import words_string

class TestWordsString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(words_string(""), [])

    def test_single_word(self):
        self.assertEqual(words_string("Hello"), ["Hello"])

    def test_multiple_words(self):
        self.assertEqual(words_string("Hi, my name is John"), ["Hi", "my", "name", "is", "John"])

    def test_multiple_words_with_spaces(self):
        self.assertEqual(words_string("One two three four five six"), ["One", "two", "three", "four", "five", "six"])

    def test_multiple_words_with_commas(self):
        self.assertEqual(words_string("One, two, three, four, five, six"), ["One", "two", "three", "four", "five", "six"])

    def test_multiple_words_with_spaces_and_commas(self):
        self.assertEqual(words_string("One, two, three, four, five, six"), ["One", "two", "three", "four", "five", "six"])

    def test_string_with_punctuation(self):
        self.assertEqual(words_string("Hello, world!"), ["Hello", "world"])

    def test_string_with_leading_and_trailing_spaces(self):
        self.assertEqual(words_string("   Hello, world!   "), ["Hello", "world"])

    def test_string_with_leading_and_trailing_commas(self):
        self.assertEqual(words_string(",,Hello, world,,,"), ["Hello", "world"])

    def test_string_with_leading_and_trailing_spaces_and_commas(self):
        self.assertEqual(words_string(",,   Hello, world,  ,,,"), ["Hello", "world"])

if __name__ == '__main__':
    unittest.main()


This test suite covers a variety of test cases, including:

- An empty string
- A single word
- Multiple words separated by spaces
- Multiple words separated by commas
- Multiple words separated by both spaces and commas
- A string with punctuation
- A string with leading and trailing spaces
- A string with leading and trailing commas
- A string with leading and trailing spaces and commas