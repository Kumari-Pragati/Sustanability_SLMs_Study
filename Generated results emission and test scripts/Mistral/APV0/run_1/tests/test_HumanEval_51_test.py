Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_51_code import remove_vowels
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])

 Here is a unittest test script for the `remove_vowels` function:


import unittest
from HumanEval_51_code import remove_vowels

class TestRemoveVowels(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_vowels(''), '')

    def test_string_with_vowels(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm"), 'bcdf\nghjklm')

    def test_string_only_vowels(self):
        self.assertEqual(remove_vowels('aaaaa'), '')

    def test_mixed_case(self):
        self.assertEqual(remove_vowels('aaBAA'), 'B')

    def test_string_with_no_vowels(self):
        self.assertEqual(remove_vowels('zbcd'), 'zbcd')

    def test_special_characters(self):
        self.assertEqual(remove_vowels('abc123!@#$%^&*()'), 'bc123!@#$%^&*()')

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as an empty string, strings with vowels, strings with only vowels, mixed case, strings with no vowels, and strings with special characters. The test cases use the `assertEqual` method to compare the expected output with the actual output of the `remove_vowels` function.