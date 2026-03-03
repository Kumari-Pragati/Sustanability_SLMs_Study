### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_145_code import order_by_points
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
2. Include: from HumanEval_145_code import order_by_points
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    def digits_sum(n):
        neg = 1
        if n < 0:
            n, neg = -1 * n, -1
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)

    return sorted(nums, key=digits_sum)

 import unittest

from HumanEval_145_code import order_by_points

class TestOrderByPoints(unittest.TestCase):
    def test_normal_inputs(self):
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])
        self.assertEqual(order_by_points([10, 11, 9, 8, 7]), [8, 9, 10, 11, 7])
        self.assertEqual(order_by_points([0, 0, 0]), [0, 0, 0])

    def test_edge_inputs(self):
        self.assertEqual(order_by_points([-1000000000000000000]), [-1000000000000000000])
        self.assertEqual(order_by_points([1000000000000000000]), [1000000000000000000])
        self.assertEqual(order_by_points([-1, 0, 1]), [-1, 0, 1])
        self.assertEqual(order_by_points([0, -1, 1]), [0, -1, 1])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, lambda: order_by_points(1.5))
        self.assertRaises(TypeError, lambda: order_by_points({"a": 1}))
        self.assertRaises(TypeError, lambda: order_by_points([1, "b"]))

if __name__ == '__main__':
    unittest.main()