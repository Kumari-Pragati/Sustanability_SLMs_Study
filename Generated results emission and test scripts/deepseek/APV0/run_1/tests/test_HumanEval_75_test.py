You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_75_code import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):

    def test_is_multiply_prime(self):
        self.assertTrue(is_multiply_prime(30))
        self.assertTrue(is_multiply_prime(105))
        self.assertTrue(is_multiply_prime(210))
        self.assertFalse(is_multiply_prime(40))
        self.assertFalse(is_multiply_prime(100))
        self.assertFalse(is_multiply_prime(1))
        self.assertFalse(is_multiply_prime(0))
        self.assertFalse(is_multiply_prime(-10))

if __name__ == '__main__':
    unittest.main()


This script includes a test case for the `is_multiply_prime` function with several test cases. The `assertTrue` method is used to check if the function returns `True` for the correct inputs, and `assertFalse` is used to check if the function returns `False` for the incorrect inputs.

Please note that the function `is_multiply_prime` is not efficient for large numbers because it checks all possible combinations of three prime numbers. It would be better to optimize it by using a different approach, such as using a Sieve of Eratosthenes to generate all prime numbers up to 100, and then checking all possible combinations.