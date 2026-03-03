### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_108_code import count_nums
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
2. Include: from HumanEval_108_code import count_nums
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """

    def digits_sum(n):
        neg = 1
        if n < 0:
            n, neg = -1 * n, -1
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)

    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))

 import unittest
from HumanEval_108_code import count_nums

class TestCountNums(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_nums([]), 0)

    def test_single_positive_number(self):
        self.assertEqual(count_nums([1]), 1)

    def test_single_negative_number(self):
        self.assertEqual(count_nums([-1]), 1)

    def test_multiple_positive_numbers(self):
        self.assertEqual(count_nums([1, 11, 111]), 3)

    def test_multiple_negative_numbers(self):
        self.assertEqual(count_nums([-1, -11, -111]), 3)

    def test_mixed_numbers(self):
        self.assertEqual(count_nums([1, -1, 11, -11]), 4)

    def test_zero_numbers(self):
        self.assertEqual(count_nums([0, 0, 0]), 0)

    def test_large_numbers(self):
        self.assertEqual(count_nums([1000, 10000, -10000]), 3)

    def test_edge_case_with_single_digit(self):
        self.assertEqual(count_nums([1, -1, 9]), 3)

    def test_edge_case_with_multiple_single_digits(self):
        self.assertEqual(count_nums([1, 2, 3, -4, -5]), 5)

if __name__ == '__main__':
    unittest.main()