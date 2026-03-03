### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_135_code import can_arrange
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
2. Include: from HumanEval_135_code import can_arrange
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    ind = -1
    i = 1
    while i < len(arr):
        if arr[i] < arr[i - 1]:
            ind = i
        i += 1
    return ind

 import unittest
from HumanEval_135_code import can_arrange

class TestCanArrange(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(can_arrange([1, 2, 4, 3, 5]), 3)

    def test_no_element_greater_than_preceding(self):
        self.assertEqual(can_arrange([1, 2, 3]), -1)

    def test_all_elements_increasing(self):
        self.assertEqual(can_arrange([1, 2, 3, 4, 5]), -1)

    def test_all_elements_decreasing(self):
        self.assertEqual(can_arrange([5, 4, 3, 2, 1]), -1)

    def test_single_element_array(self):
        self.assertEqual(can_arrange([1]), -1)

    def test_duplicate_elements_array(self):
        with self.assertRaises(ValueError):
            can_arrange([1, 1, 2])

if __name__ == '__main__':
    unittest.main()