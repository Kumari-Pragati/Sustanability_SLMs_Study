### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_27_code import flip_case
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
2. Include: from HumanEval_27_code import flip_case
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def flip_case(string: str) -> str:
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.swapcase()

 import unittest

from HumanEval_27_code import flip_case

class TestFlipCase(unittest.TestCase):
    def test_normal_string(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')

    def test_empty_string(self):
        self.assertEqual(flip_case(''), '')

    def test_string_with_mixed_case(self):
        self.assertEqual(flip_case('HeLLo WoRlD'), 'hEllO wOrld')

    def test_string_with_only_uppercase(self):
        self.assertEqual(flip_case('HELLO'), 'hello')

    def test_string_with_only_lowercase(self):
        self.assertEqual(flip_case('hello'), 'HELLO')

    def test_string_with_special_characters(self):
        self.assertEqual(flip_case('Hello, World!'), 'hELLO, wORLD!')

    def test_string_with_numbers(self):
        self.assertEqual(flip_case('123'), '123')

    def test_string_with_whitespace(self):
        self.assertEqual(flip_case('   '), '   ')

    def test_string_with_non_alphabetic_characters(self):
        self.assertEqual(flip_case('!@#$%^&*()'), '!@#$%^&*()')

if __name__ == '__main__':
    unittest.main()