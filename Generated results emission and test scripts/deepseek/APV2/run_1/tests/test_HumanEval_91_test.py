You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given function:


import unittest
from HumanEval_91_code import is_bored

class TestIsBored(unittest.TestCase):

    def test_no_boredoms(self):
        self.assertEqual(is_bored("Hello world"), 0)
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)
        self.assertEqual(is_bored("I am bored. I am bored. I am bored."), 3)

    def test_with_boredoms(self):
        self.assertEqual(is_bored("I am bored. What about you?"), 1)
        self.assertEqual(is_bored("I am bored! I am bored. I am bored."), 3)
        self.assertEqual(is_bored("I am bored. I am bored. I am bored! I am bored."), 4)

    def test_empty_string(self):
        self.assertEqual(is_bored(""), 0)

    def test_no_sentences(self):
        self.assertEqual(is_bored("No sentences here"), 0)

    def test_only_boredoms(self):
        self.assertEqual(is_bored("I am bored. I am bored. I am bored."), 3)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

- When there are no boredoms.
- When there are boredoms.
- When the input string is empty.
- When there are no sentences.
- When all sentences are boredoms.

Each test checks that the function returns the correct number of boredoms in a given string.