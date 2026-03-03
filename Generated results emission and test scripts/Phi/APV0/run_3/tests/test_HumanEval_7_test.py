Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

    def test_filter_by_substring(self):
        # Test case 1: Basic functionality
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], 'ab'), ['abc', 'ab'])

        # Test case 2: No matches
        self.assertEqual(filter_by_substring(['xyz', 'lmn', 'opq'], 'ab'), [])

        # Test case 3: Substring at the beginning
        self.assertEqual(filter_by_substring(['abcd', 'efgh', 'abij'], 'ab'), ['abcd', 'abij'])

        # Test case 4: Substring at the end
        self.assertEqual(filter_by_substring(['mnop', 'qrst', 'uvwxy'], 'xy'), ['uvwxy'])

        # Test case 5: Substring in the middle
        self.assertEqual(filter_by_substring(['abcde', 'fghij', 'klmno'], 'cd'), ['abcde'])

        # Test case 6: Empty list
        self.assertEqual(filter_by_substring([], 'ab'), [])

        # Test case 7: Substring not in any string
        self.assertEqual(filter_by_substring(['123', '456', '789'], 'xy'), [])

        # Test case 8: Substring is an empty string
        self.assertEqual(filter_by_substring(['', '', ''], ''), ['', ''])

        # Test case 9: Substring is longer than any string
        self.assertEqual(filter_by_substring(['a', 'bb', 'ccc'], 'ddd'), [])

        # Test case 10: Substring is the same as the string
        self.assertEqual(filter_by_substring(['aa', 'bb', 'cc'], 'aa'), ['aa'])

if __name__ == '__main__':
    unittest.main()