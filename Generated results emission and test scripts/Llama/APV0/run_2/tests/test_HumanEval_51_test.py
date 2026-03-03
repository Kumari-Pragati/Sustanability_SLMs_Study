user

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
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])assistant

Here is the unittest test script for the `remove_vowels` function:

import unittest
from HumanEval_51_code import remove_vowels

class TestRemoveVowels(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_vowels(""), "")

    def test_single_line_string(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm"), "bcdf\nghjklm")

    def test_single_line_string_no_vowels(self):
        self.assertEqual(remove_vowels("zbcd"), "zbcd")

    def test_single_line_string_all_vowels(self):
        self.assertEqual(remove_vowels("aaaaa"), "")

    def test_single_line_string_mixed_case(self):
        self.assertEqual(remove_vowels("aaBAA"), "B")

    def test_single_line_string_no_vowels_and_spaces(self):
        self.assertEqual(remove_vowels("   zbcd   "), "   zbcd   ")

    def test_multiple_lines_string(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm\nnopqr"), "bcdf\nghjklm\nnopqr")

    def test_multiple_lines_string_no_vowels(self):
        self.assertEqual(remove_vowels("zbcd\nxyz"), "zbcd\nxyz")

    def test_multiple_lines_string_all_vowels(self):
        self.assertEqual(remove_vowels("aaaaa\naaaaa"), "")

if __name__ == '__main__':
    unittest.main()

This script defines a `TestRemoveVowels` class that contains 8 test methods, each testing a specific scenario for the `remove_vowels` function. The `assertEqual` method is used to verify that the output of the function matches the expected output.

You can run this script directly to execute the tests. If all tests pass, you should see a message indicating that the tests were successful. If any tests fail, you will see an error message indicating which test failed and why.