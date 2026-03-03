You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is the complete unittest test suite for the `fix_spaces` function:


import unittest
from HumanEval_140_code import fix_spaces

class TestFixSpaces(unittest.TestCase):

    def test_fix_spaces_single_word(self):
        self.assertEqual(fix_spaces("Example"), "Example")
        self.assertEqual(fix_spaces("example"), "example")
        self.assertEqual(fix_spaces("EXAMPLE"), "EXAMPLE")

    def test_fix_spaces_single_space(self):
        self.assertEqual(fix_spaces("Example 1"), "Example_1")
        self.assertEqual(fix_spaces("example 1"), "example_1")
        self.assertEqual(fix_spaces("EXAMPLE 1"), "EXAMPLE_1")

    def test_fix_spaces_multiple_spaces(self):
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")
        self.assertEqual(fix_spaces(" example 2 "), "_example_2")
        self.assertEqual(fix_spaces("EXAMPLE  2"), "_EXAMPLE-2")

    def test_fix_spaces_consecutive_spaces(self):
        self.assertEqual(fix_spaces(" Example   3"), "_Example-3")
        self.assertEqual(fix_spaces(" example    4 "), "_example-4")
        self.assertEqual(fix_spaces("EXAMPLE      5"), "_EXAMPLE-5")

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases to cover different scenarios: single-word strings, strings with a single space, strings with multiple spaces, and strings with consecutive spaces. The test cases use the `assertEqual` method to compare the expected output with the actual output of the `fix_spaces` function.