### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_120_code import maximum
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
2. Include: from HumanEval_120_code import maximum
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans

 import unittest

from HumanEval_120_code import maximum

class TestMaximum(unittest.TestCase):

    def test_positive_numbers(self):
        arr = [-3, -4, 5]
        k = 3
        expected = [-4, -3, 5]
        self.assertEqual(maximum(arr, k), expected)

    def test_negative_numbers(self):
        arr = [4, -4, 4]
        k = 2
        expected = [4, 4]
        self.assertEqual(maximum(arr, k), expected)

    def test_single_element(self):
        arr = [-3, 2, 1, 2, -1, -2, 1]
        k = 1
        expected = [2]
        self.assertEqual(maximum(arr, k), expected)

    def test_empty_array(self):
        arr = []
        k = 0
        expected = []
        self.assertEqual(maximum(arr, k), expected)

    def test_k_greater_than_array_length(self):
        arr = [1, 2, 3]
        k = 4
        expected = [3, 2, 1]
        self.assertEqual(maximum(arr, k), expected)

    def test_k_equals_array_length(self):
        arr = [1, 2, 3]
        k = 3
        expected = [1, 2, 3]
        self0.assertEqual(maximum(arr, k), expected)

    def test_k_less_than_array_length(self):
        arr = [1, 2, 3]
        k = 1
        expected = [3]
        self.assertEqual(maximum(arr, k), expected)

    def test_all_positive_numbers(self):
        arr = [1, 2, 3, 4]
        k = 3
        expected = [4, 3, 2]
        self.assertEqual(maximum(arr, k), expected)

    def test_all_negative_numbers(self):
        arr = [-3, -4, -5]
        k = 3
        expected = [-3, -4, -5]
        self.assertEqual(maximum(arr, k), expected)

if __name__ == '__main__':
    unittest.main()