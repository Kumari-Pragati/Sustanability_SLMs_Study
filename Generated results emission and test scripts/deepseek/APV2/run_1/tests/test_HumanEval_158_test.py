You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given function:


import unittest
from HumanEval_158_code import find_max

class TestFindMax(unittest.TestCase):

    def test_find_max(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")
        self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")
        self.assertEqual(find_max(["apple", "banana", "cherry"]), "banana")
        self.assertEqual(find_max(["abc", "def", "ghi"]), "abc")
        self.assertEqual(find_max(["123", "456", "789"]), "123")
        self.assertEqual(find_max(["aaa", "bbb", "ccc"]), "aaa")
        self.assertEqual(find_max(["abcd", "efgh", "ijkl"]), "abcd")
        self.assertEqual(find_max(["zyx", "wvu", "tsr"]), "zyx")
        self.assertEqual(find_max(["!@#", "$%^", "&*("]), "!@#")

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure that the function is working correctly. It tests with words of different lengths, including words with the same number of unique characters but different lexicographical order. It also tests with words that have the same number of unique characters and the same lexicographical order.