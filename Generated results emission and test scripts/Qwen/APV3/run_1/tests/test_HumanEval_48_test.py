system
### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_48_code import is_palindrome
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()

user
### Immediate Task
Write the complete unittest test suite for the following Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_48_code import is_palindrome
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True


assistant

import unittest

from HumanEval_48_code import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_positive_strings(self):
        self.assertTrue(is_palindrome(''))
        self.assertTrue(is_palindrome('aba'))
        self.assertTrue(is_palindrome('aaaaa'))
        self.assertFalse(is_palindrome('zbcd'))

    def test_edge_cases(self):
        self.assertTrue(is_palindrome(''))
        self.assertTrue(is_palindrome('a'))
        self.assertTrue(is_palindrome('aa'))
        self.assertTrue(is_palindrome('aaa'))
        self.assertTrue(is_palindrome('aaaa'))
        self.assertTrue(is_palindrome('aaaaa'))
        self.assertTrue(is_palindrome('zzz'))
        self.assertTrue(is_palindrome('zzzz'))
        self.assertTrue(is_palindrome('zzzzz'))
        self.assertTrue(is_palindrome('zzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'))
        self.assertTrue(is_palindrome('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz