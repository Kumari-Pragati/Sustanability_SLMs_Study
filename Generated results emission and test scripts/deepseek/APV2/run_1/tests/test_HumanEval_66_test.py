You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_66_code import digitSum

class TestDigitSum(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(digitSum(""), 0)

    def test_no_uppercase_letters(self):
        self.assertEqual(digitSum("abc"), 0)

    def test_all_uppercase_letters(self):
        self.assertEqual(digitSum("ABCD"), 294)

    def test_mixed_case_letters(self):
        self.assertEqual(digitSum("AbCdEfGhIjKlMnOpQrStUvWxYz"), 1045)

    def test_single_uppercase_letter(self):
        self.assertEqual(digitSum("A"), 65)

    def test_single_lowercase_letter(self):
        self.assertEqual(digitSum("a"), 0)

    def test_mixed_case_letters_with_digits(self):
        self.assertEqual(digitSum("Ab1CdEfGhIjKlMnOpQrStUvWxYz"), 1045)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

- An empty string
- A string with no uppercase letters
- A string with all uppercase letters
- A string with mixed case letters
- A string with a single uppercase letter
- A string with a single lowercase letter
- A string with mixed case letters and digits

Each test checks that the `digitSum` function returns the correct sum for the given input.