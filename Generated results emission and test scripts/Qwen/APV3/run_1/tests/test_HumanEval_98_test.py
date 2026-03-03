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
    def test_positive_numbers(self):
        self.assertEqual(count_upper('aBCdEf'), 1)
        
    def test_negative_numbers(self):
        self.assertEqual(count_upper('abcdefg'), 0)
        
    def test_empty_string(self):
        self.assertEqual(count_upper(""), 0)
        
    def test_single_char(self):
        self.assertEqual(count_upper("A"), 1)
        
    def test_all_lower_case(self):
        self.assertEqual(count_upper("bcdfgh"), 0)
        
    def test_all_upper_case(self):
        self.assertEqual(count_upper("ABCDEFG"), 7)
        
    def test_mixed_case(self):
        self.assertEqual(count_upper("ABCD EFGH"), 2)
        
if __name__ == '__main__':
    unittest.main()