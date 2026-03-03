Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_16_code import count_distinct_characters
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """

    return len(set(string.lower()))

 Here is a unittest test script for the `count_distinct_characters` function:


import unittest
from HumanEval_16_code import count_distinct_characters

class TestCountDistinctCharacters(unittest.TestCase):

    def test_count_distinct_characters(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)
        self.assertEqual(count_distinct_characters(''), 0)
        self.assertEqual(count_distinct_characters('a'), 1)
        self.assertEqual(count_distinct_characters('abcabc'), 3)
        self.assertEqual(count_distinct_characters('ABCabc'), 6)
        self.assertEqual(count_distinct_characters('1234567890'), 10)
        self.assertEqual(count_distinct_characters('!@#$%^&*()_+-=[]{}|;:,.<>?/'), 32)

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to ensure the function works correctly for various inputs. It covers empty strings, single-character strings, strings with repeated characters, strings with uppercase and lowercase characters, and strings with special characters.