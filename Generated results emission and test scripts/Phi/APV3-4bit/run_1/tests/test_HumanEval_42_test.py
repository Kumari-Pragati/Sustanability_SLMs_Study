### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_42_code import incr_list
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
2. Include: from HumanEval_42_code import incr_list
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [e + 1 for e in l]

 import unittest

from HumanEval_42_code import incr_list

class TestIncrList(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])

    def test_large_input(self):
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

    def test_empty_list(self):
        self.assertEqual(incr_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(incr_list([1]), [2])

    def test_all_elements_incremented(self):
        self.assertEqual(incr_list([-1, -2, -3]), [-2, -3, -4])

    def test_all_elements_incremented_with_zero(self):
        self.assertEqual(incr_list([0, 0, 0]), [1, 1, 1])

    def test_all_elements_incremented_with_negative_zero(self):
        self.assertEqual(incr_list([-0, -0, -0]), [-1, -1, -1])

    def test_all_elements_incremented_with_decimal(self):
        self.assertEqual(incr_list([0.5, 0.5, 0.5]), [1.5, 1.5, 1.5])

    def test_all_elements_incremented_with_complex(self):
        self.assertEqual(incr_list([complex(1, 1), complex(1, 1), complex(1, 1)]), [complex(2, 1), complex(2, 1), complex(2, 1)])

    def test_all_elements_incremented_with_string(self):
        with self.assertRaises(TypeError):
            incr_list(["a", "b", "c"])

if __name__ == '__main__':
    unittest.main()