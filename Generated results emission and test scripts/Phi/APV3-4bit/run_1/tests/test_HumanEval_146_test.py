### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_146_code import specialFilter
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
2. Include: from HumanEval_146_code import specialFilter
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            odd_digits = (1, 3, 5, 7, 9)
            number_as_string = str(num)
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                count += 1
    return count

 import unittest

from HumanEval_146_code import specialFilter

class TestSpecialFilter(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)

    def test_negative_numbers(self):
        self.assertEqual(specialFilter([-33, -2, -3, 45, 21, 109]), 1)

    def test_zero_numbers(self):
        self.assertEqual(specialFilter([]), 0)

    def test_single_element(self):
        self.assertEqual(specialFilter([11]), 1)

    def test_no_qualifying_numbers(self):
        self.assertEqual(specialFilter([12, 14, 16]), 0)

    def test_all_qualifying_numbers(self):
        self.assertEqual(specialFilter([11, 33, 55, 77, 99]), 5)

    def test_edge_case_with_negative_numbers(self):
        self.assertEqual(specialFilter([-11, -33, -55, -77, -99]), 1)

    def test_edge_case_with_single_element(self):
        self.assertEqual(specialFilter([-11]), 1)

    def test_edge_case_with_zero_numbers(self):
        self.assertEqual(specialFilter([]), 0)

if __name__ == '__main__0':
    unittest.main()