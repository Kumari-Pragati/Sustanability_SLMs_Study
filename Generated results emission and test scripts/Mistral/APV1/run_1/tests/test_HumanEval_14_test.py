You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the `all_prefixes` function:


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
        self.assertListEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])
        self.assertListEqual(all_prefixes('abcd'), ['a', 'ab', 'abc', 'abcd'])
        self.assertListEqual(all_prefixes('xyz'), ['x', 'xy', 'xyz'])

    def test_special_characters(self):
        self.assertListEqual(all_prefixes('aBc'), ['a', 'aB', 'aBc'])
        self.assertListEqual(all_prefixes('123'), ['1', '12', '123'])
        self.assertListEqual(all_prefixes('!@#'), ['', '!', '!@', '!@#'])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for empty strings, single-character strings, multiple-character strings, strings with special characters, and edge cases. It uses the `assertListEqual` function to compare the expected output with the actual output of the `all_prefixes` function.