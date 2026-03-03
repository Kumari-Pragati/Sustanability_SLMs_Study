system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

from HumanEval_64_code import vowels_count

class TestVowelsCount(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(vowels_count(""), 0)

    def test_single_letter(self):
        self.assertEqual(vowels_count("a"), 1)
        self.assertEqual(vowels_count("A"), 1)

    def test_multiple_letters(self):
        self.assertEqual(vowels_count("hello"), 2)
        self.assertEqual(vowels_count("world"), 1)

    def test_y_at_end(self):
        self.assertEqual(vowels_count("sky"), 1)
        self.assertEqual(vowels_count("fly"), 1)

    def test_y_not_at_end(self):
        self.assertEqual(vowels_count("syzygy"), 2)

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases covering different scenarios such as empty strings, single letters, multiple letters, words ending in 'y', and words not ending in 'y'. It ensures that the `vowels_count` function behaves correctly under various conditions.