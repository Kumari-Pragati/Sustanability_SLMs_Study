Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

    def test_reverse_delete_no_palindrome(self):
        self.assertEqual(reverse_delete("abcde", "ae"), ('bcd', False))

    def test_reverse_delete_no_palindrome_2(self):
        self.assertEqual(reverse_delete("abcdef", "b"), ('acdef', False))

    def test_reverse_delete_palindrome(self):
        self.assertEqual(reverse_delete("abcdedcba", "ab"), ('cdedc', True))

    def test_reverse_delete_empty_string(self):
        self.assertEqual(reverse_delete("", ""), ('', True))

    def test_reverse_delete_single_character(self):
        self.assertEqual(reverse_delete("a", "a"), ('', False))

    def test_reverse_delete_no_removal(self):
        self.assertEqual(reverse_delete("abcabc", "a"), ('bcbc', False))

    def test_reverse_delete_palindrome_with_removal(self):
        self.assertEqual(reverse_delete("abccba", "c"), ('abba', True))

if __name__ == '__main__':
    unittest.main()