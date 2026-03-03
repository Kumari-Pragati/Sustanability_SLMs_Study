You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a Python unittest test suite for the given function:


import unittest
from HumanEval_143_code import words_in_sentence

class TestWordsInSentence(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(words_in_sentence("This is a test"), "is")

    def test_example2(self):
        self.assertEqual(words_in_sentence("lets go for swimming"), "go for")

    def test_single_letter_word(self):
        self.assertEqual(words_in_sentence("a b c d e"), "a b c d e")

    def test_non_prime_length_words(self):
        self.assertEqual(words_in_sentence("apple orange banana"), "apple banana")

    def test_empty_sentence(self):
        self.assertEqual(words_in_sentence(""), "")

    def test_long_sentence(self):
        self.assertEqual(words_in_sentence("this is a test sentence with multiple words"), "is test sentence with")

    def test_sentence_with_numbers(self):
        self.assertEqual(words_in_sentence("this is 123 a test"), "is a test")

    def test_sentence_with_special_characters(self):
        self.assertEqual(words_in_sentence("this is a test!@#"), "is a test")

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios such as single letter words, words with non-prime lengths, empty sentences, long sentences, sentences with numbers, and sentences with special characters. It checks if the function returns the correct output for each of these scenarios.