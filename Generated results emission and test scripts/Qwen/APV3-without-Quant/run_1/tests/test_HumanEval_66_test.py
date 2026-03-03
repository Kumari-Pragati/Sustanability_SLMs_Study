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
   - Include from HumanEval_66_code import digitSum
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
2. Include: from HumanEval_66_code import digitSum
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    if s == "":
        return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)


assistant

import unittest

from HumanEval_66_code import digitSum

class TestDigitSum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(digitSum(""), 0)
        self.assertEqual(digitSum("abAB"), 131)
        self.assertEqual(digitSum("abcCd"), 67)
        self.assertEqual(digitSum("helloE"), 69)
        self.assertEqual(digitSum("woArBld"), 131)
        self.assertEqual(digitSum("aAaaaXa"), 153)

    def test_edge_cases(self):
        self.assertEqual(digitSum(" "), 0)
        self.assertEqual(digitSum("a"), 97)
        self.assertEqual(digitSum("Z"), 90)
        self.assertEqual(digitSum("ZZZ"), 270)

    def test_invalid_input(self):
        self.assertEqual(digitSum(None), 0)
        self.assertEqual(digitSum(123), 0)
        self.assertEqual(digitSum(True), 0)
        self.assertEqual(digitSum(False), 0)

if __name__ == '__main__':
    unittest.main()