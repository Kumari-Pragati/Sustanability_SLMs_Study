You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_82_code import prime_length
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True

 import unittest
from HumanEval_82_code import prime_length

class TestPrimeLength(unittest.TestCase):

    def test_prime_length_with_prime_number(self):
        self.assertTrue(prime_length('Hello'))
        self.assertTrue(prime_length('abcdcba'))
        self.assertTrue(prime_length('kittens'))

    def test_prime_length_with_non_prime_number(self):
        self.assertFalse(prime_length(''))
        self.assertFalse(prime_length('a'))
        self.assertFalse(prime_length('orange'))
        self.assertFalse(prime_length('1234567890'))

    def test_prime_length_with_single_character(self):
        self.assertFalse(prime_length('a'))
        self.assertFalse(prime_length('1'))

    def test_prime_length_with_empty_string(self):
        self.assertFalse(prime_length(''))

if __name__ == '__main__':
    unittest.main()