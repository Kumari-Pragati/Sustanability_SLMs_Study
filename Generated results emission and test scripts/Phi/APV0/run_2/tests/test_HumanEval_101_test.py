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
    return s_list.split()

 import unittest
from HumanEval_101_code import words_string

class TestWordsString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(words_string(""), [])

    def test_string_with_commas(self):
        self.assertEqual(words_string("Hi, my name is John"), ["Hi", "my", "name", "is", "John"])

    def test_string_with_spaces(self):
        self.assertEqual(words_string("One two three four five six"), ["One", "two", "three", "four", "five", "six"])

    def test_string_with_mixed_separators(self):
        self.assertEqual(words_string("Hello, world! How are you?"), ["Hello", "world", "!", "How", "are", "you"])

    def test_string_with_no_separators(self):
        self.assertEqual(words_string("Test"), ["Test"])

    def test_string_with_special_characters(self):
        self.assertEqual(words_string("Python3.6!@#"), ["Python3", ".", "6", "!", "@", "#"])

    def test_string_with_leading_and_trailing_spaces(self):
        self.assertEqual(words_string("  Hello, world!  "), ["Hello", "world", "!"])

    def test_string_with_multiple_spaces(self):
        self.assertEqual(words_string("Hello    world"), ["Hello", "world"])

if __name__ == '__main__':
    unittest.main()