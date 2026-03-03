You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):

    def test_filter_by_substring(self):
        # Test with a list of strings that contains the substring
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], 'ab'), ['abc', 'ab'])

        # Test with a list of strings that does not contain the substring
        self.assertEqual(filter_by_substring(['xyz', 'pqr', 'stu'], 'ab'), [])

        # Test with an empty list
        self.assertEqual(filter_by_substring([], 'ab'), [])

        # Test with a list of strings that contains the substring multiple times
        self.assertEqual(filter_by_substring(['abcd', 'abef', 'ab'], 'ab'), ['abcd', 'abef', 'ab'])

        # Test with a list of strings that contains the substring at the beginning
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], 'abc'), ['abc'])

        # Test with a list of strings that contains the substring at the end
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], 'ab'), ['abc', 'ab'])

        # Test with a list of strings that contains the substring in the middle
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], 'c'), ['abc'])

        # Test with a list of strings that contains the substring with different cases
        self.assertEqual(filter_by_substring(['abc', 'def', 'Ab'], 'ab'), ['abc', 'Ab'])

        # Test with a list of strings that contains the substring with special characters
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], 'a$b'), ['abc', 'ab'])

        # Test with a list of strings that contains the substring with numbers
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab123'], 'ab'), ['abc', 'ab123'])

        # Test with a list of strings that contains the substring with spaces
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab cd'], 'ab'), ['abc', 'ab cd'])


if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure that the function is working as expected. It tests with different scenarios, including when the substring is at the beginning, end, middle, with different cases, special characters, numbers, and spaces.