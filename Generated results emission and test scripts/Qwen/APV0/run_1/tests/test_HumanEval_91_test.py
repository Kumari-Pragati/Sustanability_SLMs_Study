system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Function to be tested
from HumanEval_91_code import is_bored

class TestIsBored(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(is_bored(""), 0)

    def test_single_sentence(self):
        self.assertEqual(is_bored("Hello world"), 0)

    def test_multiple_sentences(self):
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)

    def test_sentence_with_I_starting(self):
        self.assertEqual(is_bored("I am happy. I like ice cream."), 1)

    def test_sentence_without_I_starting(self):
        self.assertEqual(is_bored("This is boring. That's not so fun."), 0)

    def test_sentence_with_multiple_I(self):
        self.assertEqual(is_bored("I am very bored. I really want to play."), 2)

if __name__ == '__main__':
    unittest.main()


Explanation:

- **Importing `unittest`**: We start by importing the necessary module (`unittest`) which allows us to write unit tests.
  
- **From Module Importing**: We then import the specific function we're testing (`is_bored`) from our code file (assuming it's named `HumanEval_91_code.py`).

- **Test Cases**:
  - **Empty String**: Tests an empty input string.
  - **Single Sentence**: Tests a single sentence without any 'I' starting.
  - **Multiple Sentences**: Tests multiple sentences including one where 'I' starts.
  - **Sentence With 'I' Starting**: Tests a sentence where 'I' starts.
  - **Sentence Without 'I' Starting**: Tests a sentence where 'I' does not start.
  - **Sentence With Multiple 'I'**: Tests a sentence with multiple instances of 'I'.

- **Running the Tests**: Finally, we call `unittest.main()` to run all the defined test cases.

This script will help ensure that the `is_bored` function works correctly across various scenarios.