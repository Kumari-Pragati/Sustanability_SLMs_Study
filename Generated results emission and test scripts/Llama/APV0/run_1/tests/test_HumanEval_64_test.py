user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return n_vowelsassistant

Here is the unittest test script for the `vowels_count` function:

import unittest
from HumanEval_64_code import vowels_count

class TestVowelsCount(unittest.TestCase):
    def test_vowels_count(self):
        # Test cases
        self.assertEqual(vowels_count("abcde"), 2)
        self.assertEqual(vowels_count("ACEDY"), 3)
        self.assertEqual(vowels_count("hello"), 2)
        self.assertEqual(vowels_count("AEIOU"), 4)
        self.assertEqual(vowels_count("y"), 1)
        self.assertEqual(vowels_count("Y"), 1)
        self.assertEqual(vowels_count(""), 0)
        self.assertEqual(vowels_count("bcdfghjklmnpqrstvwxyz"), 0)
        self.assertEqual(vowels_count("AEIOUY"), 5)
        self.assertEqual(vowels_count("AEIOUy"), 4)
        self.assertEqual(vowels_count("AEIOUYy"), 5)

if __name__ == '__main__':
    unittest.main()

This script defines a `TestVowelsCount` class that contains several test methods. Each test method tests a specific scenario or edge case for the `vowels_count` function. The `assertEqual` method is used to verify that the output of the function matches the expected result.

You can run this script directly to execute the tests. If all tests pass, you should see a message indicating that all tests were successful. If any tests fail, you will see an error message indicating which test failed and why.