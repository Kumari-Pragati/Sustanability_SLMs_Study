system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
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
    return Trueassistant

Here is the complete unittest test suite for the given Python function:


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
        self.assertTrue(prime_length(''))
        self.assertTrue(prime_length('a'))
        self.assertTrue(prime_length('ab'))
        self.assertFalse(prime_length('abc'))
        self.assertTrue(prime_length('a'))
        self.assertTrue(prime_length('ab'))
        self.assertTrue(prime_length('abc'))
        self.assertTrue(prime_length('abcd'))
        self.assertFalse(prime_length('abcde'))
        self.assertTrue(prime_length('a'))
        self.assertTrue(prime_length('ab'))
        self.assertTrue(prime_length('abc'))
        self.assertTrue(prime_length('abcd'))
        self.assertTrue(prime_length('abcde'))
        self.assertTrue(prime_length('abcdef'))
        self.assertFalse(prime_length('abcdefg'))
        self.assertTrue(prime_length('a'))
        self.assertTrue(prime_length('ab'))
        self.assertTrue(prime_length('abc'))
        self.assertTrue(prime_length('abcd'))
        self.assertTrue(prime_length('abcde'))
        self.assertTrue(prime_length('abcdef'))
        self.assertTrue(prime_length('abcdefg'))
        self.assertTrue(prime_length('abcdefgh'))
        self.assertFalse(prime_length('abcdefghi'))
        self.assertTrue(prime_length('a'))
        self.assertTrue(prime_length('ab'))
        self.assertTrue(prime_length('abc'))
        self.assertTrue(prime_length('abcd'))
        self.assertTrue(prime_length('abcde'))
        self.assertTrue(prime_length('abcdef'))
        self.assertTrue(prime_length('abcdefg'))
        self.assertTrue(prime_length('abcdefgh'))
        self.assertTrue(prime_length('abcdefghi'))
        self.assertTrue(prime_length('abcdefghij'))
        self.assertFalse(prime_length('abcdefghiji'))
        self.assertTrue(prime_length('a'))
        self.assertTrue(prime_length('ab'))
        self.assertTrue(prime_length('abc'))
        self.assertTrue(prime_length('abcd'))
        self.assertTrue(prime_length('abcde'))
        self.assertTrue(prime_length('abcdef'))
        self.assertTrue(prime_length('abcdefg'))
        self.assertTrue(prime_length('abcdefgh'))
        self.assertTrue(prime_length('abcdefghi'))
        self.assertTrue(prime_length('abcdefghij'))
        self.assertTrue(prime_length('abcdefghiji'))
        self.assertTrue(prime_length('abcdefghijii'))
        self.assertFalse(prime_length('abcdefghijiii'))
        self.assertTrue(prime_length('a'))
        self.assertTrue(prime_length('ab'))
        self.assertTrue(prime_length('abc'))
        self.assertTrue(prime_length('abcd'))
        self.assertTrue(prime_length('abcde'))
        self.assertTrue(prime_length('abcdef'))
        self.assertTrue(prime_length('abcdefg'))
        self.assertTrue(prime_length('abcdefgh'))
        self.assertTrue(prime_length('abcdefghi'))
        self.assertTrue(prime_length('abcdefghij'))
        self.assertTrue(prime_length('abcdefghiji'))
        self.assertTrue(prime_length('abcdefghijii'))
        self.assertTrue(prime_length('abcdefghijiii'))
        self.assertTrue(prime_length('abcdefghijiiii'))
        self.assertFalse(prime_length('abcdefghijiiiiii'))
        self.assertTrue(prime_length('a'))
        self.assertTrue(prime_length('ab'))
        self.assertTrue(prime_length('abc'))
        self.assertTrue(prime_length('abcd'))
        self.assertTrue(prime_length('abcde'))
        self.assertTrue(prime_length('abcdef'))
        self.assertTrue(prime_length('abcdefg'))
        self.assertTrue(prime_length('abcdefgh'))
        self.assertTrue(prime_length('abcdefghi'))
        self.assertTrue(prime_length('abcdefghij'))
        self.assertTrue(prime_length('abcdefghiji'))
        self.assertTrue(prime_length('abcdefghijii'))
        self.assertTrue(prime_length('abcdefghijiii'))
        self.assertTrue(prime_length('abcdefghijiiii'))
        self.assertTrue(prime_length('abcdefghijiiiiii'))
        self.assertTrue(prime_length('abcdefghijiiiiiii'))
        self.assertFalse(prime_length('abcdefghijiiiiiiii'))
        self.assertTrue(prime_length('a'))
        self.assertTrue(prime_length('ab'))
        self.assertTrue(prime_length('abc'))
        self.assertTrue(prime_length('abcd'))
        self.assertTrue(prime_length('abcde'))
        self.assertTrue(prime_length('abcdef'))
        self.assertTrue(prime_length('abcdefg'))
        self.assertTrue(prime_length('abcdefgh'))
        self.assertTrue(prime_length('abcdefghi'))
        self.assertTrue(prime_length('abcdefghij'))
        self.assertTrue(prime_length('abcdefghiji'))
        self.assertTrue(prime_length('abcdefghijii'))
        self.assertTrue(prime_length('abcdefghijiii'))
        self.assertTrue(prime_length('abcdefghijiiii'))
        self.assertTrue(prime_length