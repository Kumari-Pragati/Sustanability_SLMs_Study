You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_91_code import is_bored

class TestIsBored(unittest.TestCase):

    def test_no_boredoms(self):
        self.assertEqual(is_bored("Hello world"), 0)
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)

    def test_with_boredoms(self):
        self.assertEqual(is_bored("I am bored. What should I do?"), 1)
        self.assertEqual(is_bored("I am bored! Can you help me?"), 1)
        self.assertEqual(is_bored("I am bored. I am bored! I am bored?"), 3)

    def test_empty_string(self):
        self.assertEqual(is_bored(""), 0)

    def test_no_sentences(self):
        self.assertEqual(is_bored(" "), 0)

    def test_single_boredom(self):
        self.assertEqual(is_bored("I am bored."), 1)

    def test_multiple_boredoms(self):
        self.assertEqual(is_bored("I am bored. I am bored. I am bored."), 3)

    def test_boredoms_with_other_words(self):
        self.assertEqual(is_bored("You are bored. I am bored."), 1)

if __name__ == '__main__':
    unittest.main()


This script includes several test cases to ensure that the function is working correctly. It tests the function with different types of inputs, including:

- No boredoms
- With boredoms
- Empty string
- No sentences
- Single boredom
- Multiple boredoms
- Boredoms with other words

Each test case checks that the function's output matches the expected output. If the function's output does not match the expected output, the test case will fail.