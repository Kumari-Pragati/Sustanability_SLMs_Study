system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest
from HumanEval_91_code import is_bored

class TestIsBored(unittest.TestCase):

    def test_is_bored(self):
        self.assertEqual(is_bored("Hello world"), 0)
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)
        self.assertEqual(is_bored("I am bored. I have nothing to do."), 1)
        self.assertEqual(is_bored("I'm not bored at all!"), 0)
        self.assertEqual(is_bored(""), 0)
        self.assertEqual(is_bored("I like eating pizza. Pizza is my favorite food."), 1)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestIsBored` class that inherits from `unittest.TestCase`. It contains a single method `test_is_bored`, which tests various cases using assertions to ensure the `is_bored` function works as expected. The `assertEqual` methods compare the output of `is_bored` against the expected results, ensuring the function behaves correctly under different conditions.