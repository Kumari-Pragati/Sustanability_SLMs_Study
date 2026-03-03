You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the `count_upper` function:


import unittest
from HumanEval_98_code import count_upper

class TestCountUpper(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_upper(""), 0)

    def test_all_lowercase(self):
        self.assertEqual(count_upper("abcdefg"), 0)

    def test_all_uppercase(self):
        self.assertEqual(count_upper("ABCDEFG"), 3)

    def test_mixed_case(self):
        self.assertEqual(count_upper("aBCdEf"), 1)

    def test_odd_length(self):
        self.assertEqual(count_upper("dBBE"), 0)

    def test_single_uppercase_vowel(self):
        self.assertEqual(count_upper("A"), 1)

    def test_multiple_uppercase_vowels(self):
        self.assertEqual(count_upper("AEIOU"), 3)

    def test_special_characters(self):
        self.assertEqual(count_upper("!A@B$C%D&E#F"), 1)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios such as empty strings, all lowercase, all uppercase, mixed case, odd length strings, single uppercase vowel, multiple uppercase vowels, and strings containing special characters.