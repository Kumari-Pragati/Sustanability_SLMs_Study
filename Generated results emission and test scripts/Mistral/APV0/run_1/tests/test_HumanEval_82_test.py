Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the provided `prime_length` function:


import unittest
from HumanEval_82_code import prime_length

class TestPrimeLength(unittest.TestCase):
    def test_prime_length(self):
        self.assertTrue(prime_length('Hello'))
        self.assertTrue(prime_length('abcdcba'))
        self.assertTrue(prime_length('kittens'))
        self.assertFalse(prime_length('orange'))
        self.assertFalse(prime_length(''))
        self.assertFalse(prime_length('a'))
        self.assertTrue(prime_length('abcdefgh'))
        self.assertFalse(prime_length('abcdefghi'))

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the given examples and additional tests to ensure the function works correctly for strings of length 0, 1, and prime numbers greater than 5. Run this script using the command `python -m unittest test_prime_length.py` to execute the tests.