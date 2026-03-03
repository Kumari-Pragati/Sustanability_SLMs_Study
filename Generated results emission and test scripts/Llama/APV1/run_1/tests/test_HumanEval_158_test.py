user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
    return sorted(words, key=lambda x: (-len(set(x)), x))[0]assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_158_code import find_max

class TestFindMax(unittest.TestCase):

    def test_find_max(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")
        self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")
        self.assertEqual(find_max(["abc", "def", "ghi"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "ghi"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "ghi"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "abc"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "abc", "ghi"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "abc", "abc"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "abc", "abc", "ghi"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "abc", "abc", "abc"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "abc", "abc", "abc", "ghi"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "abc", "abc", "abc", "abc"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "abc", "abc", "abc", "abc", "ghi"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "abc", "abc", "abc", "abc", "abc"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "ghi"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "ghi"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "ghi"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "ghi"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "ghi"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "ghi"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc", "abc"]), "abc")
        self.assertEqual(find_max(["abc", "def", "abc", "abc