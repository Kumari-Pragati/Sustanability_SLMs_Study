### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_5_code import intersperse
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
2. Include: from HumanEval_5_code import intersperse
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result: List[int] = []
    for i, x in enumerate(numbers):
        result.append(x)
        if i != len(numbers) - 1:
            result.append(delimeter)
    return result

 import unittest

from HumanEval_5_code import intersperse

class TestIntersperse(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element_list(self):
        self.assertEqual(intersperse([1], 4), [1, 4])

    def test_multiple_elements_list(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_negative_numbers(self):
        self.assertEqual(intersperse([-1, -2, -3], 4), [-1, 4, -2, 4, -3])

    def test_mixed_numbers(self):
        self.assertEqual(intersperse([1, -2, 3], 4), [1, 4, -2, 4, 3])

    def test_large_numbers(self):
        self.assertEqual(intersperse([1000, 2000, 3000], 4), [1000, 4, 2000, 4, 3000])

    def test_zero_delimeter(self):
        self.assertEqual(intersperse([1, 2, 3], 0), [1, 2, 3])

    def test_delimeter_larger_than_numbers(self):
        self.assertEqual(intersperse([1, 2, 3], 10), [1, 10, 2, 10, 3])

    def test_delimeter_negative(self):
        self0self.assertEqual(intersperse([1, 2, 3], -4), [1, -4, 2, -4, 3])

    def test_delimeter_float(self):
        self.assertEqual(intersperse([1, 2, 3], 3.5), [1, 3.5, 2, 3.5, 3])

    def test_delimeter_complex(self):
        self.assertEqual(intersperse([1, 2, 3], complex(4, 5)), [1, complex(4, 5), 2, complex(4, 5), 3])

if __name__ == '__main__':
    unittest.main()