You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is a complete unittest test suite for the `count_upper` function:


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
        self.assertEqual(count_upper('a'), 0)
        self.assertEqual(count_upper('AEIOUabcdefg'), 2)
        self.assertEqual(count_upper('AEIOUabcdefgABC'), 3)

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover various scenarios, such as empty strings, strings with only uppercase vowels, strings with mixed cases, and strings with odd-indexed vowels. The `assertEqual` method is used to compare the expected output with the actual output of the `count_upper` function.