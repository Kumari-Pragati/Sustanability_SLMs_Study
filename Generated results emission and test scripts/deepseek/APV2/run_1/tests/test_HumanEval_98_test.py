You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_98_code import count_upper

class TestCountUpper(unittest.TestCase):
    def test_count_upper(self):
        self.assertEqual(count_upper('aBCdEf'), 1)
        self.assertEqual(count_upper('abcdefg'), 0)
        self.assertEqual(count_upper('dBBE'), 0)
        self.assertEqual(count_upper('AaBbCc'), 1)
        self.assertEqual(count_upper('dEfGhIj'), 1)
        self.assertEqual(count_upper(''), 0)
        self.assertEqual(count_upper('ABCDE'), 2)
        self.assertEqual(count_upper('abcde'), 0)
        self.assertEqual(count_upper('ABCDEabcde'), 2)
        self.assertEqual(count_upper('123456'), 0)
        self.assertEqual(count_upper('A1B2C3D4E5'), 2)

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases, including both upper and lower case letters, and letters at even and odd indices. It also tests the function with an empty string and with strings of length 1.