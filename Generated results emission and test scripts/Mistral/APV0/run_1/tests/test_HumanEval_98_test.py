Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_98_code import count_upper
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    Examples:
    count_upper('aBCdEf') ➞ 1
    count_upper('abcdefg') ➞ 0
    count_upper('dBBE') ➞ 0
    """

    count = 0
    for i in range(0, len(s), 2):
        if s[i] in "AEIOU":
            count += 1
    return count

 Here is a unittest test script for the `count_upper` function:


import unittest
from HumanEval_98_code import count_upper

class TestCountUpper(unittest.TestCase):

    def test_count_upper(self):
        self.assertEqual(count_upper('aBCdEf'), 1)
        self.assertEqual(count_upper('abcdefg'), 0)
        self.assertEqual(count_upper('dBBE'), 0)
        self.assertEqual(count_upper('AeIoU'), 3)
        self.assertEqual(count_upper(''), 0)
        self.assertEqual(count_upper('AEIOU'), 1)
        self.assertEqual(count_upper('AEIOUAEIOU'), 2)
        self.assertEqual(count_upper('12345'), 0)
        self.assertEqual(count_upper('a1b2c3'), 0)
        self.assertEqual(count_upper('A1B2C3'), 0)

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to ensure the function works correctly for various inputs. It covers the base case (empty string), single uppercase vowel, multiple uppercase vowels, mixed case, and non-vowel characters.