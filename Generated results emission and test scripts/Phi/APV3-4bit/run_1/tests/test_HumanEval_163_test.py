### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_163_code import generate_integers
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
2. Include: from HumanEval_163_code import generate_integers
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))
    return [i for i in range(lower, upper + 1) if i % 2 == 0]

 
import unittest
from HumanEval_163_code import generate_integers

class TestGenerateIntegers(unittest.TestCase):

    def test_even_digits_ascending_order(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])

    def test_even_digits_ascending_order_reversed(self):
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])

    def test_no_even_digits_in_range(self):
        self.assertEqual(generate_integers(10, 14), [])

    def test_lower_bound_is_at_least_2(self):
        self.assertEqual(generate_integers(1, 8), [2, 4, 6, 8])

    def test_upper_bound_is_at_most_8(self):
        self.assertEqual(generate_integers(2, 10), [2, 4, 6, 8])

    def test_lower_bound_is_at_least_2_with_even_upper_bound(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])

    def test_upper_bound_is_at_most_8_with_even_lower_bound(self):
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])

    def test_lower_bound_is_at_least_2_with_even_upper_bound_reversed(self):
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])

    def test_upper_bound_is_at_most_8_with_even_lower_bound_reversed(self):
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])

    def test_lower_bound_is_at_least_2_with_odd_upper_bound(self):
        self.assertEqual(generate_integers(2, 9), [2, 4, 6])

    def test_upper_bound_is_at_most_8_with_odd_lower_bound(self):
        self.assertEqual(generate_integers(2, 7), [2, 4, 6])

    def test_lower_bound_is_at_least_2_with_odd_upper_bound_reversed(self):
        self.assertEqual(generate_integers(9, 2), [2, 4, 6])

    def test_upper_bound_is_at_most_8_with_odd_lower_bound_reversed(self):
        self.assertEqual(generate_integers(9, 2), [2, 4, 6])

    def test_lower_bound_is_at_least_2_with_upper_bound_at_1(self):
        self.assertEqual(generate_integers(2, 1), [2])

    def test_upper_bound_is_at_most_8_with_upper_bound_at_1_reversed(self):
        self.assertEqual(generate_integers(1, 2), [2])

    def test_lower_bound_is_at_least_2_with_upper_bound_at_1_reversed(self):
        self.assertEqual(generate_integers(1, 2), [2])

if __name__ == '__main__':
    unittest.main()