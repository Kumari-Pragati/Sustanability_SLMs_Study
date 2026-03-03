You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 import unittest
from HumanEval_23_code import strlen

class TestStrlenFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_single_character(self):
        self.assertEqual(strlen('a'), 1)

    def test_multiple_characters(self):
        self.assertEqual(strlen('abc'), 3)

    def test_string_with_spaces(self):
        self.assertEqual(strlen('hello world'), 11)

    def test_string_with_special_characters(self):
        self.assertEqual(strlen('!@#$%^&*()'), 11)

    def test_string_with_numbers(self):
        self.assertEqual(strlen('12345'), 5)

    def test_string_with_mixed_characters(self):
        self.assertEqual(strlen('abc123!@#'), 9)

if __name__ == '__main__':
    unittest.main()