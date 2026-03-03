Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_66_code import digitSum
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    if s == "":
        return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)

 Here is a unittest test script for the `digitSum` function:


import unittest
from HumanEval_66_code import digitSum

class TestDigitSum(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(digitSum(""), 0)

    def test_lowercase_characters(self):
        self.assertEqual(digitSum("abcdefghijklmnopqrstuvwxyz"), 0)

    def test_mixed_case_characters(self):
        self.assertEqual(digitSum("AbCdEfGhIjKlMnOpQrStUvWxYz"), 1055)

    def test_single_uppercase_characters(self):
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.assertEqual(digitSum(char), ord(char))

    def test_multiple_uppercase_characters(self):
        for s in ["AA", "ABC", "ABCDE", "ABCDEFG", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]:
            self.assertEqual(digitSum(s), sum(ord(char) for char in s))

    def test_mixed_case_and_digits(self):
        for s in ["A1B2C3", "A1B2C3D4", "A1B2C3D4E5", "A1B2C3D4E5F6"]:
            self.assertEqual(digitSum(s), sum(ord(char) for char in s if char.isupper()))

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as an empty string, lowercase characters, mixed case characters, single uppercase characters, multiple uppercase characters, and mixed case and digits. It uses the `unittest.TestCase.assertEqual` method to verify the expected and actual results.