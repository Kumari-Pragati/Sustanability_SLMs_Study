You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_101_code import words_string

class TestWordsString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(words_string(""), [])

    def test_single_word(self):
        self.assertEqual(words_string("Hello"), ["Hello"])

    def test_multiple_words(self):
        self.assertEqual(words_string("Hello, world"), ["Hello", "world"])

    def test_comma_separated_words(self):
        self.assertEqual(words_string("Hello, my, name, is, John"), ["Hello", "my", "name", "is", "John"])

    def test_space_separated_words(self):
        self.assertEqual(words_string("Hello world my name is John"), ["Hello", "world", "my", "name", "is", "John"])

    def test_mixed_comma_and_space_separated_words(self):
        self.assertEqual(words_string("Hello, world my, name is, John"), ["Hello", "world", "my", "name", "is", "John"])

if __name__ == '__main__':
    unittest.main()


This script creates a test class `TestWordsString` that inherits from `unittest.TestCase`. It includes several test methods to test the `words_string` function with different types of input. Each test method uses the `assertEqual` method to check if the output of the function matches the expected output.

Please note that the `words_string` function in the question is not correct. It replaces all commas with spaces, which is not the correct behavior. The correct function should split the string by either commas or spaces, not replace commas with spaces. Here is the correct function:


def words_string(s):
    if not s:
        return []
    return s.replace(',', '').split()


This function first replaces all commas with nothing (effectively removing them) and then splits the string by spaces.