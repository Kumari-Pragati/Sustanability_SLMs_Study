### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_47_code import median
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
2. Include: from HumanEval_47_code import median
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0

 import unittest

from HumanEval_47_code import median

class TestMedianFunction(unittest.TestCase):

    def test_even_length_list(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)

    def test_odd_length_list(self):
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            median([])

    def test_single_element_list(self):
        self.assertEqual(median([7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(median([-10, -4, -6, -1000, -10, -20]), -6.0)

    def test_positive_numbers(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)

    def test_mixed_numbers(self):
        self.assertEqual(median([3, 1, 2, 4, 5, -10]), 3)

    def test_large_numbers(self):
        self.assertEqual(median([1000000, 2000000, 3000000, 4000000, 5000000]), 3000000)

    def test_floating_point_numbers(self):
        self.assertEqual(median([1.5, 2.3, 3.1, 4.7]), 2.7)

    def test_already_sorted_list(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)

    def test_reverse_sorted_list(self):
        self.assertEqual(median([5, 4, 3, 2, 1]), 3)

    def test_duplicate_elements(self):
        self.assertEqual(median([1, 2, 2, 3, 4]), 2)

    def test_uneven_length_list(self):
        self.assertEqual(median([3, 1, 2, 4]), 2.5)

if __name__ == '__main__':
    unittest.main()