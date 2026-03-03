user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

Here is the unittest test script for the given Python function:

Python
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
        expected_output = "this is"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_empty_sentence(self):
        sentence = ""
        expected_output = ""
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_sentence_with_prime_length_words(self):
        sentence = "hello world 3 test"
        expected_output = "hello world 3 test"
        self.assertEqual(words_in_sentence(sentence), expected_output)

    def test_sentence_with_non_prime_length_words(self):
        sentence = "hello world 4 test"
        expected_output = "hello world test"
        self.assertEqual(words_in_sentence(sentence), expected_output)

if __name__ == '__main__':
    unittest.main()


This script includes 7 test cases to cover different scenarios:

- Test example 1 and 2 to ensure the function works correctly for the given examples.
- Test a single word to ensure the function doesn't modify the word if its length is prime.
- Test multiple words to ensure the function works correctly for sentences with multiple words.
- Test an empty sentence to ensure the function returns an empty string.
- Test a sentence with prime length words to ensure the function doesn't modify the words.
- Test a sentence with non-prime length words to ensure the function filters out the words with non-prime lengths.