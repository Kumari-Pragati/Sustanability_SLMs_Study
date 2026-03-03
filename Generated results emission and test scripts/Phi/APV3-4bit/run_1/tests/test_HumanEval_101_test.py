### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_101_code import words_string
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
2. Include: from HumanEval_101_code import words_string
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """

    if not s:
        return []

    s_list = []

    for letter in s:
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)

    s_list = "".join(s_list)
    return s_list.split()

 import unittest

from HumanEval_101_code import words_string

class TestWordsString(unittest.TestCase):

    def test_normal_input(self):
        input_str = "Hi, my name is John"
        expected_output = ["Hi", "my", "name", "is", "John"]
        self.assertEqual(words_string(input_str), expected_output)

    def test_normal_input_with_spaces(self):
        input_str = "One two three four five six"
        expected_output = ["One", "two", "three", "four", "five", "six"]
        self.assertEqual(words_string(input_str), expected_output)

    def test_empty_string(self):
        input_str = ""
        expected_output = []
        self.assertEqual(words_string(input_str), expected_output)

    def test_input_with_commas_only(self):
        input_str = ",,"
        expected_output = []
        self.assertEqual(words_string(input_str), expected_output)

    def test_input_with_spaces_only(self):
        input_str = "   "
        expected_output = []
        self.assertEqual(words_string(input_str), expected_output)

    def test_input_with_mixed_commas_and_spaces(self):
        input_str = "Hi, my, name, is John, "
        expected_output = ["Hi", "my", "name", "is", "John"]
        self.assertEqual(words_string(input_str), expected_output)

    def test_input_with_mixed_commas_and_spaces_and_numbers(self):
        input_str = "1, 2, 3, 4, 5, 6"
        expected_output = ["1", "2", "3", "4", "5", "6"]
        self.assertEqual(words_string(input_str), expected_output)

    def test_input_with_mixed_commas_and_spaces_and_numbers_and_letters(self):
        input_str = "1,a,2,b,3,c,4,d,5,e,6"
        expected_output = ["1", "a", "2", "b", "3", "c", "4", "d", "5", "e", "6"]
        self.assertEqual(words_string(input_str), expected_output)

    def test_input_with_mixed_commas_and_spaces_and_numbers_and_letters_and_special_chars(self):
        input_str = "1,a,2,b,3,c,4,d,e,6,!@#$%^&*()"
        expected_output = ["1", "a", "2", "b", "3", "c", "4", "d", "e", "6", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
        self.assertEqual(words_string(input_str), expected_output)

if __name__ == '__main__':
    unittest.main()