system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
    return " ".join(new_lst)assistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_143_code import words_in_sentence

class TestWordsInSentence(unittest.TestCase):

    def test_example1(self):
        sentence = "This is a test"
        expected_output = "is"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_example2(self):
        sentence = "lets go for swimming"
        expected_output = "go for"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_single_word(self):
        sentence = "hello"
        expected_output = "hello"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_multiple_words(self):
        sentence = "hello world this is a test"
        expected_output = "hello this is a"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_empty_sentence(self):
        sentence = ""
        expected_output = ""
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_sentence_with_no_prime_length_words(self):
        sentence = "abc def ghi"
        expected_output = "abc def"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_sentence_with_all_prime_length_words(self):
        sentence = "a b c d e f g"
        expected_output = "a b c d e f g"
        self.assertEqual(words_in_sentence(sentence), expected_output)

if __name__ == '__main__':
    unittest.main()