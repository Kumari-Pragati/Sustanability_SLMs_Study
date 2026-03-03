system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Provided function to be tested
from HumanEval_23_code import strlen

class TestStringLength(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(strlen(""), 0)
        
    def test_single_character_string(self):
        self.assertEqual(strlen("a"), 1)
        
    def test_multiple_character_string(self):
        self.assertEqual(strlen("hello"), 5)
        
    def test_whitespace_string(self):
        self.assertEqual(strlen(" "), 1)
        
    def test_long_string(self):
        long_string = "This is a very long string that should exceed the maximum allowed length in this context."
        self.assertGreaterEqual(strlen(long_string), 64)
        
    def test_negative_length(self):
        with self.assertRaises(ValueError):
            strlen("-")

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various edge cases such as empty strings, single characters, multiple characters, whitespace, and longer strings. It also checks for negative lengths by raising a `ValueError`.