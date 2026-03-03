You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is a comprehensive unittest test suite for the `vowels_count` function:


import unittest
from HumanEval_64_code import vowels_count

class TestVowelsCount(unittest.TestCase):
    def test_vowels_count(self):
        self.assertEqual(vowels_count("abcde"), 2)
        self.assertEqual(vowels_count("ACEDY"), 3)
        self.assertEqual(vowels_count("aeiou"), 5)
        self.assertEqual(vowels_count("AEIOU"), 5)
        self.assertEqual(vowels_count("y"), 1)
        self.assertEqual(vowels_count(""), 0)
        self.assertEqual(vowels_count("abc"), 1)
        self.assertEqual(vowels_count("ABC"), 1)
        self.assertEqual(vowels_count("aeiouY"), 6)
        self.assertEqual(vowels_count("AEIOUY"), 6)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as uppercase and lowercase vowels, single-letter words, words with 'y' at the end, and words with multiple vowels. It also includes an empty string as a test case to ensure that the function handles edge cases correctly.