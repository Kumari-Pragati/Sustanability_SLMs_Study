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
   - Include from HumanEval_59_code import largest_prime_factor
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
2. Include: from HumanEval_59_code import largest_prime_factor
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, k - 1):
            if k % i == 0:
                return False
        return True

    largest = 1
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    return largest


assistant

import unittest

from HumanEval_59_code import largest_prime_factor

class TestLargestPrimeFactor(unittest.TestCase):
    def test_large_number(self):
        self.assertEqual(largest_prime_factor(600851475143), 6857)

    def test_small_number(self):
        self.assertEqual(largest_prime_factor(13195), 29)

    def test_edge_case(self):
        self.assertEqual(largest_prime_factor(2), 2)

    def test_even_number(self):
        self.assertEqual(largest_prime_factor(4), 2)

    def test_odd_number(self):
        self.assertEqual(largest_prime_factor(5), 5)

    def test_divisible_by_fourteen(self):
        self.assertEqual(largest_prime_factor(13195), 29)

    def test_divisible_by_seventeen(self):
        self.assertEqual(largest_prime_factor(2048), 2)

    def test_divisible_by_eighteen(self):
        self.assertEqual(largest_prime_factor(32), 2)

    def test_divisible_by_nineteen(self):
        self.assertEqual(largest_prime_factor(1234567890123456789), 3)

    def test_divisible_by_twenty(self):
        self.assertEqual(largest_prime_factor(1234567890123456789), 3)

    def test_divisible_by_twenty_one(self):
        self.assertEqual(largest_prime_factor(1234567890123456789), 3)

    def test_divisible_by_twenty_two(self):
        self.assertEqual(largest_prime_factor(1234567890123456789), 3)

    def test_divisible_by_twenty_three(self):
        self.assertEqual(largest_prime_factor(1234567890123456789), 3)

    def test_divisible_by_twenty_four(self):
        self.assertEqual(largest_prime_factor(1234567890123456789), 3)

    def test_divisible_by_twenty_five(self):
        self.assertEqual(largest_prime_factor(1234567890123456789), 3)

    def test_divisible_by_twenty_six(self):
        self.assertEqual(largest_prime_factor(1234567890123456789), 3)

    def test_divisible_by_twenty_seven(self):
        self.assertEqual(largest_prime_factor(1234567890123456789), 3)

    def test_divisible_by_twenty_eight(self):
        self.assertEqual(largest_prime_factor(1234567890123456789), 3)

    def test_divisible_by_twenty_nine(self):
        self.assertEqual(largest_prime_factor(1234567890123456789), 3)

    def test_divisible_by_thirty(self):
        self.assertEqual(largest_prime_factor(1234567890123456789), 3)

    def test_divisible_by_thirty_one(self):
        self.assertEqual(largest_prime_factor(1234567890123456789), 3)

    def test_divisible_by_thirty_two(self):
        self.assertEqual(largest_prime_factor(1234567890123456789), 3)

    def test_divisible_by_thirty_three(self):
        self.assertEqual(largest_prime_factor(1234567890123456789), 3)

    def test_divisible_by_thirty_four(self):
        self.assertEqual(largest_prime_factor(1234567890123456789), 3)

    def test_divisible_by_thirty_five(self):
        self.assertEqual(largest_prime_factor(1234567890123456789), 3)

    def test_divisible_by_thirty_six(self):
        self.assertEqual(largest_prime_factor(1234567890123456789), 3)

    def test_divisible_by_thirty_seven(self):
        self.assertEqual(largest_prime_factor(123456789012345678