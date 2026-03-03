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
   - Include from HumanEval_63_code import fibfib
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
2. Include: from HumanEval_63_code import fibfib
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)


assistant

import unittest

# Importing the fibfib function from the given module
from HumanEval_63_code import fibfib

class TestFibFib(unittest.TestCase):
    def test_fibfib_zero(self):
        self.assertEqual(fibfib(0), 0)

    def test_fibfib_one(self):
        self.assertEqual(fibfib(1), 0)

    def test_fibfib_two(self):
        self.assertEqual(fibfib(2), 1)

    def test_fibfib_three(self):
        self.assertEqual(fibfib(3), 2)

    def test_fibfib_four(self):
        self.assertEqual(fibfib(4), 4)

    def test_fibfib_five(self):
        self.assertEqual(fibfib(5), 7)

    def test_fibfib_six(self):
        self.assertEqual(fibfib(6), 13)

    def test_fibfib_seven(self):
        self.assertEqual(fibfib(7), 24)

    def test_fibfib_eight(self):
        self.assertEqual(fibfib(8), 44)

    def test_fibfib_nine(self):
        self.assertEqual(fibfib(9), 74)

    def test_fibfib_ten(self):
        self.assertEqual(fibfib(10), 112)

if __name__ == '__main__':
    unittest.main()