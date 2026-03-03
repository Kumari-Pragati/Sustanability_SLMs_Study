You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
Here is a unittest test suite for the given Python function:


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

    def test_prefix_length(self):
        self.assertEqual(filter_by_prefix(['abc', 'abcd', 'bcd', 'cde', 'array'], 'ab'), ['abc', 'abcd'])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

- An empty list
- A list with no strings starting with the given prefix
- A list with a single string starting with the given prefix
- A list with multiple strings starting with the given prefix
- Case sensitivity (the function is case-sensitive)
- Prefix length (the function checks for the prefix of the correct length)

Please note that the function is case-sensitive, so the test `test_case_sensitivity` checks for this behavior.