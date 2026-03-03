### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_7_code import filter_by_substring
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
2. Include: from HumanEval_7_code import filter_by_substring
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter the list of strings and return only those that contain `substring`.
    >>> filter_by_substring(['abc', 'def', 'ab'], 'ab')
    ['abc', 'ab']
    """
    return [x for x in strings if substring in x]

 import unittest
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):
    def test_strings_containing_substring(self):
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], 'ab'), ['abc', 'ab'])

    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'abc'), [])

    def test_substring_not_found(self):
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], 'xyz'), [])

    def test_substring_at_beginning(self):
        self.assertEqual(filter_by_substring(['abcd', 'xyz', 'abc'], 'ab'), ['abcd', 'abc'])

    def test_substring_at_end(self):
        self.assertEqual(filter_by_substring(['abc', 'xyzdef', 'abc'], 'c'), ['abc', 'xyzdef'])

    def test_substring_in_middle(self):
        self.assertEqual(filter_by_substring(['abcxyz', 'defghi', 'abc'], 'bc'), ['abcxyz', 'abc'])

if __name__ == '__main__':
    unittest.main()