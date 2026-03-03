system
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

user
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


assistant

import unittest

from HumanEval_158_code import find_max

class TestFindMax(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(find_max(["apple"]), "apple")

    def test_multiple_words(self):
        self.assertEqual(find_max(["banana", "cherry", "date"]), "cherry")

    def test_same_length_unique_chars(self):
        self.assertEqual(find_max(["abc", "def", "ghi"]), "abc")

    def test_case_insensitive(self):
        self.assertEqual(find_max(["Apple", "Banana", "Cherry"]), "Cherry")

    def test_duplicate_words(self):
        self.assertEqual(find_max(["cat", "dog", "elephant", "cat", "mouse"]), "elephant")

    def test_empty_string(self):
        self.assertIsNone(find_max([]))

    def test_all_duplicates(self):
        self.assertEqual(find_max(["a", "b", "c", "d", "e"]), None)

if __name__ == '__main__':
    unittest.main()