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

 import unittest
from HumanEval_98_code import count_upper

class TestCountUpper(unittest.TestCase):

    def test_count_upper_with_vowels_at_even_indices(self):
        self.assertEqual(count_upper('aBCdEf'), 1)

    def test_count_upper_with_no_vowels_at_even_indices(self):
        self.assertEqual(count_upper('abcdefg'), 0)

    def test_count_upper_with_vowels_at_odd_indices(self):
        self.assertEqual(count_upper('dBBE'), 0)

    def test_count_upper_with_no_vowels_at_all(self):
        self.assertEqual(count_upper('XYZ'), 0)

    def test_count_upper_with_only_vowels_at_even_indices(self):
        self.assertEqual(count_upper('AEIOU'), 5)

    def test_count_upper_with_mixed_case_vowels_at_even_indices(self):
        self.assertEqual(count_upper('aEIOUe'), 3)

    def test_count_upper_with_mixed_case_no_vowels_at_even_indices(self):
        self.assertEqual(count_upper('aBCdEf'), 1)

    def test_count_upper_with_empty_string(self):
        self.assertEqual(count_upper(''), 0)

    def test_count_upper_with_single_character_string(self):
        self.assertEqual(count_upper('A'), 1)

if __name__ == '__main__':
    unittest.main()