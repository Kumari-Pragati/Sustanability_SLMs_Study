You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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


### Response:
Here is the unittest test script for the given Python function:


import unittest
from HumanEval_56_code import correct_bracketing

class TestCorrectBracketing(unittest.TestCase):

    def test_single_bracket(self):
        self.assertFalse(correct_bracketing("<"))
        self.assertTrue(correct_bracketing(">"))

    def test_matching_brackets(self):
        self.assertTrue(correct_bracketing("<>"))
        self.assertTrue(correct_bracketing("<<>>"))
        self.assertTrue(correct_bracketing("<<><>>"))

    def test_mismatched_brackets(self):
        self.assertFalse(correct_bracketing("><"))
        self.assertFalse(correct_bracketing("><>"))
        self.assertFalse(correct_bracketing("><<>"))

    def test_empty_string(self):
        self.assertTrue(correct_bracketing(""))

    def test_large_input(self):
        self.assertTrue(correct_bracketing("<<"*10000 + ">>"*10000))

if __name__ == '__main__':
    unittest.main()


This script includes several test cases to ensure the function is working as expected. It tests the function with single brackets, matching brackets, mismatched brackets, an empty string, and a large input.