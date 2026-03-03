system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return s_list.split()


assistant

import unittest

# Function to be tested
from HumanEval_101_code import words_string

class TestWordsString(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(words_string(""), [])

    def test_single_word(self):
        self.assertEqual(words_string("Hello"), ["Hello"])

    def test_multiple_words_separated_by_comma(self):
        self.assertEqual(words_string("apple, banana, cherry"), ["apple", "banana", "cherry"])

    def test_multiple_words_separated_by_space(self):
        self.assertEqual(words_string("apple  banana cherry"), ["apple", "banana", "cherry"])

    def test_mixed_delimiters(self):
        self.assertEqual(words_string("apple, banana cherry, date"), ["apple", "banana", "cherry", "date"])

    def test_all_spaces(self):
        self.assertEqual(words_string("   "), [])

    def test_all_commas(self):
        self.assertEqual(words_string(",,,,"), [])

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and includes the necessary code snippet as per your requirements. It also defines a class `TestWordsString` that inherits from `unittest.TestCase`. Each method within this class tests a specific case using assertions provided by `unittest`. The `if __name__ == '__main__':` block ensures that the script can be run directly without needing to import it first.