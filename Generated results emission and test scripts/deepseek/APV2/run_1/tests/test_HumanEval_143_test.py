You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_143_code import words_in_sentence

class TestWordsInSentence(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(words_in_sentence("This is a test"), "is")

    def test_example_2(self):
        self.assertEqual(words_in_sentence("lets go for swimming"), "go for")

    def test_single_word(self):
        self.assertEqual(words_in_sentence("Python"), "Python")

    def test_two_words(self):
        self.assertEqual(words_in_sentence("hello world"), "hello")

    def test_prime_length_words(self):
        self.assertEqual(words_in_sentence("prime length words"), "prime length words")

    def test_empty_string(self):
        self.assertEqual(words_in_sentence(""), "")

    def test_long_sentence(self):
        self.assertEqual(words_in_sentence("this is a long sentence with some words of different lengths"), "is a with")

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the function with different types of input, including single words, words of prime length, and sentences with words of different lengths. It also includes a test for an empty string.

Please note that the function `words_in_sentence` is not provided in the question. I assumed it's in the file `HumanEval_143_code.py` and imported it. If it's in a different file, you need to adjust the import statement accordingly.

Also, the function `words_in_sentence` is not optimized for large inputs. It has a time complexity of O(n^2) because it checks for each word if it's a prime number by iterating from 2 to the length of the word. For a more efficient solution, you could use a precomputed list of prime numbers or a more efficient algorithm to check for prime numbers.