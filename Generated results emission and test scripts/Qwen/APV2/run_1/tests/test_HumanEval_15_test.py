system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

# Importing the function from the provided code snippet
from HumanEval_15_code import string_sequence

class TestStringSequence(unittest.TestCase):
    
    def test_string_sequence(self):
        # Test cases to verify the correctness of the function
        self.assertEqual(string_sequence(0), "0")
        self.assertEqual(string_sequence(5), "0 1 2 3 4 5")
        self.assertEqual(string_sequence(10), "0 1 2 3 4 5 6 7 8 9 10")

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases that cover different scenarios (n=0, n=5, and n=10). It uses `assertEqual` methods to check if the output of the `string_sequence` function matches the expected results.