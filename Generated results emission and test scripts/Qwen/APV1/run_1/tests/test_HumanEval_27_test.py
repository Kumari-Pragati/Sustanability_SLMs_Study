system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
        # Test case 1: Normal input (all letters)
        self.assertEqual(flip_case('Hello'), 'hELLO')

        # Test case 2: All uppercase
        self.assertEqual(flip_case('HELLO'), 'hELLO')

        # Test case 3: All lowercase
        self.assertEqual(flip_case('hello'), 'HELL')

        # Test case 4: Mixed case
        self.assertEqual(flip_case('HeLLo WoRLD!'), 'hEllO wOrLD!')

        # Test case 5: Empty string
        self.assertEqual(flip_case(""), "")

        # Test case 6: String with special characters
        self.assertEqual(flip_case('123abcABC$'), '123ABCabc$')

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestFlipCase` class that inherits from `unittest.TestCase`. It contains a single method `test_flip_case`, which tests various scenarios of the `flip_case` function using assertions. The `assertEqual` method checks if the output of `flip_case` matches the expected result. If any of these cases fail, it will raise an assertion error, indicating that something went wrong in the implementation.