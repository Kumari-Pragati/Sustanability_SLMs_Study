### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_122_code import add_elements
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
2. Include: from HumanEval_122_code import add_elements
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)

 import unittest

from HumanEval_122_code import add_elements

class TestAddElements(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4), 24)
        self.assertEqual(add_elements([1, 2, 3, 400, 5, 6, 7, 8, 9], 8), 21)
        self.assertEqual(add_elements([11, 2, 3, 40, 5, 6, 7, 8, 9], 7), 13)

    def test_edge_cases(self):
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 1), 21)
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 100), 21)
        self.assertEqual(add_elements([], 4), 0)
        self.assertEqual(add_elements([1, 2, 3, 4000, 5, 6, 7, 8, 9], 0), 0)
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 5), 21)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, add_elements, [1, 2, 3], -1)
        self.assertRaises(ValueError, add_elements, [1, 2, 3], len([1, 2, 3]) + 1)
        self.assertRaises(ValueError, add_elements, [1, 2, 3], 0)
        self.assertRaises(TypeError, add_elements, [1, 2, 3], "k")
        self.assertRaises(TypeError, add_elements, [1, 2, 3, 4], 5.5)

if __name__ == '__main__':
    unittest.main()