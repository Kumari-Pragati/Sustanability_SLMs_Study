### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_151_code import double_the_difference
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
2. Include: from HumanEval_151_code import double_the_difference
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    return sum([i**2 for i in lst if i > 0 and i % 2 != 0 and "." not in str(i)])

 import unittest
from HumanEval_151_code import double_the_difference

class TestDoubleTheDifference(unittest.TestCase):
    def test_positive_odd_integers(self):
        self.assertEqual(double_the_difference([1, 3, 5]), 25)

    def test_positive_odd_integers_with_zero(self):
        self.assertEqual(double_the_difference([1, 3, 0]), 10)

    def test_negative_integers(self):
        self.assertEqual(double_the_difference([-1, -3, -5]), 0)

    def test_mixed_integers(self):
        self.assertEqual(double_the_difference([1, 2, 3, 4, 5]), 25)

    def test_mixed_integers_with_zero(self):
        self.assertEqual(double_the_difference([1, 2, 3, 0, 5]), 25)

    def test_mixed_integers_with_non_integer(self):
        self.assertEqual(double_the_difference([1, 2, 3, 4.5, 5]), 25)

    def test_empty_list(self):
        self.assertEqual(double_the_difference([]), 0)

    def test_list_with_only_even_integers(self):
        self.assertEqual(double_the_difference([2, 4, 6]), 0)

    def test_list_with_only_non_integers(self):
        self.assertEqual(double_the_difference([1.5, 2.3, 3.7]), 0)

    def test_list_with_only_negative_integers(self):
        self.assertEqual(double_the_difference([-1, -3, -5]), 0)

    def test_list_with_mixed_types(self):
        self.assertEqual(double_the_difference([1, 'a', 3.0, -2]), 1)

if __name__ == '__main__':
    unittest.main()