system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_56_code import correct_bracketing

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def correct_bracketing(brackets: str):
    """brackets is a string of "<" and ">".
    Return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    depth = 0
    for b in brackets:
        if b == "<":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0


assistant

import unittest

# Function to be tested
from HumanEval_56_code import correct_bracketing

class TestCorrectBracketing(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(correct_bracketing("<"))

    def test_single_character(self):
        self.assertTrue(correct_bracketing("<>"))
    
    def test_balanced_string(self):
        self.assertTrue(correct_bracketing("<<><>>"))
    
    def test_unbalanced_string(self):
        self.assertFalse(correct_bracketing("><<>"))

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestCorrectBracketing` class that inherits from `unittest.TestCase`. It contains four test methods to verify the correctness of the `correct_bracketing` function:

- The first method tests an empty string, expecting it to return `False`.
- The second method tests a single character string, expecting it to return `True`.
- The third method tests a balanced string, expecting it to return `True`.
- The fourth method tests an unbalanced string, expecting it to return `False`.

The `unittest.main()` call at the end runs all the test methods when the script is executed directly.