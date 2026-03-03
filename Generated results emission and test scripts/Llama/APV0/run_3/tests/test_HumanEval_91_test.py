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
    return sum(sentence.startswith('I ') for sentence in sentences if sentence)assistant

Here is the unittest test script for the `is_bored` function:

import unittest
from HumanEval_91_code import is_bored

class TestIsBored(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(is_bored(""), 0)

    def test_no_boredoms(self):
        self.assertEqual(is_bored("Hello world"), 0)

    def test_one_boredom(self):
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)

    def test_multiple_boredoms(self):
        self.assertEqual(is_bored("I am bored. I am so bored. I am really bored"), 3)

    def test_boredoms_with_punctuation(self):
        self.assertEqual(is_bored("I love this weather! I hate this weather."), 2)

    def test_boredoms_with_multiple_sentences(self):
        self.assertEqual(is_bored("I am bored. I am so bored. I am really bored. I am happy now"), 3)

    def test_boredoms_with_empty_sentences(self):
        self.assertEqual(is_bored("I am bored.. I am so bored. I am really bored"), 2)

if __name__ == '__main__':
    unittest.main()

This script defines a `TestIsBored` class with seven test methods:

1. `test_empty_string`: Tests that an empty string returns 0.
2. `test_no_boredoms`: Tests that a string with no boredoms returns 0.
3. `test_one_boredom`: Tests that a string with one boredom returns 1.
4. `test_multiple_boredoms`: Tests that a string with multiple boredoms returns the correct count.
5. `test_boredoms_with_punctuation`: Tests that a string with boredoms and punctuation returns the correct count.
6. `test_boredoms_with_multiple_sentences`: Tests that a string with multiple sentences and boredoms returns the correct count.
7. `test_boredoms_with_empty_sentences`: Tests that a string with empty sentences and boredoms returns the correct count.

Each test method uses the `assertEqual` method to check that the output of the `is_bored` function matches the expected result.

You can run this script directly to execute the tests and verify that the `is_bored` function is working correctly.