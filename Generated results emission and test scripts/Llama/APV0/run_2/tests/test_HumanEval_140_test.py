user

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
    return new_textassistant

Here is the unittest test script for the `fix_spaces` function:

import unittest
from HumanEval_140_code import fix_spaces

class TestFixSpaces(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(fix_spaces("Example"), "Example")

    def test_single_space(self):
        self.assertEqual(fix_spaces("Example 1"), "Example_1")

    def test_multiple_spaces(self):
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")

    def test_consecutive_spaces(self):
        self.assertEqual(fix_spaces(" Example   3"), "_Example-3")

    def test_multiple_consecutive_spaces(self):
        self.assertEqual(fix_spaces("   Example   4"), "_-_Example-4")

    def test_no_spaces(self):
        self.assertEqual(fix_spaces("NoSpaces"), "NoSpaces")

    def test_leading_spaces(self):
        self.assertEqual(fix_spaces("   LeadingSpaces"), "_LeadingSpaces")

    def test_trailing_spaces(self):
        self.assertEqual(fix_spaces("TrailingSpaces   "), "TrailingSpaces")

if __name__ == '__main__':
    unittest.main()

This script defines a `TestFixSpaces` class with 7 test methods, each testing a specific scenario:

1. `test_single_word`: Tests that a single-word input is returned unchanged.
2. `test_single_space`: Tests that a single space is replaced with an underscore.
3. `test_multiple_spaces`: Tests that multiple spaces are replaced with a single underscore.
4. `test_consecutive_spaces`: Tests that consecutive spaces are replaced with a single hyphen.
5. `test_multiple_consecutive_spaces`: Tests that multiple consecutive spaces are replaced with multiple hyphens.
6. `test_no_spaces`: Tests that an input with no spaces is returned unchanged.
7. `test_leading_spaces` and `test_trailing_spaces`: Test that leading and trailing spaces are handled correctly.

You can run this script directly to execute the tests. If all tests pass, you should see a message indicating that the tests were successful.