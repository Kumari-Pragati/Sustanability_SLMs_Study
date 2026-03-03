You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

 import unittest
from HumanEval_158_code import find_max

class TestFindMax(unittest.TestCase):

    def test_find_max_single_max(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")

    def test_find_max_multiple_max(self):
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")

    def test_find_max_all_same_length(self):
        self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")

    def test_find_max_empty_list(self):
        self.assertEqual(find_max([]), "")

    def test_find_max_single_word(self):
        self.assertEqual(find_max(["a"]), "a")

    def test_find_max_single_letter(self):
        self.assertEqual(find_max(["a", "b"]), "b")

    def test_find_max_lexicographical_tie(self):
        self.assertEqual(find_max(["apple", "banana", "apricot"]), "apple")

    def test_find_max_lexicographical_after_length_tie(self):
        self.assertEqual(find_max(["banana", "apple", "apricot"]), "apple")

if __name__ == '__main__':
    unittest.main()