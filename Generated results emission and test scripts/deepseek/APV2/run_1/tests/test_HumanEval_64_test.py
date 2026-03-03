You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is a unittest test suite for the given function:


import unittest
from HumanEval_64_code import vowels_count

class TestVowelsCount(unittest.TestCase):
    def test_lowercase_vowels(self):
        self.assertEqual(vowels_count("abcde"), 2)
        self.assertEqual(vowels_count("aeiou"), 5)
        self.assertEqual(vowels_count("aAeEiIoOuU"), 10)

    def test_uppercase_vowels(self):
        self.assertEqual(vowels_count("AEIOU"), 5)
        self.assertEqual(vowels_count("Aeiou"), 5)

    def test_mixed_case_vowels(self):
        self.assertEqual(vowels_count("AbCdE"), 2)
        self.assertEqual(vowels_count("aBcDe"), 2)

    def test_y_at_end(self):
        self.assertEqual(vowels_count("y"), 1)
        self.assertEqual(vowels_count("Y"), 1)
        self.assertEqual(vowels_count("yes"), 1)
        self.assertEqual(vowels_count("Yes"), 1)
        self.assertEqual(vowels_count("YE"), 1)
        self.assertEqual(vowels_count("YEa"), 2)

    def test_no_vowels(self):
        self.assertEqual(vowels_count("bcdfghjklmnpqrstvwxyz"), 0)
        self.assertEqual(vowels_count("BCDFGHJKLMNPQRSTVWXYZ"), 0)

    def test_empty_string(self):
        self.assertEqual(vowels_count(""), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure that the function is working correctly. It tests the function with lowercase vowels, uppercase vowels, mixed-case vowels, 'y' at the end of the word, no vowels, and an empty string.