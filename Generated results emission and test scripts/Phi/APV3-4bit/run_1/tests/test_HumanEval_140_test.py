### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_140_code import fix_spaces
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()
 ### Immediate Task
Write the complete unittest test suite for the following Python function.

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

 import unittest
from HumanEval_140_code import fix_spaces

class TestFixSpaces(unittest.TestCase):
    def test_single_space(self):
        self.assertEqual(fix_spaces("Example"), "Example")

    def test_single_space_with_number(self):
        self.assertEqual(fix_spaces("Example 1"), "Example_1")

    def test_multiple_spaces(self):
        self.assertEqual(fix_spaces(" Example 2"), "_Example_2")

    def test_multiple_spaces_with_numbers(self):
        self.assertEqual(fix_spaces(" Example   3"), "_Example-3")

    def test_no_spaces(self):
        self.assertEqual(fix_spaces("Example123"), "Example123")

    def test_spaces_at_beginning_and_end(self):
        self.assertEqual(fix_spaces("   Example   "), "_Example_")

    def test_spaces_in_middle_with_number(self):
        self.assertEqual(fix_spaces(" Example 12 "), "_Example_12")

    def test_spaces_in_middle_with_underscore(self):
        self.assertEqual(fix_spaces(" Example_12 "), "Example_12")

    def test_spaces_in_middle_with_hyphen(self):
        self.assertEqual(fix_spaces(" Example-12 "), "_Example-12")

    def test_spaces_in_middle_with_multiple_hyphens(self):
        self.assertEqual(fix_spaces(" Example---12 "), "_Example-12")

    def test_spaces_in_middle_with_multiple_underscores(self):
        self.assertEqual(fix_spaces(" Example__12 "), "_Example_12")

    def test_spaces_in_middle_with_multiple_hyphens_and_underscores(self):
        self.assertEqual(fix_spaces(" Example---_12 "), "_Example-_12")

    def test_spaces_in_middle_with_mixed_characters(self):
        self.assertEqual(fix_spaces(" Example-12-_ "), "_Example-12-_")

    def test_spaces_in_middle_with_mixed_characters_and_numbers(self):
        self.assertEqual(fix_spaces(" Example-12-_3 "), "_Example-12-_3")

    def test_spaces_in_middle_with_mixed_characters_and_underscores(self):
        self.assertEqual(fix_spaces(" Example-12-_ "), "_Example-12-_")

    def test_spaces_in_middle_with_mixed_characters_and_hyphens(self):
        self.assertEqual(fix_spaces(" Example-12-_ "), "_Example-12-_")

    def test_spaces_in_middle_with_mixed_characters_and_numbers_and_underscores(self):
        self.assertEqual(fix_spaces(" Example-12-_3 "), "_Example-12-_3")

if __name__ == '__main__':
    unittest.main()