Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `strlen` function:


import unittest
from HumanEval_23_code import strlen

class TestStrlen(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_single_character_string(self):
        self.assertEqual(strlen('a'), 1)
        self.assertEqual(strlen('z'), 1)

    def test_multi_character_string(self):
        self.assertEqual(strlen('abc'), 3)
        self.assertEqual(strlen('xyz'), 3)

    def test_string_with_spaces(self):
        self.assertEqual(strlen('hello world'), 11)
        self.assertEqual(strlen('  foo  '), 5)

    def test_string_with_special_characters(self):
        self.assertEqual(strlen('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), 47)
        self.assertEqual(strlen('abc!def'), 7)

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as an empty string, single character strings, multi-character strings with spaces, and strings with special characters. It uses the `assertEqual` method to verify the expected and actual outputs.