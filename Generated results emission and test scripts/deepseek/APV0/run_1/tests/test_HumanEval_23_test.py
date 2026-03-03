You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test script for the given Python function:


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
        self.assertEqual(strlen('hello@world'), 10)

    def test_string_with_numbers(self):
        self.assertEqual(strlen('12345'), 5)

if __name__ == '__main__':
    unittest.main()


This script creates a test class `TestStrlen` that inherits from `unittest.TestCase`. It includes several test methods to test the `strlen` function with different types of input strings. Each test method uses the `assertEqual` method to check if the output of `strlen` is as expected.

Please note that the `strlen` function is already implemented in the function body you provided. If you want to test a different function, you need to replace the `strlen` function in the `from HumanEval_23_code import strlen` line with the function you want to test.

Also, make sure to save the function you want to test in a file named `HumanEval_23_code.py` in the same directory as your test script.