You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the `fix_spaces` function:


import unittest
from HumanEval_140_code import fix_spaces

class TestFixSpaces(unittest.TestCase):

    def test_single_space(self):
        self.assertEqual(fix_spaces("Example"), "Example")
        self.assertEqual(fix_spaces("Example_1"), "Example_1")

    def test_multiple_spaces(self):
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")
        self.assertEqual(fix_spaces(" Example   3"), "_Example-3")
        self.assertEqual(fix_spaces("   Example   4"), "_Example-4")
        self.assertEqual(fix_spaces(" Example      5"), "_Example-5")

    def test_edge_cases(self):
        self.assertEqual(fix_spaces(""), "")
        self.assertEqual(fix_spaces(" "), "_")
        self.assertEqual(fix_spaces("Example "), "_Example")
        self.assertEqual(fix_spaces(" Example"), "_Example")
        self.assertEqual(fix_spaces("Example_"), "Example_")
        self.assertEqual(fix_spaces("Example-"), "Example-")

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for single spaces, multiple spaces, edge cases, and empty strings. It covers various scenarios where the function might be used, ensuring that the function behaves as expected.