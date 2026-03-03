### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_64_code import vowels_count
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
2. Include: from HumanEval_64_code import vowels_count
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
FIX = """
Add more test cases.
"""


def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = "aeiouAEIOU"
    n_vowels = sum(c in vowels for c in s)
    if s[-1] == 'y' or s[-1] == 'Y':
        n_vowels += 1
    return n_vowels

 import unittest

from HumanEval_64_code import vowels_count

class TestVowelsCount(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(vowels_count("abcde"), 2)

    def test_case_with_y_at_end(self):
        self.assertEqual(vowels_count("ACEDY"), 3)

    def test_case_with_no_y(self):
        self.assertEqual(vowels_count("abc"), 2)

    def test_case_with_y_not_at_end(self):
        self.assertEqual(vowels_count("abcy"), 3)

    def test_case_with_no_vowels(self):
        self.assertEqual(vowels_count("bcdf"), 0)

    def test_case_with_mixed_case(self):
        self.assertEqual(vowels_count("AbCde"), 2)

    def test_case_with_multiple_y(self):
        self.assertEqual(vowels_count("AyY"), 3)

    def test_case_with_uppercase_only(self):
        self.assertEqual(vowels_count("AY"), 2)

    def test_case_with_lowercase_only(self):
        self.assertEqual(vowels_count("yY"), 2)

    def test_case_with_mixed_uppercase_and_lowercase(self):
        self.assertEqual(vowels_count("AyYb"), 3)

    def test_case_with_consecutive_y(self):
        self.assertEqual(vowels_count("AyYy"), 3)

    def test_case_with_no_vowels_and_y(self):
        self.assertEqual(vowels_count("bY"), 1)

    def test_case_with_single_y_not_at_end(self):
        self.assertEqual(vowels_count("bY"), 1)

    def test_case_with_single_y_at_end(self):
0
        self.assertEqual(vowels_count("bYy"), 2)

if __name__ == '__main__':
    unittest.main()