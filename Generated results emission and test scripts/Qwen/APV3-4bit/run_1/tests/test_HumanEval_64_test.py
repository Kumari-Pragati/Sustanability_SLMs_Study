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

class TestVowelCount(unittest.TestCase):
    def test_single_letter(self):
        self.assertEqual(vowels_count("a"), 1)

    def test_consecutive_letters(self):
        self.assertEqual(vowels_count("aa"), 2)

    def test_mixed_case(self):
        self.assertEqual(vowels_count("AbCdEfGhIjKlMnOpQrStUvWxYz"), 17)

    def test_y_at_end(self):
        self.assertEqual(vowels_count("abcy"), 2)

    def test_y_not_at_end(self):
        self.assertEqual(vowels_count("abcyZ"), 1)

    def test_empty_string(self):
        self.assertEqual(vowels_count(""), 0)

    def test_all_uppercase(self):
        self.assertEqual(vowels_count("ABCDEF"), 3)

    def test_all_lowercase(self):
        self.assertEqual(vowels_count("abcdef"), 3)

    def test_all_caps(self):
        self.assertEqual(vowels_count("ABCDEFG"), 3)

    def test_all_lower(self):
        self.assertEqual(vowels_count("abcdefgh"), 3)

    def test_all_caps_and_digits(self):
        self.assertEqual(vowels_count("ABCDEFG123"), 3)

    def test_all_lower_and_digits(self):
        self.assertEqual(vowels_count("abcdef123"), 3)

    def test_all_caps_and_special_chars(self):
        self.assertEqual(vowels_count("ABCDEFG!@#%^&*()"), 3)

    def test_all_lower_and_special_chars(self):
        self.assertEqual(vowels_count("abcdef!@#%^&*()"), 3)

    def test_all_caps_and_spaces(self):
        self.assertEqual(vowels_count("ABCDEFG ABCDEFGH"), 3)

    def test_all_lower_and_spaces(self):
        self.assertEqual(vowels_count("abcdef abcdefgh"), 3)

    def test_all_caps_and_punctuation(self):
        self.assertEqual(vowels_count("ABCDEFG abcdefghi!@#$%^&*()"), 3)

    def test_all_lower_and_punctuation(self):
        self.assertEqual(vowels_count("abcdef abcdefghi!@#$%^&*()"), 3)

    def test_all_caps_and_symbols(self):
        self.assertEqual(vowels_count("ABCDEFG abcdefghi!@#$%^&*()"), 3)

    def test_all_lower_and_symbols(self):
        self.assertEqual(vowels_count("abcdef abcdefghi!@#$%^&*()"), 3)

    def test_all_caps_and_whitespace(self):
        self.assertEqual(vowels_count("ABCDEFG abcdefghi!@#$%^&*() "), 3)

    def test_all_lower_and_whitespace(self):
        self.assertEqual(vowels_count("abcdef abcdefghi!@#$%^&*() "), 3)

    def test_all_caps_and_numbers(self):
        self.assertEqual(vowels_count("ABCDEFG abcdefghi!@#$%^&*()1234567890"), 3)

    def test_all_lower_and_numbers(self):
        self.assertEqual(vowels_count("abcdef abcdefghi!@#$%^&*()1234567890"), 3)

    def test_all_caps_and_alphabetic(self):
        self.assertEqual(vowels_count("ABCDEFG abcdefghi!@#$%^&*()A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z"), 3)

    def test_all_lower_and_alphabetic(self):
        self.assertEqual(vowels_count("abcdef abcdefghi!@#$%^&*()a b c d e f g h i j k l m n o p q r s t u v w x y z"), 3)

    def test_all_caps_and_alphanumeric(self):
        self.assertEqual(vowels_count("ABCDEFG abcdefghi!@#$%^&*()A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z0123456789"), 3)

    def test_all_lower_and_alphanumeric(self):
        self.assertEqual(vowels_count("abcdef abcdefghi!@#$%^&*()a b c d e f g h i j k l m n o p q r s t u v w x y z0123456789"), 3)

    def test_all_caps_and_special_and_alphanumeric(self):
        self.assertEqual(vowels_count("ABCDEFG