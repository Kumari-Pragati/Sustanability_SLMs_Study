### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_85_code import add
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
2. Include: from HumanEval_85_code import add
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def add(lst):
    """Given a non-empty list of integers lst. Add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0])

 import unittest

from HumanEval_85_code import add

class TestAddFunction(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)

    def test_empty_list(self):
        self.assertEqual(add([]), 0)

    def test_all_odd_indices(self):
        self.assertEqual(add([1, 3, 5, 7]), 0)

    def test_all_even_indices(self):
        self.assertEqual(add([2, 4, 6, 8]), 12)

    def test_mixed_indices(self):
        self.assertEqual(add([1, 2, 3, 4]), 2)

    def test_no_even_at_odd_indices(self):
        self.assertEqual(add([1, 3, 5, 7]), 0)

    def test_negative_numbers(self):
        self.assertEqual(add([-2, -4, -6, -8]), -12)

if __name__ == '__main__':
    unittest.main()