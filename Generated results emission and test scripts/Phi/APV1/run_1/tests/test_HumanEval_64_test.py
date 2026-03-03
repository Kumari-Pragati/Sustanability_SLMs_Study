You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

    def test_empty_string(self):
        self.assertEqual(vowels_count(""), 0)

    def test_single_character(self):
        self.assertEqual(vowels_count("a"), 1)
        self.assertEqual(vowels_count("A"), 1)
        self.assertEqual(vowels_count("y"), 1)
        self.assertEqual(vowels_count("Y"), 1)

    def test_no_vowels(self):
        self.assertEqual(vowels_count("bcdfg"), 0)

    def test_only_vowels(self):
        self.assertEqual(vowels_count("aeiou"), 5)
        self.assertEqual(vowels_count("AEIOU"), 5)

    def test_vowels_with_y_at_end(self):
        self.assertEqual(vowels_count("abcdeY"), 3)
        self.assertEqual(vowels_count("ABCDEy"), 3)

    def test_vowels_with_y_not_at_end(self):
        self.assertEqual(vowels_count("abcdey"), 2)
        self.assertEqual(vowels_count("ABCDEy"), 2)

    def test_mixed_case_vowels(self):
        self.assertEqual(vowels_count("AbCde"), 2)
        self.assertEqual(vowels_count("aBcDe"), 2)

    def test_mixed_case_no_vowels(self):
        self.assertEqual(vowels_count("bcdfG"), 0)
        self.assertEqual(vowels_count("BcDFG"), 0)

    def test_long_string_with_vowels(self):
        self.assertEqual(vowels_count("aabbccddeeffgg"), 8)
        self.assertEqual(vowels_count("Aabbccddeeffgg"), 8)

    def test_long_string_with_y_at_end(self):
        self.assertEqual(vowels_count("aabbccddeeffggy"), 9)
        self.assertEqual(vowels_count("AabbccddeeffggY"), 9)

    def test_long_string_with_y_not_at_end(self):
        self.assertEqual(vowels_count("aabbccddeeffggy"), 8)
        self.assertEqual(vowels_count("AabbccddeeffggY"), 8)

if __name__ == '__main__':
    unittest.main()