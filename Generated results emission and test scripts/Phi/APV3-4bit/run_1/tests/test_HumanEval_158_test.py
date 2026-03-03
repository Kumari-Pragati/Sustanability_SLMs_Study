### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_158_code import find_max
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
    def test_normal_input(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")
        self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")

    def test_empty_list(self):
        self.assertEqual(find_max([]), None)

    def test_single_element_list(self):
        self.assertEqual(find_max(["single"]), "single")

    def test_all_elements_same_length(self):
        self.assertEqual(find_max(["aaaa", "aaaa", "aaaa"]), "aaaa")

    def test_all_elements_same_lexicographical_order(self):
        self.assertEqual(find_max(["aaa", "aaa", "aaa"]), "aaa")

    def test_all_elements_different_length_and_lexicographical_order(self):
        self.assertEqual(find_max(["a", "ab", "abc"]), "abc")

    def test_all_elements_different_length_and_lexicographical_order_with_ties(self):
        self.assertEqual(find_max(["a", "ab", "abc", "abcd"]), "abcd")

    def test_all_elements_same_length_and_lexicographical_order(self):
        self.assertEqual(find0(["aa", "aa", "aa"]), "aa")

if __name__ == '__main__':
    unittest.main()