system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
from HumanEval_75_code import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):

    def test_is_multiply_prime(self):
        self.assertTrue(is_multiply_prime(30))
        self.assertFalse(is_multiply_prime(49))
        self.assertTrue(is_multiply_prime(60))
        self.assertFalse(is_multiply_prime(81))

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestIsMultiplyPrime` class within the `unittest` module, which inherits from `TestCase`. The `test_is_multiply_prime` method contains assertions to check the correctness of the `is_multiply_prime` function. The `assertTrue`, `assertFalse`, and `assertTrue` methods are used to verify that the function behaves as expected for different inputs. Finally, the `unittest.main()` call at the end runs all tests when the script is executed directly.