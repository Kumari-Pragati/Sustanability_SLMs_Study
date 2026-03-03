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
   - Include from HumanEval_55_code import fib
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
2. Include: from HumanEval_55_code import fib
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


assistant

import unittest

from HumanEval_55_code import fib

class TestFibonacci(unittest.TestCase):
    def test_fib_zero(self):
        self.assertEqual(fib(0), 0)

    def test_fib_one(self):
        self.assertEqual(fib(1), 1)

    def test_fib_large(self):
        # Large numbers should overflow due to integer limitations
        large_number = 1000000
        result = fib(large_number)
        self.assertTrue(result > 10**9, "Result should exceed 1 billion")

    def test_fib_edge_cases(self):
        # Edge cases like negative numbers or non-integer values should raise exceptions
        with self.assertRaises(ValueError):
            fib(-1)
        
        with self.assertRaises(TypeError):
            fib("a")


This test suite includes three tests:
1. `test_fib_zero` checks that the function returns 0 when given 0 as input.
2. `test_fib_one` checks that the function returns 1 when given 1 as input.
3. `test_fib_large` checks that the function correctly handles very large inputs by checking if the result exceeds 1 billion.

The other two tests (`test_fib_edge_cases`) check for potential issues such as raising a ValueError for negative numbers or TypeError for non-integer inputs.