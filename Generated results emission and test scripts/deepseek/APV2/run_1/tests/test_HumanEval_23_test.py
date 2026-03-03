You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_23_code import strlen
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def strlen(string: str) -> int:
    """Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_23_code import strlen

class TestStrlen(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_non_empty_string(self):
        self.assertEqual(strlen('abc'), 3)

    def test_string_with_spaces(self):
        self.assertEqual(strlen('hello world'), 11)

    def test_string_with_special_characters(self):
        self.assertEqual(strlen('!@#$%^&*()'), 10)

    def test_string_with_numbers(self):
        self.assertEqual(strlen('1234567890'), 10)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for an empty string, a non-empty string, a string with spaces, a string with special characters, and a string with numbers. It uses the `assertEqual` method to check if the output of the `strlen` function matches the expected output.