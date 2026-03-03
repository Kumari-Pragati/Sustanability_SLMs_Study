### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_92_code import any_int
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
2. Include: from HumanEval_92_code import any_int
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    any_int(3, 2, 2) ➞ False
    any_int(3, -2, 1) ➞ True
    any_int(3.6, -2.2, 2) ➞ False
    '''

    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if (x + y == z) or (x + z == y) or (y + z == x):
            return True
        return False
    return False

 import unittest
from HumanEval_92_code import any_int

class TestAnyIntFunction(unittest.TestCase):
    def test_positive_integers(self):
        self.assertTrue(any_int(5, 2, 7))
        self.assertFalse(any_int(3, 2, 2))
        self.assertTrue(any_int(3, -2, 1))

    def test_negative_integers(self):
        self.assertTrue(any_int(-1, -2, -3))
        self.assertFalse(any_int(-1, -2, -4))

    def test_zero_integers(self):
        self.assertTrue(any_int(0, 0, 0))
        self.assertFalse(any_int(0, 0, 1))

    def test_non_integer_values(self):
        self.assertFalse(any_int(5, 2, 7.0))
        self.assertFalse(any_int(3, 2, 2.2))
        self.assertFalse(any_int(3.6, -2.2, 2))

    def test_all_integers_are_zero(self):
        self.assertFalse(any_int(0, 0, 0))

    def test_two_numbers_are_zero(self):
        self.assertFalse(any_int(0, 0, 1))

    def test_two_numbers_are_equal(self):
        self.assertFalse(any_int(3, 3, 3))

if __name__ == '__main__':
    unittest.main()