You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_29_code import filter_by_prefix
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [x for x in strings if x.startswith(prefix)]


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_29_code import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_no_matching_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'z'), [])

    def test_single_matching_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_multiple_matching_prefixes(self):
        self.assertEqual(filter_by_prefix(['abc', 'abcd', 'bcd', 'cde', 'array'], 'a'), ['abc', 'abcd', 'array'])

    def test_case_sensitivity(self):
        self.assertEqual(filter_by_prefix(['Abc', 'abcd', 'bcd', 'cde', 'array'], 'a'), [])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the following scenarios:

- An empty list of strings.
- A list of strings with no matching prefix.
- A list of strings with a single matching prefix.
- A list of strings with multiple matching prefixes.
- Case sensitivity of the prefix.

The test cases are designed to cover all possible scenarios and edge cases.