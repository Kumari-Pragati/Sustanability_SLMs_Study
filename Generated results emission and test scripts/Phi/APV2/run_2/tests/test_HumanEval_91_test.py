You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

 import unittest
from HumanEval_91_code import is_bored

class TestIsBored(unittest.TestCase):

    def test_no_boredoms(self):
        self.assertEqual(is_bored("Hello world"), 0)

    def test_single_boredom(self):
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)

    def test_multiple_boredom(self):
        self.assertEqual(is_bored("I am tired. I am hungry. I love this weather"), 3)

    def test_no_sentences(self):
        self.assertEqual(is_bored(""), 0)

    def test_empty_sentences(self):
        self.assertEqual(is_bored("I. I. I."), 3)

    def test_sentences_with_punctuation(self):
        self.assertEqual(is_bored("I am here. I am fine! I am ready."), 3)

    def test_sentences_with_whitespace(self):
        self.assertEqual(is_bored("I am here.   I am fine! I am ready."), 3)

    def test_sentences_with_no_boredom(self):
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I am not bored."), 0)

if __name__ == '__main__':
    unittest.main()