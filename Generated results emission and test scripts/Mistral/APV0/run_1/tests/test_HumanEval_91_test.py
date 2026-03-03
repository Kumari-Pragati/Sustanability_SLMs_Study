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

 Here is a unittest test script for the `is_bored` function:


import unittest
from HumanEval_91_code import is_bored

class TestIsBored(unittest.TestCase):

    def test_is_bored(self):
        self.assertEqual(is_bored("Hello world"), 0)
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)
        self.assertEqual(is_bored("I'm bored. Let's go out."), 1)
        self.assertEqual(is_bored("I'm not bored."), 0)
        self.assertEqual(is_bored("I'm bored!"), 1)
        self.assertEqual(is_bored("I'm bored."), 1)
        self.assertEqual(is_bored("I'm bored.."), 1)
        self.assertEqual(is_bored("I'm bored?"), 1)
        self.assertEqual(is_bored("I'm bored!!"), 1)
        self.assertEqual(is_bored("I'm bored. I'm bored."), 2)
        self.assertEqual(is_bored("I'm not bored. I'm not bored."), 0)
        self.assertEqual(is_bored("I'm bored. I'm not bored."), 1)
        self.assertEqual(is_bored("I'm not bored. I'm bored."), 0)
        self.assertEqual(is_bored("I'm bored.".upper()), 1)
        self.assertEqual(is_bored("I'm bored.".lower()), 1)
        self.assertEqual(is_bored("I'm bored.".capitalize()), 1)

if __name__ == '__main__':
    unittest.main()


This test script includes multiple test cases to ensure the function works correctly for different inputs, including uppercase, lowercase, and title case sentences. It also tests for sentences with multiple boredoms and sentences with no boredoms.