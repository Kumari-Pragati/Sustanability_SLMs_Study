Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
        self.assertEqual(is_bored("I am tired. I am hungry. I need to sleep."), 3)

    def test_no_sentences(self):
        self.assertEqual(is_bored(""), 0)

    def test_sentences_with_punctuation(self):
        self.assertEqual(is_bored("I am excited! I can't wait. I'm going to the park."), 3)

    def test_sentences_with_whitespace(self):
        self.assertEqual(is_bored("I am here.   I am waiting."), 2)

    def test_sentences_with_uppercase(self):
        self.assertEqual(is_bored("I am here. I am WAITING."), 2)

    def test_sentences_with_numbers(self):
        self.assertEqual(is_bored("I have 3 apples. I have 2 oranges."), 2)

    def test_sentences_with_special_characters(self):
        self.assertEqual(is_bored("I am here! I am waiting..."), 2)

if __name__ == '__main__':
    unittest.main()