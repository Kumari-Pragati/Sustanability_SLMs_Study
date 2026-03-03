system
### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_98_code import count_upper
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()

user
### Immediate Task
Write the complete unittest test suite for the following Python function.

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


assistant

import unittest

from HumanEval_98_code import count_upper

class TestCountUpper(unittest.TestCase):
    def test_string_with_uppercase_vowels_in_even_indices(self):
        self.assertEqual(count_upper("aBCdEf"), 1)
        
    def test_string_without_uppercase_vowels_in_even_indices(self):
        self.assertEqual(count_upper("abcdefg"), 0)
        
    def test_string_with_only_lowercase_letters(self):
        self.assertEqual(count_upper("xyz"), 0)
        
    def test_string_with_no_uppercase_vowels(self):
        self.assertEqual(count_upper("zzz"), 0)
        
    def test_string_with_all_uppercase_vowels(self):
        self.assertEqual(count_upper("AEIOU"), 5)
        
    def test_string_with_mixed_case(self):
        self.assertEqual(count_upper("AeIoU"), 5)
        
    def test_string_with_multiple_uppercase_vowels(self):
        self.assertEqual(count_upper("ABCEFGHIJKL"), 3)
        
    def test_string_with_single_uppercase_vowel(self):
        self.assertEqual(count_upper("B"), 0)
        
    def test_string_with_double_uppercase_vowels(self):
        self.assertEqual(count_upper("AA"), 1)
        
    def test_string_with_triple_uppercase_vowels(self):
        self.assertEqual(count_upper("AAA"), 1)
        
    def test_string_with_four_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAA"), 1)
        
    def test_string_with_five_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAAAAAA"), 1)
        
    def test_string_with_six_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAAAAAAAA"), 1)
        
    def test_string_with_seven_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAAAAAAAAA"), 1)
        
    def test_string_with_eight_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAAAAAAAAAA"), 1)
        
    def test_string_with_nine_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAAAAAAAAAAAAAA"), 1)
        
    def test_string_with_ten_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAAAAAAAAAAAAAAAA"), 1)
        
    def test_string_with_eleven_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAAAAAAAAAAAAAAAAAA"), 1)
        
    def test_string_with_twelve_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAAAAAAAAAAAAAAAAAAAAAA"), 1)
        
    def test_string_with_thirteen_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAAAAAAAAAAAAAAAAAAAAAAAAAA"), 1)
        
    def test_string_with_fourteen_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"), 1)
        
    def test_string_with_fifteen_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"), 1)
        
    def test_string_with_sixteen_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"), 1)
        
    def test_string_with_seventeen_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"), 1)
        
    def test_string_with_eighteen_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"), 1)
        
    def test_string_with_nineteen_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"), 1)
        
    def test_string_with_twenty_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"), 1)
        
    def test_string_with_twenty_one_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"), 1)
        
    def test_string_with_twenty_two_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"), 1)
        
    def test_string_with_twenty_three_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"), 1)
        
    def test_string_with_twenty_four_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"), 1)
        
    def test_string_with_twenty_five_or_more_uppercase_vowels(self):
        self.assertEqual(count_upper("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"), 1)
        
    def test_string_with_twenty_six_or_more_uppercase_vowels(self):
        self.assertEqual(count