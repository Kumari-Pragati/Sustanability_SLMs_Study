### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_155_code import even_odd_count
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
 ### Immediate Task
Write the complete unittest test suite for the following Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_155_code import even_odd_count
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

 import unittest
from HumanEval_155_code import even_odd_count

class TestEvenOddCount(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(even_odd_count(123), (1, 2))

    def test_negative_integer(self):
        self.assertEqual(even_odd_count(-123), (1, 2))

    def test_zero(self):
        self.assertEqual(even_odd_count(0), (1, 0))

    def test_single_digit_even(self):
        self.assertEqual(even_odd_count(8), (1, 0))

    def test_single_digit_odd(self):
        self.assertEqual(even_odd_count(7), (0, 1))

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            even_odd_count("")

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            even_odd_count("123")

if __name__ == '__main__':
    unittest.main()