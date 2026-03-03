Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 import unittest
from HumanEval_158_code import find_max

class TestFindMax(unittest.TestCase):

    def test_max_unique_characters(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")

    def test_lexicographical_order(self):
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")

    def test_longest_string(self):
        self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")

    def test_no_unique_characters(self):
        self.assertEqual(find_max(["aa", "bb", "cc"]), "aa")

    def test_single_word(self):
        self.assertEqual(find_max(["test"]), "test")

    def test_empty_list(self):
        self.assertEqual(find_max([]), "")

    def test_single_element_list(self):
        self.assertEqual(find_max(["single"]), "single")

if __name__ == '__main__':
    unittest.main()