You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_117_code import select_words

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    result = []
    for word in s.split():
        n_consonants = 0
        for i in range(0, len(word)):
            if word[i].lower() not in ["a", "e", "i", "o", "u"]:
                n_consonants += 1
        if n_consonants == n:
            result.append(word)
    return result


### Response:
Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_117_code import select_words

class TestSelectWords(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(select_words("", 0), [])

    def test_no_matching_words(self):
        self.assertEqual(select_words("simple white space", 2), [])

    def test_one_matching_word(self):
        self.assertEqual(select_words("Hello world", 4), ["world"])

    def test_multiple_matching_words(self):
        self.assertEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])

    def test_one_matching_word_with_different_case(self):
        self.assertEqual(select_words("Uncle sam", 3), ["Uncle"])

    def test_one_matching_word_with_consonants(self):
        self.assertEqual(select_words("consonants in word", 4), ["consonants"])

    def test_multiple_matching_words_with_consonants(self):
        self.assertEqual(select_words("consonants in word and sentence", 4), ["consonants", "word", "sentence"])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios, including an empty string, no matching words, one matching word, multiple matching words, a word with different cases, words with consonants, and multiple words with consonants.