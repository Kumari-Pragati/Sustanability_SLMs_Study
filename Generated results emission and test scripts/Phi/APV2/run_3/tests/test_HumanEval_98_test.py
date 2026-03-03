You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

 import unittest
from HumanEval_98_code import count_upper

class TestCountUpper(unittest.TestCase):

    def test_count_upper_with_vowels_at_even_indices(self):
        self.assertEqual(count_upper('aBCdEf'), 1)

    def test_count_upper_with_no_vowels_at_even_indices(self):
        self.assertEqual(count_upper('abcdefg'), 0)

    def test_count_upper_with_vowels_at_odd_indices(self):
        self.assertEqual(count_upper('dBBE'), 0)

    def test_count_upper_with_all_uppercase_vowels_at_even_indices(self):
        self.assertEqual(count_upper('AEIOU'), 5)

    def test_count_upper_with_no_uppercase_vowels(self):
        self.assertEqual(count_upper('XYZ'), 0)

    def test_count_upper_with_mixed_case_vowels_at_even_indices(self):
        self.assertEqual(count_upper('aEIOUb'), 2)

    def test_count_upper_with_empty_string(self):
        self.assertEqual(count_upper(''), 0)

    def test_count_upper_with_single_character(self):
        self.assertEqual(count_upper('A'), 1)

    def test_count_upper_with_multiple_vowels_at_even_indices(self):
        self.assertEqual(count_upper('AEIOUAEIOU'), 10)

if __name__ == '__main__':
    unittest.main()