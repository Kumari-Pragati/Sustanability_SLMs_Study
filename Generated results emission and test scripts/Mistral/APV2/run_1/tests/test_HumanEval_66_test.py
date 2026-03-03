You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the `digitSum` function:


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
        for s in ["AA", "AB", "ABC", "ABCD", "ABCDE", "ABCDEF", "ABCDEFG", "ABCDEFGH", "ABCDEFGHI", "ABCDEFGHIJ", "ABCDEFGHIJK", "ABCDEFGHIJKL", "ABCDEFGHIJKLM", "ABCDEFGHIJKLMN", "ABCDEFGHIJKLMNO", "ABCDEFGHIJKLMNOP", "ABCDEFGHIJKLMNOPQ", "ABCDEFGHIJKLMNOPQR", "ABCDEFGHIJKLMNOPQRS", "ABCDEFGHIJKLMNOPQRST", "ABCDEFGHIJKLMNOPQRSTU", "ABCDEFGHIJKLMNOPQRSTUV", "ABCDEFGHIJKLMNOPQRSTUW", "ABCDEFGHIJKLMNOPQRSTUVWX", "ABCDEFGHIJKLMNOPQRSTUVWXY", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]:
            self.assertEqual(digitSum(s), sum(ord(char) for char in s if char.isupper()))

    def test_special_cases(self):
        self.assertEqual(digitSum("A1B2C3"), 66)
        self.assertEqual(digitSum("A1B2C3D"), 66)
        self.assertEqual(digitSum("A1B2C3D4"), 66)
        self.assertEqual(digitSum("A1B2C3D4E"), 131)
        self.assertEqual(digitSum("A1B2C3D4E5"), 131)
        self.assertEqual(digitSum("A1B2C3D4E5F"), 131)
        self.assertEqual(digitSum("A1B2C3D4E5FG"), 131)
        self.assertEqual(digitSum("A1B2C3D4E5FGH"), 131)
        self.assertEqual(digitSum("A1B2C3D4E5FGHI"), 131)
        self.assertEqual(digitSum("A1B2C3D4E5FGHIJ"), 131)
        self.assertEqual(digitSum("A1B2C3D4E5FGHIJK"), 131)
        self.assertEqual(digitSum("A1B2C3D4E5FGHIJKL"), 131)
        self.assertEqual(digitSum("A1B2C3D4E5FGHIJKLM"), 131)
        self.assertEqual(digitSum("A1B2C3D4E5FGHIJKLMN"), 131)
        self.assertEqual(digitSum("A1B2C3D4E5FGHIJKLMNO"), 131)
        self.assertEqual(digitSum("A1B2C3D4E5FGHIJKLMNOP"), 131)
        self.assertEqual(digitSum("A1B2C3D4E5FG