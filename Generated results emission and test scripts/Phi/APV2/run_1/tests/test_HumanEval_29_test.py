You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

 
import unittest
from HumanEval_29_code import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_filter_with_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_no_matching_prefix(self):
        self.assertEqual(filter_by_prefix(['xyz', 'bcd', 'cde', 'array'], 'a'), [])

    def test_single_element_list(self):
        self.assertEqual(filter_by_prefix(['abc'], 'a'), ['abc'])

    def test_multiple_elements_with_prefix(self):
        self.assertEqual(filter_by_prefix(['apple', 'application', 'banana', 'application'], 'app'), ['application', 'application'])

    def test_multiple_elements_without_prefix(self):
        self.assertEqual(filter_by_prefix(['apple', 'application', 'banana', 'application'], 'xyz'), [])

    def test_case_insensitive_filter(self):
        self.assertEqual(filter_by_prefix(['Apple', 'application', 'banana', 'Application'], 'app'), ['Apple', 'application', 'Application'])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover the following scenarios:

1. An empty list should return an empty list.
2. A list with strings that start with the given prefix should return those strings.
3. A list with no strings that start with the given prefix should return an empty list.
4. A list with a single string that starts with the given prefix should return that string.
5. A list with multiple strings that start with the given prefix should return all of them.
6. A list with multiple strings that do not start with the given prefix should return an empty list.
7. The function should be case-insensitive, meaning it should match strings regardless of their case.

Each test case is defined as a method within the `TestFilterByPrefix` class, and they are all run by the `unittest.main()` function when the script is executed.