### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_112_code import reverse_delete
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
 ### Immediate Task
Write the complete unittest test suite for the following Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_112_code import reverse_delete
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def reverse_delete(s, c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd', False)
    For s = "abcdef", c = "b"  the result should be ('acdef', False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc', True)
    """

    s = ''.join([char for char in s if char not in c])
    return (s, s[::-1] == s)

 import unittest

from HumanEval_112_code import reverse_delete

class TestReverseDelete(unittest.TestCase):
    def test_normal_case(self):
        result, is_palindrome = reverse_delete("abcde", "ae")
        self.assertEqual(result, "bcd")
        self.assertFalse(is_palindrome)

    def test_empty_string(self):
        result, is_palindrome = reverse_delete("", "")
        self.assertEqual(result, "")
        self.assertTrue(is_palindrome)

    def test_single_character(self):
        result, is_palindrome = reverse_delete("a", "a")
        self.assertEqual(result, "")
        self.assertTrue(is_palindrome)

    def test_palindrome_case(self):
        result, is_palindrome = reverse_delete("abcdedcba", "ab")
        self.assertEqual(result, "cdedc")
        self.assertTrue(is_palindrome)

    def test_no_match_case(self):
        result, is_palindrome = reverse_delete("abcdef", "xy")
        self.assertEqual(result, "abcdef")
        self.assertFalse(is_palindrome)

    def test_case_with_no_removal(self):
        result, is_palindrome = reverse_delete("abcdef", "ghijklmnopqrstuvwxyz")
        self.assertEqual(result, "abcdef")
        self.assertFalse(is_palindrome)

if __name__ == '__main__':
    unittest.main()