user

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
    return countassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_98_code import count_upper

class TestCountUpper(unittest.TestCase):

    def test_count_upper(self):
        self.assertEqual(count_upper('aBCdEf'), 1)
        self.assertEqual(count_upper('abcdefg'), 0)
        self.assertEqual(count_upper('dBBE'), 0)
        self.assertEqual(count_upper('AEIOU'), 2)
        self.assertEqual(count_upper('bcDEfG'), 0)
        self.assertEqual(count_upper(''), 0)
        self.assertEqual(count_upper('AEIOUa'), 1)
        self.assertEqual(count_upper('BCDEFG'), 0)

if __name__ == '__main__':
    unittest.main()


This script includes 8 test cases to cover different scenarios, including edge cases like an empty string. The `assertEqual` method is used to compare the output of the `count_upper` function with the expected output. If the output does not match the expected output, the test case will fail.