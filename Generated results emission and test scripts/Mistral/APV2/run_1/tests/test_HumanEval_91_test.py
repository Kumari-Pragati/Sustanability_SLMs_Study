You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the `is_bored` function:


import unittest
from HumanEval_91_code import is_bored

class TestIsBored(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(is_bored(""), 0)

    def test_single_word(self):
        self.assertEqual(is_bored("Hello"), 0)
        self.assertEqual(is_bored("World"), 0)

    def test_multiple_words(self):
        self.assertEqual(is_bored("The sky is blue"), 0)
        self.assertEqual(is_bored("The sun is shining"), 0)
        self.assertEqual(is_bored("I love this weather"), 1)

    def test_sentence_with_punctuation(self):
        self.assertEqual(is_bored("I'm bored. I'm tired."), 2)
        self.assertEqual(is_bored("I'm not bored! I'm happy."), 1)
        self.assertEqual(is_bored("I'm not bored? I'm curious."), 1)

    def test_multiple_boredoms(self):
        self.assertEqual(is_bored("I'm bored. I'm tired. I'm hungry."), 3)
        self.assertEqual(is_bored("I'm bored. I'm tired! I'm hungry."), 3)
        self.assertEqual(is_bored("I'm bored? I'm tired. I'm hungry!"), 2)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as an empty string, single words, multiple words, sentences with punctuation, and multiple boredoms in a single string.