system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return s_list.split()


assistant

import unittest

from HumanEval_101_code import words_string

class TestWordsString(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(words_string(""), [])

    def test_single_word(self):
        self.assertEqual(words_string("Hello"), ["Hello"])

    def test_multiple_words_with_spaces(self):
        self.assertEqual(words_string("Hello World"), ["Hello", "World"])

    def test_multiple_words_with_commas(self):
        self.assertEqual(words_string("Hello, World!"), ["Hello", "World"])

    def test_mixed_delimiters(self):
        self.assertEqual(words_string("Hello, world! This is a test."), 
                         ["Hello", ",", "world", "! ", "This", "is", "a", "test", "."])

    def test_large_number_of_words(self):
        self.assertEqual(words_string("The quick brown fox jumps over the lazy dog"),
                         ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"])

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestWordsString` class that inherits from `unittest.TestCase`. It contains several test methods to verify the correctness of the `words_string` function. The tests cover various scenarios including empty input, single word, multiple words with spaces, multiple words with commas, mixed delimiters, and large numbers of words. If you run this script directly (i.e., without importing it as a module), it will execute all the defined tests using the built-in `unittest.main()` method.