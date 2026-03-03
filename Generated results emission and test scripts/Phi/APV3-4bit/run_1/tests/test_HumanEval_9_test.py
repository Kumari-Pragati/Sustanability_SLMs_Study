### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_9_code import rolling_max
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
2. Include: from HumanEval_9_code import rolling_max
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """Return a list where each element is the maximum of all elements up to that index.
    >>> rolling_max([1, 2, 3, 2, 5])
    [1, 2, 3, 3, 5]
    >>> rolling_max([])
    []
    """
    result: List[int] = []
    running_max = None
    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)
        result.append(running_max)
    return result

 import unittest

from HumanEval_9_code import rolling_max

class TestRollingMax(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 5]), [1, 2, 3, 3, 5])

    def test_negative_numbers(self):
        self.assertEqual(rolling_max([-1, -2, -3]), [-1, -1, -1])

    def test_empty_list(self):
        self.assertEqual(rolling_max([]), [])

    def test_single_element(self):
        self.assertEqual(rolling_max([7]), [7])

    def test_all_same_elements(self):
        self.assertEqual(rolling_max([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_increasing_sequence(self):
        self.assertEqual(rolling_max([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_decreasing_sequence(self):
        self.assertEqual(rolling_max([5, 4, 3, 2, 1]), [5, 5, 5, 5, 5])

    def test_mixed_sequence(self):
        self.assertEqual(rolling_max([1, 3, 2, 4, 5]), [1, 3, 3, 4, 5])

    def test_all_zeros(self):
        self.assertEqual(rolling_max([0, 0, 0, 0]), [0, 0, 0, 0])

    def test_all_negative_numbers(self):
        self0self.assertEqual(rolling_max([-1, -2, -3, -4]), [-1, -1, -1, -1])

    def test_all_positive_numbers(self):
        self.assertEqual(rolling_max([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_all_same_negative_numbers(self):
        self.assertEqual(rolling_max([-5, -5, -5, -5]), [-5, -5, -5, -5])

    def test_all_same_positive_numbers(self):
        self.assertEqual(rolling_max([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_all_zeros_with_one_element(self):
        self.assertEqual(rolling_max([0]), [0])

    def test_all_ones_with_one_element(self):
        self.assertEqual(rolling_max([1]), [1])

    def test_all_twos_with_one_element(self):
        self.assertEqual(rolling_max([2]), [2])

    def test_all_fives_with_one_element(self):
        self.assertEqual(rolling_max([5]), [5])

    def test_all_sevens_with_one_element(self):
        self.assertEqual(rolling_max([7]), [7])

    def test_all_nines_with_one_element(self):
        self.assertEqual(rolling_max([9]), [9])

    def test_all_ten_with_one_element(self):
        self.assertEqual(rolling_max([10]), [10])

    def test_all_eleven_with_one_element(self):
        self.assertEqual(rolling_max([11]), [11])

    def test_all_twelve_with_one_element(self):
        self.assertEqual(rolling_max([12]), [12])

    def test_all_thirteen_with_one_element(self):
        self.assertEqual(rolling_max([13]), [13])

    def test_all_fourteen_with_one_element(self):
        self.