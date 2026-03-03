user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return resultassistant

Here is the unittest test script for the `all_prefixes` function:

import unittest
from HumanEval_14_code import all_prefixes

class TestAllPrefixes(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(all_prefixes(""), [])

    def test_single_character_string(self):
        self.assertEqual(all_prefixes("a"), ["a"])

    def test_multiple_character_string(self):
        self.assertEqual(all_prefixes("abc"), ["a", "ab", "abc"])

    def test_long_string(self):
        self.assertEqual(all_prefixes("abcdefghijklmnopqrstuvwxyz"), 
                         ["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", 
                          "abcdefgh", "abcdefghi", "abcdefghij", "abcdefghijk", 
                          "abcdefghijkl", "abcdefghijklm", "abcdefghijklmn", 
                          "abcdefghijklmno", "abcdefghijklmnop", "abcdefghijklmnopq", 
                          "abcdefghijklmnopqr", "abcdefghijklmnopqrs", "abcdefghijklmnopqrst", 
                          "abcdefghijklmnopqrstu", "abcdefghijklmnopqrstv", "abcdefghijklmnopqrstuw", 
                          "abcdefghijklmnopqrstxy", "abcdefghijklmnopqrstyz", "abcdefghijklmnopqrstz"])

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            all_prefixes(123)

if __name__ == '__main__':
    unittest.main()

This script tests the `all_prefixes` function with various inputs, including:

* An empty string
* A single-character string
* A multiple-character string
* A long string
* A non-string input (to test the function's error handling)

Each test case uses the `assertEqual` method to check that the output of the `all_prefixes` function matches the expected result. The `with self.assertRaises` block is used to test that the function raises a `TypeError` when given a non-string input.