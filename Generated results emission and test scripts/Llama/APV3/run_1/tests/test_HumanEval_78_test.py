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
   - Include from HumanEval_78_code import hex_key
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
2. Include: from HumanEval_78_code import hex_key
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def hex_key(num):
    """You have been tasked to write a function that receives 
    a hexadecimal number as a string and counts the number of hexadecimal 
    digits that are primes (prime number, or a prime, is a natural number 
    greater than 1 that is not a product of two smaller natural numbers).
    Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    Note: you may assume the input is always correct or empty string, 
    and symbols A,B,C,D,E,F are always uppercase.
    Examples:
        For num = "AB" the output should be 1.
        For num = "1077E" the output should be 2.
        For num = "ABED1A33" the output should be 4.
        For num = "123456789ABCDEF0" the output should be 6.
        For num = "2020" the output should be 2.
    """

    primes = ('2', '3', '5', '7', 'B', 'D')
    total = 0
    for i in range(len(num)):
        if num[i] in primes:
            total += 1
    return totalassistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_78_code import hex_key

class TestHexKey(unittest.TestCase):
    def test_single_prime_digit(self):
        self.assertEqual(hex_key("2"), 1)
        self.assertEqual(hex_key("3"), 1)
        self.assertEqual(hex_key("5"), 1)
        self.assertEqual(hex_key("7"), 1)
        self.assertEqual(hex_key("B"), 1)
        self.assertEqual(hex_key("D"), 1)

    def test_multiple_prime_digits(self):
        self.assertEqual(hex_key("AB"), 1)
        self.assertEqual(hex_key("1077E"), 2)
        self.assertEqual(hex_key("ABED1A33"), 4)
        self.assertEqual(hex_key("123456789ABCDEF0"), 6)
        self.assertEqual(hex_key("2020"), 2)

    def test_empty_string(self):
        self.assertEqual(hex_key(""), 0)

    def test_non_hexadecimal_digits(self):
        self.assertEqual(hex_key("1234567890"), 0)
        self.assertEqual(hex_key("123456789ABC"), 0)
        self.assertEqual(hex_key("123456789ABCDEF"), 0)

if __name__ == '__main__':
    unittest.main()