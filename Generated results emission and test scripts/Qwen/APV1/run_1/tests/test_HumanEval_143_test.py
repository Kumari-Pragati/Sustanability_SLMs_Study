system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_143_code import words_in_sentence

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    new_lst = []
    for word in sentence.split():
        flg = 0
        if len(word) == 1:
            flg = 1
        for i in range(2, len(word)):
            if len(word) % i == 0:
                flg = 1
        if flg == 0 or len(word) == 2:
            new_lst.append(word)
    return " ".join(new_lst)


assistant

import unittest

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test class for the words_in_sentence function
class TestWordsInSentence(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(words_in_sentence("This is a test"), "is")

    def test_example_2(self):
        self.assertEqual(words_in_sentence("lets go for swimming"), "go for")

    def test_empty_string(self):
        self.assertEqual(words_in_sentence(""), "")

    def test_single_letter_words(self):
        self.assertEqual(words_in_sentence("a"), "")
        self.assertEqual(words_in_sentence("aa"), "")
        self.assertEqual(words_in_sentence("aaa"), "")

    def test_multiple_letters_words(self):
        self.assertEqual(words_in_sentence("hello world"), "")
        self.assertEqual(words_in_sentence("helloworld"), "")
        self.assertEqual(words_in_sentence("helloworldworld"), "")

    def test_large_input(self):
        large_sentence = "The quick brown fox jumps over the lazy dog"
        expected_output = "quick brown fox jumps over the lazy dog"
        self.assertEqual(words_in_sentence(large_sentence), expected_output)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestWordsInSentence` class that inherits from `unittest.TestCase`. It includes several test methods to verify the correctness of the `words_in_sentence` function under different conditions. The `is_prime` helper function checks whether a number is prime. The tests cover various scenarios including single-letter words, multiple-letter words, empty strings, and larger input sentences.