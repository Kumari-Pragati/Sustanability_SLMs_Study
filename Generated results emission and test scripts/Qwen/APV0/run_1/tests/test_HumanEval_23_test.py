system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Importing the function to be tested
from HumanEval_23_code import strlen

class TestStringLength(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(strlen(""), 0)
        
    def test_single_character_string(self):
        self.assertEqual(strlen("a"), 1)
        
    def test_multiple_characters_string(self):
        self.assertEqual(strlen("hello"), 5)
        
    def test_whitespace_string(self):
        self.assertEqual(strlen("   "), 1)
        
    def test_long_string(self):
        long_string = "This is a very long string that will exceed the maximum allowed length in some systems."
        self.assertEqual(strlen(long_string), len(long_string))

if __name__ == '__main__':
    unittest.main()


Explanation:

- The `unittest` module is imported at the beginning to create unit tests.
- The `strlen` function is imported using an alias (`from HumanEval_23_code import strlen`) so it can be referenced as `strlen`.
- A class named `TestStringLength` is defined within the `unittest.TestCase` framework. This class inherits from `unittest.TestCase`, which provides basic assertion methods like `assertEqual()`.
- Four test cases are defined inside the `TestStringLength` class:
  - `test_empty_string`: Tests if the function returns 0 for an empty string.
  - `test_single_character_string`: Tests if the function returns 1 for a single character string.
  - `test_multiple_characters_string`: Tests if the function returns the correct number of characters for a longer string.
  - `test_whitespace_string`: Tests if the function correctly handles strings containing whitespace.
  - `test_long_string`: Tests if the function returns the correct length for a very long string.
- Each test case uses the `self.assertEqual()` method to check if the output of the `strlen` function matches the expected result.
- Finally, the `unittest.main()` function runs all the test cases when executed directly (i.e., not as part of another program).