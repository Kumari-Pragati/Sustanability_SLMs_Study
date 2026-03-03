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

user
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


assistant

import unittest

from HumanEval_75_code import is_prime

def is_multiply_prime(a):
    """
    Write a function that returns true if the given number is the multiplication of 3 prime numbers
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

    primes_found = set()
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
                    primes_found.add((i, j, k))
                    break
    
    return len(primes_found) >= 3

class TestIsMultiplyPrime(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(is_multiply_prime(30))

    def test_negative_numbers(self):
        self.assertFalse(is_multiply_prime(-30))

    def test_zero(self):
        self.assertFalse(is_multiply_prime(0))

    def test_large_number(self):
        self.assertFalse(is_multiply_prime(987654321))

    def test_edge_cases(self):
        # Check for small cases where it should return False
        self.assertFalse(is_multiply_prime(1))
        self.assertFalse(is_multiply_prime(2))
        self.assertFalse(is_multiply_prime(3))
        self.assertFalse(is_multiply_prime(4))
        self.assertFalse(is_multiply_prime(5))
        self.assertFalse(is_multiply_prime(6))
        self.assertFalse(is_multiply_prime(7))
        self.assertFalse(is_multiply_prime(8))
        self.assertFalse(is_multiply_prime(9))
        self.assertFalse(is_multiply_prime(10))
        self.assertFalse(is_multiply_prime(11))
        self.assertFalse(is_multiply_prime(12))
        self.assertFalse(is_multiply_prime(13))
        self.assertFalse(is_multiply_prime(14))
        self.assertFalse(is_multiply_prime(15))
        self.assertFalse(is_multiply_prime(16))
        self.assertFalse(is_multiply_prime(17))
        self.assertFalse(is_multiply_prime(18))
        self.assertFalse(is_multiply_prime(19))
        self.assertFalse(is_multiply_prime(20))
        self.assertFalse(is_multiply_prime(21))
        self.assertFalse(is_multiply_prime(22))
        self.assertFalse(is_multiply_prime(23))
        self.assertFalse(is_multiply_prime(24))
        self.assertFalse(is_multiply_prime(25))
        self.assertFalse(is_multiply_prime(26))
        self.assertFalse(is_multiply_prime(27))
        self.assertFalse(is_multiply_prime(28))
        self.assertFalse(is_multiply_prime(29))
        self.assertFalse(is_multiply_prime(30))
        self.assertFalse(is_multiply_prime(31))
        self.assertFalse(is_multiply_prime(32))
        self.assertFalse(is_multiply_prime(33))
        self.assertFalse(is_multiply_prime(34))
        self.assertFalse(is_multiply_prime(35))
        self.assertFalse(is_multiply_prime(36))
        self.assertFalse(is_multiply_prime(37))
        self.assertFalse(is_multiply_prime(38))
        self.assertFalse(is_multiply_prime(39))
        self.assertFalse(is_multiply_prime(40))
        self.assertFalse(is_multiply_prime(41))
        self.assertFalse(is_multiply_prime(42))
        self.assertFalse(is_multiply_prime(43))
        self.assertFalse(is_multiply_prime(44))
        self.assertFalse(is_multiply_prime(45))
        self.assertFalse(is_multiply_prime(46))
        self.assertFalse(is_multiply_prime(47))
        self.assertFalse(is_multiply_prime(48))
        self.assertFalse(is_multiply_prime(49))
        self.assertFalse(is_multiply_prime(50))
        self.assertFalse(is_multiply_prime(51))
        self.assertFalse(is_multiply_prime(52))
        self.assertFalse(is_multiply_prime(53))
        self.assertFalse(is_multiply_prime(54))
        self.assertFalse(is_multiply_prime(55))
        self.assertFalse(is_multiply_prime(56))
        self.assertFalse(is_multiply_prime(57))
        self.assertFalse(is_multiply_prime(58))
        self.assertFalse(is_multiply_prime(59))
        self.assertFalse(is_multiply_prime(60))
        self.assertFalse(is_multiply_prime(61))
        self.assertFalse(is_multiply_prime(62))
        self.assertFalse(is_multiply_prime(63))
        self.assertFalse(is_multiply_prime(64))
        self.assertFalse(is_multiply_prime(65))
        self.assertFalse(is_multiply_prime(66))
        self.assertFalse(is_multiply_prime(67))
        self.assertFalse(is_multiply_prime(68))
        self.assertFalse(is_multiply_prime(69))
        self.assertFalse(is_multiply