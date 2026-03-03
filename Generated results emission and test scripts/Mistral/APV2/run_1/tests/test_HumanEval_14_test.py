You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_14_code import all_prefixes
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    result: List[str] = []
    for i in range(len(string)):
        result.append(string[: i + 1])
    return result

 Here is the complete unittest test suite for the `all_prefixes` function:


import unittest
from HumanEval_14_code import all_prefixes

class TestAllPrefixes(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(all_prefixes(''), [''])

    def test_single_character(self):
        self.assertListEqual(all_prefixes('a'), ['a'])
        self.assertListEqual(all_prefixes('b'), ['b'])
        self.assertListEqual(all_prefixes('c'), ['c'])

    def test_multiple_characters(self):
        self.assertListEqual(all_prefixes('ab'), ['a', 'ab'])
        self.assertListEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])
        self.assertListEqual(all_prefixes('abcd'), ['a', 'ab', 'abc', 'abcd'])

    def test_special_characters(self):
        self.assertListEqual(all_prefixes('123'), ['1', '12', '123'])
        self.assertListEqual(all_prefixes('!@#'), ['!', '!@', '!@#'])
        self.assertListEqual(all_prefixes('abc!'), ['a', 'ab', 'abc', 'abc!'])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for an empty string, single-character strings, multiple-character strings, and strings with special characters. The test cases are designed to cover various edge cases and ensure the function works as expected.