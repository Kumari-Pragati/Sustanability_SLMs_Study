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
   - Include from HumanEval_36_code import fizz_buzz
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
    unittest.main()user

### Immediate Task
Write the complete unittest test suite for the following Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_36_code import fizz_buzz
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        ans += (c == '7')
    return ansassistant

import unittest
from HumanEval_36_code import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    def test_small_numbers(self):
        self.assertEqual(fizz_buzz(10), 0)
        self.assertEqual(fizz_buzz(11), 0)
        self.assertEqual(fizz_buzz(12), 0)
        self.assertEqual(fizz_buzz(13), 0)
        self.assertEqual(fizz_buzz(14), 0)
        self.assertEqual(fizz_buzz(15), 0)
        self.assertEqual(fizz_buzz(16), 0)
        self.assertEqual(fizz_buzz(17), 0)
        self.assertEqual(fizz_buzz(18), 0)
        self.assertEqual(fizz_buzz(19), 0)
        self.assertEqual(fizz_buzz(20), 0)

    def test_edge_cases(self):
        self.assertEqual(fizz_buzz(22), 0)
        self.assertEqual(fizz_buzz(33), 0)
        self.assertEqual(fizz_buzz(44), 0)
        self.assertEqual(fizz_buzz(55), 0)
        self.assertEqual(fizz_buzz(66), 0)
        self.assertEqual(fizz_buzz(77), 1)
        self.assertEqual(fizz_buzz(88), 0)
        self.assertEqual(fizz_buzz(99), 0)

    def test_large_numbers(self):
        self.assertEqual(fizz_buzz(100), 2)
        self.assertEqual(fizz_buzz(101), 3)
        self.assertEqual(fizz_buzz(102), 2)
        self.assertEqual(fizz_buzz(103), 3)
        self.assertEqual(fizz_buzz(104), 2)
        self.assertEqual(fizz_buzz(105), 3)
        self.assertEqual(fizz_buzz(106), 2)
        self.assertEqual(fizz_buzz(107), 3)
        self.assertEqual(fizz_buzz(108), 2)
        self.assertEqual(fizz_buzz(109), 3)

if __name__ == '__main__':
    unittest.main()