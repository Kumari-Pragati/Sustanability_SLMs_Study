### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_25_code import factorize
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
2. Include: from HumanEval_25_code import factorize
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    import math
    fact = []
    i = 2
    while i <= int(math.sqrt(n) + 1):
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1

    if n > 1:
        fact.append(n)
    return fact

 import unittest

from HumanEval_25_code import factorize

class TestFactorize(unittest.TestCase):
    def test_perfect_powers(self):
        self.assertEqual(factorize(4), [2, 2])
        self.assertEqual(factorize(9), [3, 3])
        self.assertEqual(factorize(16), [2, 2, 2, 2])
        self.assertEqual(factorize(25), [5, 5])
        self.assertEqual(factorize(27), [3, 3, 3])
        self.assertEqual(factorize(64), [2, 2, 2, 2, 2, 2, 2, 2])

    def test_composite_numbers(self):
        self.assertEqual(factorize(6), [2, 3])
        self.assertEqual(factorize(10), [2, 5])
        self.assertEqual(factorize(12), [2, 2, 3])
        self.assertEqual(factorize(15), [3, 5])
        self.assertEqual(factorize(18), [2, 3, 3])
        self.assertEqual(factorize(20), [2, 2, 5])
        self.assertEqual(factorize(30), [2, 3, 5, 5])
        self.assertEqual(factorize(35), [5, 7])
        self.assertEqual(factorize(40), [2, 2, 2, 5])
        self.assertEqual(factorize(42), [2, 3, 7])
        self.assertEqual(factorize(45), [3, 3, 5])
        self.assertEqual(factorize(50), [2, 5, 5])
        self.assertEqual(factorize(56), [2, 2, 7, 7])
        self.assertEqual(factorize(60), [2, 2, 3, 5])
        self.assertEqual(factorize(63), [3, 3, 7])
        self.assertEqual(factorize(70), [2, 5, 7])
        self.assertEqual(factorize(72), [2, 2, 3, 3])
        self.assertEqual(factorize(78), [2, 3, 7, 7])
        self.assertEqual(factorize(81), [3, 3, 3, 3])
        self.assertEqual(factorize(84), [2, 2, 3, 7])
        self.assertEqual(factorize(90), [2, 3, 3, 5])
        self.assertEqual(factorize(96), [2, 2, 2, 2, 3])
        self.assertEqual(factorize(100), [2, 2, 5, 5])
        self.assertEqual(factorize(105), [3, 5, 7])
        self.assertEqual(factorize(110), [2, 2, 5, 5, 5])
        self.assertEqual(factorize(112), [2, 2, 3, 3, 3])
        self.assertEqual(factorize(117), [117])
        self.assertEqual(factorize(120), [2, 2, 2, 3, 3])
        self.assertEqual(factorize(126), [2, 2, 3, 3, 7])
        self.assertEqual(factorize(130), [2, 5, 7, 7])
        self.assertEqual(factorize(133), [7, 19])
        self.assertEqual(factorize(135), [3, 3, 5])
        self.assertEqual(factorize(140), [2, 2, 2, 5, 5])
        self.assertEqual(factorize(144), [2, 2, 2, 3, 3, 3])
        self.assertEqual(factorize(150), [2, 3, 5, 5])
        self.assertEqual(factorize(154), [2, 3, 7, 7])