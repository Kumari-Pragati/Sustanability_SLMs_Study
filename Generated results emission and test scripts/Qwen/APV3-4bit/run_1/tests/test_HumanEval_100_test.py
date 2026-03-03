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
   - Include from HumanEval_100_code import make_a_pile
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

user
### Immediate Task
Write the complete unittest test suite for the following Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_100_code import make_a_pile
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """

    return [n + 2*i for i in range(n)]


assistant

import unittest

from HumanEval_100_code import make_a_pile

class TestMakeAPile(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])

    def test_edge_case_odd_n(self):
        # Edge case: when n is odd, the second level should also be odd
        self.assertEqual(make_a_pile(5), [5, 7, 9, 11, 13])

    def test_edge_case_even_n(self):
        # Edge case: when n is even, the second level should also be even
        self.assertEqual(make_a_pile(4), [4, 6, 8, 10])

    def test_invalid_input(self):
        # Invalid input: negative numbers should raise an error
        with self.assertRaises(ValueError):
            make_a_pile(-1)

        # Invalid input: non-integer values should raise an error
        with self.assertRaises(TypeError):
            make_a_pile("a")

if __name__ == '__main__':
    unittest.main()


This solution includes a test suite that covers normal cases, edge cases, and invalid inputs as per the requirements. It uses the `unittest` framework to run the tests.