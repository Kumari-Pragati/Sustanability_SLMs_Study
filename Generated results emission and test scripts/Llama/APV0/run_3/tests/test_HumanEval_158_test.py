user

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
    return sorted(words, key=lambda x: (-len(set(x)), x))[0]assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_158_code import find_max

class TestFindMax(unittest.TestCase):

    def test_find_max(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")
        self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")
        self.assertEqual(find_max(["abc", "def", "ghi"]), "abc")
        self.assertEqual(find_max(["a", "b", "c"]), "a")
        self.assertEqual(find_max(["a", "aa", "aaa"]), "a")
        self.assertEqual(find_max(["a", "ab", "abc"]), "a")
        self.assertEqual(find_max(["a", "ab", "abcd"]), "a")
        self.assertEqual(find_max(["a", "ab", "abcd", "abcde"]), "a")

    def test_empty_list(self):
        self.assertRaises(IndexError, find_max, [])

    def test_single_element_list(self):
        self.assertEqual(find_max(["a"]), "a")

    def test_list_with_duplicates(self):
        self.assertEqual(find_max(["a", "a", "b", "c"]), "a")

if __name__ == '__main__':
    unittest.main()


This script includes several test cases to cover different scenarios, such as:

- Testing the function with different lists of words
- Testing the function with an empty list
- Testing the function with a list containing a single element
- Testing the function with a list containing duplicate elements

Each test case uses the `assertEqual` method to check if the output of the function matches the expected output. If the output does not match the expected output, the test will fail and an error message will be displayed.