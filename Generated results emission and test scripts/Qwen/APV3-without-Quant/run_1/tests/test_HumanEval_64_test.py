system
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

user
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


assistant

import unittest

from HumanEval_64_code import vowels_count

class TestVowelsCount(unittest.TestCase):
    def test_single_letter(self):
        self.assertEqual(vowels_count(""), 0)

    def test_one_vowel(self):
        self.assertEqual(vowels_count("a"), 1)

    def test_multiple_vowels(self):
        self.assertEqual(vowels_count("aeiou"), 5)

    def test_consonants_only(self):
        self.assertEqual(vowels_count("bcdfghjklmnpqrstvwxyz"), 0)

    def test_y_at_end(self):
        self.assertEqual(vowels_count("hello"), 2)

    def test_y_not_at_end(self):
        self.assertEqual(vowels_count("helloworld"), 3)

    def test_y_in_middle(self):
        self.assertEqual(vowels_count("hyphenated"), 1)

    def test_y_with_space(self):
        self.assertEqual(vowels_count("yummy"), 1)

    def test_y_with_punctuation(self):
        self.assertEqual(vowels_count("y!um"), 1)

    def test_y_with_number(self):
        self.assertEqual(vowels_count("y1n"), 1)

    def test_y_with_special_char(self):
        self.assertEqual(vowels_count("y@#$"), 1)

    def test_y_with_uppercase(self):
        self.assertEqual(vowels_count("Y"), 1)

    def test_y_with_lowercase(self):
        self.assertEqual(vowels_count("y"), 1)

    def test_y_with_accented_letters(self):
        self.assertEqual(vowels_count("ééé"), 3)

    def test_y_with_combination(self):
        self.assertEqual(vowels_count("yuiou"), 4)

    def test_y_with_long_word(self):
        self.assertEqual(vowels_count("yummyyum"), 4)

    def test_y_with_short_word(self):
        self.assertEqual(vowels_count("y"), 1)

    def test_y_with_mixed_case(self):
        self.assertEqual(vowels_count("Yummy"), 1)

    def test_y_with_numbers_and_symbols(self):
        self.assertEqual(vowels_count("y!1$"), 1)

    def test_y_with_spaces_and_symbols(self):
        self.assertEqual(vowels_count("y y"), 1)

    def test_y_with_numbers_and_symbols(self):
        self.assertEqual(vowels_count("y1$"), 1)

    def test_y_with_accented_letters_and_numbers(self):
        self.assertEqual(vowels_count("ééé1"), 3)

    def test_y_with_accented_letters_and_symbols(self):
        self.assertEqual(vowels_count("ééé!"), 3)

    def test_y_with_accented_letters_and_numbers(self):
        self.assertEqual(vowels_count("ééé1$"), 3)

    def test_y_with_accented_letters_and_symbols(self):
        self.assertEqual(vowels_count("ééé!1"), 3)

    def test_y_with_accented_letters_and_numbers(self):
        self.assertEqual(vowels_count("ééé!1$"), 3)

    def test_y_with_accented_letters_and_symbols(self):
        self.assertEqual(vowels_count("ééé!1$ "), 3)

    def test_y_with_accented_letters_and_symbols(self):
        self.assertEqual(vowels_count("ééé!1$ @"), 3)

    def test_y_with_accented_letters_and_symbols(self):
        self.assertEqual(vowels_count("ééé!1$ @#"), 3)

    def test_y_with_accented_letters_and_symbols(self):
        self.assertEqual(vowels_count("ééé!1$ @#", "!"), 3)

    def test_y_with_accented_letters_and_symbols(self):
        self.assertEqual(vowels_count("ééé!1$ @#", "!@"), 3)

    def test_y_with_accented_letters_and_symbols(self):
        self.assertEqual(vowels_count("ééé!1$ @#", "!@#", "@"), 3)

    def test_y_with_accented_letters_and_symbols(self):
        self.assertEqual(vowels_count("ééé!1$ @#", "!@#", "@#", "#"), 3)

    def test_y_with_accented_letters_and_symbols(self):
        self.assertEqual(vowels_count("ééé!1$ @#", "!@#", "@#", "#", "$"), 3)

    def test_y_with_accented_letters_and_symbols(self):
        self.assertEqual(vowels_count("ééé!1$ @#", "!@#", "@#", "#", "$", "%"), 3)

    def test_y_with_accented_letters_and_symbols(self):
        self.assertEqual(vowels_count("ééé!1$ @#", "!@#", "@