### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_69_code import search
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
2. Include: from HumanEval_69_code import search
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such value exists, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    frq = [0] * (max(lst) + 1)
    for i in lst:
        frq[i] += 1

    ans = -1
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i

    return ans

 import unittest
from HumanEval_69_code import search

class TestSearchFunction(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)

    def test_frequency_greater_than_value(self):
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)

    def test_no_value_found(self):
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)

    def test_single_element_list(self):
        self.assertEqual(search([1]), 1)

    def test_all_elements_same(self):
        self.assertEqual(search([3, 3, 3, 3]), 3)

    def test_empty_list(self):
        self.assertEqual(search([]), -1)

    def test_all_elements_zero(self):
        self.assertEqual(search([0, 0, 0]), -1)

    def test_all_elements_negative(self):
        self.assertEqual(search([-1, -1, -1]), -1)

    def test_all_elements_positive(self):
        self.assertEqual(search([1, 1, 1]), 1)

    def test_large_numbers(self):
        self.assertEqual(search([1000, 1000, 1000]), 1000)

    def test_large_numbers_with_smaller_frequency(self):
        self.assertEqual(search([1000, 1000, 999]), -1)

if __name__ == '__main__':
    unittest.main()