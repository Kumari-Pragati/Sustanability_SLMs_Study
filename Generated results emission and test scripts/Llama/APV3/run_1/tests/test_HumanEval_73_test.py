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
   - Include from HumanEval_73_code import smallest_change
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
    unittest.main()user

### Immediate Task
Write the complete unittest test suite for the following Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_73_code import smallest_change
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
        smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
        smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
        smallest_change([1, 2, 3, 2, 1]) == 0
    """
    ans = 0
    for i in range(len(arr) // 2):
        if arr[i]!= arr[len(arr) - i - 1]:
            ans += 1
    return ansassistant

import unittest
from HumanEval_73_code import smallest_change

class TestSmallestChange(unittest.TestCase):
    def test_palindromic_array(self):
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)

    def test_non_palindromic_array(self):
        self.assertEqual(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]), 4)

    def test_array_with_one_element(self):
        self.assertEqual(smallest_change([1]), 0)

    def test_array_with_two_elements(self):
        self.assertEqual(smallest_change([1, 2]), 1)

    def test_array_with_three_elements(self):
        self.assertEqual(smallest_change([1, 2, 3]), 2)

    def test_array_with_four_elements(self):
        self.assertEqual(smallest_change([1, 2, 3, 4]), 2)

    def test_array_with_five_elements(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 3]), 1)

    def test_array_with_six_elements(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2]), 1)

    def test_array_with_seven_elements(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)

    def test_array_with_eight_elements(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2, 1]), 1)

if __name__ == '__main__':
    unittest.main()