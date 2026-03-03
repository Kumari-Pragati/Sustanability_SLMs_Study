system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_27_code import flip_case
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def flip_case(string: str) -> str:
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.swapcase()


assistant

import unittest

# Importing the function to be tested
from HumanEval_27_code import flip_case

class TestFlipCase(unittest.TestCase):
    def test_flip_case(self):
        # Test case 1: Normal input
        self.assertEqual(flip_case('Hello'), 'hELLO')

        # Test case 2: All uppercase letters
        self.assertEqual(flip_case('HELLO'), 'hello')

        # Test case 3: All lowercase letters
        self.assertEqual(flip_case('hello'), 'HELLO')

        # Test case 4: A mix of uppercase and lowercase letters
        self.assertEqual(flip_case('HELLo'), 'hello')

        # Test case 5: Empty string
        self.assertEqual(flip_case(''), '')

        # Test case 6: String with spaces
        self.assertEqual(flip_case(' Hello World! '), ' hELLO wORLD!')

if __name__ == '__main__':
    unittest.main()


This script imports the `flip_case` function and creates a test class named `TestFlipCase`. It includes several test cases to ensure that the function behaves as expected under different conditions. The `assertEqual` method is used to check if the output of `flip_case` matches the expected result. If any test fails, an assertion error will be raised, indicating which test failed and what the expected and actual results were.