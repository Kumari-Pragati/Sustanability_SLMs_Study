### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_134_code import check_if_last_char_is_a_letter
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
2. Include: from HumanEval_134_code import check_if_last_char_is_a_letter
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False

 import unittest
from HumanEval_134_code import check_if_last_char_is_a_letter

class TestCheckIfLastCharIsALetter(unittest.TestCase):
    def test_last_char_is_letter(self):
        self.assertTrue(check_if_last_char_is_a_letter("apple pi e"))

    def test_last_char_is_not_letter(self):
        self.assertFalse(check_if_last_char_is_a_letter("apple pie"))

    def test_empty_string(self):
        self.assertFalse(check_if_last_char_is_a_letter(""))

    def test_last_char_is_space(self):
        self.assertFalse(check_if_last_char_is_a_letter("apple pi e "))

    def test_single_char_string(self):
        self.assertTrue(check_if_last_char_is_a_letter("a"))

    def test_non_alphabetical_last_char(self):
        self.assertFalse(check_if_last_char_is_a_letter("apple p1"))

if __name__ == '__main__':
    unittest.main()