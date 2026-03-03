You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_158_code import find_max
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    Examples:
    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    """
    return sorted(words, key=lambda x: (-len(set(x)), x))[0]

 Here is the complete unittest test suite for the `find_max` function:


import unittest
from collections import Counter
from HumanEval_158_code import find_max

class TestFindMax(unittest.TestCase):

    def test_find_max(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")
        self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")
        self.assertEqual(find_max(["abcd", "abbb", "abcdde", "aabbcc"]), "abcdde")
        self.assertEqual(find_max(["aa", "bb", "aa", "cc", "aa"]), "cc")
        self.assertEqual(find_max(["", "abc", "xyz"]), "abc")
        self.assertEqual(find_max(["123", "123", "123"]), "123")
        self.assertEqual(find_max(["abc", "xyz", "abc"]), "xyz")
        self.assertEqual(find_max(["a", "b", "a"]), "b")
        self.assertEqual(find_max(["aa", "bb", "aa"]), "bb")

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover various scenarios, including edge cases and cases where the function might not behave as expected. The test cases are designed to be self-explanatory and easy to understand. The test suite uses the built-in `unittest.TestCase.assertEqual` method to compare the expected and actual results.