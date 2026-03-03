You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_140_code import fix_spaces

class TestFixSpaces(unittest.TestCase):

    def test_no_spaces(self):
        self.assertEqual(fix_spaces("Example"), "Example")

    def test_single_space(self):
        self.assertEqual(fix_spaces("Example 1"), "Example_1")
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")
        self.assertEqual(fix_spaces(" Example   3"), "_Example-3")

    def test_multiple_spaces(self):
        self.assertEqual(fix_spaces("Example   "), "Example---")
        self.assertEqual(fix_spaces("  Example"), "---Example")
        self.assertEqual(fix_spaces("   Example   "), "---_Example---")
        self.assertEqual(fix_spaces("   Example   Test"), "---_Example---Test")

    def test_no_consecutive_spaces(self):
        self.assertEqual(fix_spaces("ExampleTest"), "ExampleTest")

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases:

1. `test_no_spaces`: Tests the function with a string that doesn't contain any spaces.
2. `test_single_space`: Tests the function with a string that contains one or more spaces.
3. `test_multiple_spaces`: Tests the function with a string that contains multiple consecutive spaces.
4. `test_no_consecutive_spaces`: Tests the function with a string that doesn't contain any consecutive spaces.

Each test case uses the `assertEqual` method to check if the output of the `fix_spaces` function matches the expected result.