### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_75_code import is_multiply_prime
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
2. Include: from HumanEval_75_code import is_multiply_prime
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less than 100. 
    Example:
        is_multiply_prime(30) == True
        30 = 2 * 3 * 5
    """

    def is_prime(n):
        for j in range(2, n):
            if n % j == 0:
                return False
        return True

    for i in range(2, 101):
        if not is_prime(i):
            continue
        for j in range(2, 101):
            if not is_prime(j):
                continue
            for k in range(2, 101):
                if not is_prime(k):
                    continue
                if i * j * k == a:
                    return True
    return False

 import unittest
from HumanEval_75_code import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):

    def test_multiplication_of_primes(self):
        self.assertTrue(is_multiply_prime(30))
        self.assertTrue(is_multiply_prime(210))
        self.assertTrue(is_multiply_prime(2310))

    def test_not_multiplication_of_primes(self):
        self.assertFalse(is_multiply_prime(1))
        self.assertFalse(is_multiply_prime(4))
        self.assertFalse(is_multiply_prime(100))
        self.assertFalse(is_multiply_prime(101))

    def test_edge_cases(self):
        self.assertTrue(is_multiply_prime(2))
        self.assertTrue(is_multiply_prime(3))
        self.assertTrue(is_multiply_prime(5))
        self.assertTrue(is_multiply_prime(7))
        self.assertTrue(is_multiply_prime(11))
        self.assertTrue(is_multiply_prime(13))
        self.assertTrue(is_multiply_prime(17))
        self.assertTrue(is_multiply_prime(19))
        self.assertTrue(is_multiply_prime(23))
        self.assertTrue(is_multiply_prime(29))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_multiply_prime("not a number")
        with self.assertRaises(TypeError):
            is_multiply_prime([2, 3, 5])
        with self.assertRaises(TypeError):
            is_multiply_prime({2, 3, 5})

if __name__ == '__main__':
    unittest.main()