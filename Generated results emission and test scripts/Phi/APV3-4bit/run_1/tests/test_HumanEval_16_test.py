### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_16_code import count_distinct_characters
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
2. Include: from HumanEval_16_code import count_distinct_characters
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    return len(set(string.lower()))

 
import unittest
from HumanEval_16_code import count_distinct_characters

class TestCountDistinctCharacters(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)

    def test_empty_string(self):
        self.assertEqual(count_distinct_characters(''), 0)

    def test_single_character_string(self):
        self.assertEqual(count_distinct_characters('a'), 1)

    def test_all_same_characters(self):
        self.assertEqual(count_distinct_characters('aaaaaa'), 1)

    def test_mixed_case_string(self):
        self.assertEqual(count_distinct_characters('AaBbCc'), 3)

    def test_special_characters(self):
        self.assertEqual(count_distinct_characters('!@#$%^&*'), 6)

    def test_whitespace_string(self):
        self.assertEqual(count_distinct_characters('   '), 0)

    def test_numeric_string(self):
        self.assertEqual(count_distinct_characters('1234567890'), 10)

    def test_non_alphabetical_string(self):
        self.assertEqual(count_distinct_characters('1234567890!@#$%^&*'), 10)

    def test_invalid_input(self):
        with self.assertRaiss(TypeError):
            count_distinct_characters(123)

if __name__ == '__main__':
    unittest.main()