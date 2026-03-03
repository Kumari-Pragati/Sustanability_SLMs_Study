You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_140_code import fix_spaces
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    new_text = ""
    i = 0
    start, end = 0, 0
    while i < len(text):
        if text[i] == " ":
            end += 1
        else:
            if end - start > 2:
                new_text += "-" + text[i]
            elif end - start > 0:
                new_text += "_" * (end - start) + text[i]
            else:
                new_text += text[i]
            start, end = i + 1, i + 1
        i += 1
    if end - start > 2:
        new_text += "-"
    elif end - start > 0:
        new_text += "_"
    return new_text


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_140_code import fix_spaces

class TestFixSpaces(unittest.TestCase):

    def test_no_spaces(self):
        self.assertEqual(fix_spaces("Example"), "Example")

    def test_one_space(self):
        self.assertEqual(fix_spaces("Example 1"), "Example_1")

    def test_leading_space(self):
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")

    def test_multiple_spaces(self):
        self.assertEqual(fix_spaces(" Example   3"), "_Example-3")

    def test_no_consecutive_spaces(self):
        self.assertEqual(fix_spaces("Example  Example"), "Example_Example")

    def test_multiple_consecutive_spaces(self):
        self.assertEqual(fix_spaces("Example   Example"), "Example---Example")

    def test_all_spaces(self):
        self.assertEqual(fix_spaces("   "), "-")

    def test_empty_string(self):
        self.assertEqual(fix_spaces(""), "")

if __name__ == '__main__':
    unittest.main()


This script includes a test class `TestFixSpaces` that inherits from `unittest.TestCase`. Each method in this class is a test case that tests a specific scenario of the `fix_spaces` function. The `assertEqual` method is used to check if the output of the function matches the expected result.

To run this script, you need to have the `fix_spaces` function defined in a file named `HumanEval_140_code.py` in the same directory.