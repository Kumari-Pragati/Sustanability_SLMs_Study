user

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

    return len(set(string.lower()))assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_16_code import count_distinct_characters

class TestCountDistinctCharacters(unittest.TestCase):

    def test_count_distinct_characters(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)
        self.assertEqual(count_distinct_characters(''), 0)
        self.assertEqual(count_distinct_characters('a'), 1)
        self.assertEqual(count_distinct_characters('abc'), 3)
        self.assertEqual(count_distinct_characters('aA'), 1)
        self.assertEqual(count_distinct_characters('aAa'), 1)
        self.assertEqual(count_distinct_characters('aAaB'), 2)
        self.assertEqual(count_distinct_characters('aAaBc'), 3)
        self.assertEqual(count_distinct_characters('aAaBcD'), 4)
        self.assertEqual(count_distinct_characters('aAaBcD123'), 6)
        self.assertEqual(count_distinct_characters('aAaBcD123!@#'), 7)

if __name__ == '__main__':
    unittest.main()


This script includes 10 test cases to cover different scenarios, including empty string, single character, multiple characters, and mixed case. The `assertEqual` method is used to compare the output of the function with the expected result.