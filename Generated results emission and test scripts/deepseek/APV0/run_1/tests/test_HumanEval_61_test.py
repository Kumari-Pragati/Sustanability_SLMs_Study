You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_61_code import correct_bracketing

class TestCorrectBracketing(unittest.TestCase):

    def test_single_opening_bracket(self):
        self.assertFalse(correct_bracketing("("))

    def test_matching_brackets(self):
        self.assertTrue(correct_bracketing("()"))

    def test_nested_brackets(self):
        self.assertTrue(correct_bracketing("(()())"))

    def test_unmatching_brackets(self):
        self.assertFalse(correct_bracketing(")(()"))

    def test_extra_closing_bracket(self):
        self.assertFalse(correct_bracketing("())("))

    def test_extra_opening_bracket(self):
        self.assertFalse(correct_bracketing("((("))

    def test_empty_string(self):
        self.assertTrue(correct_bracketing(""))

if __name__ == '__main__':
    unittest.main()


This script includes a test class `TestCorrectBracketing` that inherits from `unittest.TestCase`. Each method in this class is a test case that tests a specific scenario. The `unittest.main()` at the end will run all the test cases when the script is run directly.