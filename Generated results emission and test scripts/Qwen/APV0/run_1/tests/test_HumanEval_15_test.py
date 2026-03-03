system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_15_code import string_sequence
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 up to n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return ' '.join(str(x) for x in range(n + 1))


assistant

import unittest

# Importing the function from the given code snippet
from HumanEval_15_code import string_sequence

class TestStringSequence(unittest.TestCase):
    def test_string_sequence(self):
        self.assertEqual(string_sequence(0), "0")
        self.assertEqual(string_sequence(5), "0 1 2 3 4 5")

if __name__ == '__main__':
    unittest.main()


This script imports the `string_sequence` function from the provided code snippet and defines a test case class `TestStringSequence`. It includes two test cases using the `assertEqual` method to verify that the function returns the expected output for inputs of 0 and 5. Finally, it runs all tests when executed as a standalone script.