You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_91_code import is_bored

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """

    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence.startswith('I ') for sentence in sentences if sentence)


### Response:
Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_91_code import is_bored

class TestIsBored(unittest.TestCase):

    def test_no_boredoms(self):
        self.assertEqual(is_bored("Hello world"), 0)
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)
        self.assertEqual(is_bored("I am bored. I love to play. I am happy"), 2)
        self.assertEqual(is_bored("I am bored. I love to play. I am happy. I am tired"), 3)

    def test_with_boredoms(self):
        self.assertEqual(is_bored("I am bored. I love to play. I am happy. I am tired. I miss you"), 5)
        self.assertEqual(is_bored("I am bored. I love to play. I am happy. I am tired. I miss you. I am sad"), 6)

    def test_empty_string(self):
        self.assertEqual(is_bored(""), 0)

    def test_no_sentences(self):
        self.assertEqual(is_bored(" "), 0)

    def test_single_boredom(self):
        self.assertEqual(is_bored("I am bored."), 1)

    def test_multiple_boredoms(self):
        self.assertEqual(is_bored("I am bored. I am bored. I am bored."), 3)

    def test_boredoms_with_different_delimiters(self):
        self.assertEqual(is_bored("I am bored! I am bored? I am bored."), 3)

    def test_boredoms_with_non_starting_words(self):
        self.assertEqual(is_bored("You are bored. I am bored. He is bored."), 1)

    def test_boredoms_with_non_bored_sentences(self):
        self.assertEqual(is_bored("You are bored. He is bored. She is bored."), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure that the `is_bored` function is working correctly. It tests with and without boredoms, with empty strings, with strings with no sentences, with single boredoms, with multiple boredoms, and with boredoms with different delimiters. It also tests with sentences that do not start with "I" and with sentences that are not boredoms.