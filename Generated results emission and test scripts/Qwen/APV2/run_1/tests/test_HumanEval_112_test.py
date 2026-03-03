system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


assistant

import unittest

# Function to be tested
from HumanEval_112_code import reverse_delete

class TestReverseDelete(unittest.TestCase):

    def test_reverse_delete(self):
        # Test case 1
        self.assertEqual(reverse_delete("abcde", "ae"), ("bcd", False))
        
        # Test case 2
        self.assertEqual(reverse_delete("abcdef", "b"), ("acdef", False))
        
        # Test case 3
        self.assertEqual(reverse_delete("abcdedcba", "ab"), ("cdedc", True))

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases to verify the correctness of the `reverse_delete` function. Each test case uses the `assertEqual` method to compare the expected outcome with the actual outcome returned by the function.