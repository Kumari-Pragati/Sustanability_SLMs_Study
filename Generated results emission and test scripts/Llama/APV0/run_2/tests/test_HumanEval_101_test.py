user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

Here is the unittest test script for the given Python function:

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

    def test_multiple_words_with_punctuation(self):
        self.assertEqual(words_string("One, two, three, four, five, six"), ["One", "two", "three", "four", "five", "six"])

    def test_multiple_words_with_punctuation_and_spaces(self):
        self.assertEqual(words_string("One, two, three, four, five, six, seven, eight, nine, ten"), ["One", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"])

    def test_string_with_leading_and_trailing_spaces(self):
        self.assertEqual(words_string("   Hi, my name is John   "), ["Hi", "my", "name", "is", "John"])

    def test_string_with_leading_and_trailing_punctuation(self):
        self.assertEqual(words_string("!, Hi, my name is John,!"), ["Hi", "my", "name", "is", "John"])

if __name__ == '__main__':
    unittest.main()


This script includes 6 test cases to cover different scenarios:

- An empty string
- A single word
- Multiple words with commas
- Multiple words with commas and spaces
- Multiple words with commas, spaces, and punctuation
- A string with leading and trailing spaces and punctuation