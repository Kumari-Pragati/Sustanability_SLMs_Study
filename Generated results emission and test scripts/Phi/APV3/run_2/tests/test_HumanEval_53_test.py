### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_53_code import add
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
2. Include: from HumanEval_53_code import add
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y

 import unittest

from HumanEval_53_code import add

class TestAddFunction(unittest.TestCase):

    def test_positive_integers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

    def test_negative_integers(self):
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(-5, -7), -12)

    def test_zero_integers(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, -0), 0)

    def test_positive_and_negative_integers(self):
        self.assertEqual(add(-1, 2), 1)
        self.assertEqual(add(2, -3), -1)

    def test_large_integers(self):
        self.assertEqual(add(1000000, 2000000), 3000000)

    def test_edge_case_integers(self):
        self.assertEqual(add(Integer.MAX_VALUE, 1), Integer.MAX_VALUE)
        self.assertEqual(add(-1, Integer.MIN_VALUE), -1)

if __name__ == '__main__':
    unittest.main()