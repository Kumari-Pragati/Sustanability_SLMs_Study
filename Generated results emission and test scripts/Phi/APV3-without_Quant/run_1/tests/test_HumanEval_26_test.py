### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_26_code import remove_duplicates
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
2. Include: from HumanEval_26_code import remove_duplicates
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]

 
import unittest
from HumanEval_26_code import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplicates([5]), [5])

    def test_all_elements_duplicates(self):
        self.assertEqual(remove_duplicates([2, 2, 2, 2]), [])

    def test_no_duplicates(self):
        self.assertEqual(remove_duplicates([1, 3, 5, 7]), [1, 3, 5, 7])

    def test_mixed_integers(self):
        self.assertEqual(remove_duplicates([1, -1, 2, -2, 3, -3]), [1, -1, 2, -2, 3, -3])

    def test_negative_integers(self):
        self.assertEqual(remove_duplicates([-1, -2, -3, -1]), [-2, -3])

    def test_large_numbers(self):
        self.assertEqual(remove_duplicates([1000000, 2000000, 3000000, 2000000]), [1000000, 3000000])

    def test_zero_list(self):
        self.assertEqual(remove_duplicates([0, 0, 0, 0]), [0])

    def test_non_integer_list(self):
        with self.assertRaises(TypeError):
            remove_duplicates([1, 'a', 2])

if __name__ == '__main__':
    unittest.main()