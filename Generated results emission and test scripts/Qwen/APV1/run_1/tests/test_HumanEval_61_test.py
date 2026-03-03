system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_61_code import correct_bracketing

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def correct_bracketing(brackets: str):
    """brackets is a string of "(" and ")".
    Return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    depth = 0
    for b in brackets:
        if b == "(":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0


assistant

import unittest

# Function to be tested
from HumanEval_61_code import correct_bracketing

class TestCorrectBracketing(unittest.TestCase):

    def test_single_open(self):
        self.assertFalse(correct_bracketing("("))

    def test_single_close(self):
        self.assertFalse(correct_bracketing(")"))

    def test_balanced_parentheses(self):
        self.assertTrue(correct_bracketing("()"))
        self.assertTrue(correct_bracketing("(()())"))

    def test_unbalanced_parentheses(self):
        self.assertFalse(correct_bracketing(")("))
        self.assertFalse(correct_bracketing(")(()))"))

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `unittest` test case class named `TestCorrectBracketing`. It includes several test methods that cover different scenarios to ensure the correctness of the `correct_bracketing` function. The `assertNotEqual` method checks for balanced parentheses, while the `assertTrue` method verifies unbalanced parentheses. If any of these tests fail, it will raise an assertion error indicating which specific scenario failed.