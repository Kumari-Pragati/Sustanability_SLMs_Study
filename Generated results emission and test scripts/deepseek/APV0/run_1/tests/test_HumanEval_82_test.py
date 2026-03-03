You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given function:


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
        self.assertTrue(prime_length('abcdefghijklmnopqrstuvwxyz'))
        self.assertFalse(prime_length('abcdefghijklmnopqrstuvwxyza'))

if __name__ == '__main__':
    unittest.main()


This script creates a test case class `TestPrimeLength` that inherits from `unittest.TestCase`. It then defines a test method `test_prime_length` that tests the `prime_length` function with various inputs. The `assertTrue` and `assertFalse` methods are used to check that the function returns the correct output for each input.

The script ends with `if __name__ == '__main__': unittest.main()`, which means that the tests will be run when the script is executed directly.

Please note that the `HumanEval_82_code` module and the `prime_length` function should be defined in a separate Python file for this script to work.