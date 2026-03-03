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
   - Include from HumanEval_65_code import circular_shift
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
2. Include: from HumanEval_65_code import circular_shift
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]


assistant

import unittest

from HumanEval_65_code import circular_shift

class TestCircularShift(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(circular_shift(12, 1), "21")
        self.assertEqual(circular_shift(12, 2), "12")

    def test_edge_case_large_shift(self):
        self.assertEqual(circular_shift(12345, 5), "54321")
        self.assertEqual(circular_shift(12345, 7), "54321")

    def test_edge_case_zero_shift(self):
        self.assertEqual(circular_shift(12345, 0), "12345")

    def test_edge_case_negative_shift(self):
        self.assertEqual(circular_shift(-12345, -1), "-54321")
        self.assertEqual(circular_shift(-12345, -2), "-12345")

    def test_edge_case_string_input(self):
        self.assertEqual(circular_shift("abc", 1), "cba")
        self.assertEqual(circular_shift("abc", 2), "cba")

    def test_edge_case_empty_string(self):
        self.assertEqual(circular_shift("", 1), "")
        self.assertEqual(circular_shift("", 2), "")

if __name__ == '__main__':
    unittest.main()