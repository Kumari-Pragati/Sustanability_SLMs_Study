system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

# Provided function to be tested
from HumanEval_143_code import words_in_sentence

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

    def test_two_letter_words(self):
        self.assertEqual(words_in_sentence("ab"), "")
        self.assertEqual(words_in_sentence("ba"), "")
        self.assertEqual(words_in_sentence("aba"), "")

    def test_prime_length_words(self):
        self.assertEqual(words_in_sentence("apple"), "ppl")
        self.assertEqual(words_in_sentence("banana"), "anana")
        self.assertEqual(words_in_sentence("cherry"), "hery")

    def test_mixed_case(self):
        self.assertEqual(words_in_sentence("Hello World!"), "llo Wrd!")

    def test_multiple_spaces(self):
        self.assertEqual(words_in_sentence("   "), "")
        self.assertEqual(words_in_sentence("   hello world!   "), "hello world!")

    def test_special_characters(self):
        self.assertEqual(words_in_sentence("Hello@World!"), "elloWorl!")
        self.assertEqual(words_in_sentence("Hello-World!"), "elloWorl!")

if __name__ == '__main__':
    unittest.main()


This unittest test suite includes various test cases to ensure the `words_in_sentence` function behaves correctly under different conditions, including edge cases such as empty strings, single-letter words, two-letter words, prime-length words, mixed case, multiple spaces, and special characters.