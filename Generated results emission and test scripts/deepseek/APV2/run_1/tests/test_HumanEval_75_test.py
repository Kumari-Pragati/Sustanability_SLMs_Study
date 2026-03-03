You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_75_code import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):

    def test_is_multiply_prime(self):
        self.assertTrue(is_multiply_prime(30))
        self.assertTrue(is_multiply_prime(210))
        self.assertTrue(is_multiply_prime(105))
        self.assertFalse(is_multiply_prime(40))
        self.assertFalse(is_multiply_prime(120))
        self.assertFalse(is_multiply_prime(1))
        self.assertFalse(is_multiply_prime(0))
        self.assertFalse(is_multiply_prime(-1))

if __name__ == '__main__':
    unittest.main()


This test suite includes a single test case `test_is_multiply_prime` that tests the function with a variety of inputs. The `assertTrue` method is used to check that the function returns `True` for inputs that should be considered "multiply prime" (i.e., the product of three distinct prime numbers), while the `assertFalse` method is used to check that the function returns `False` for inputs that should not be considered "multiply prime".

Please note that the function `is_multiply_prime` is not optimized for performance, and it has a time complexity of O(n^3), which may not be suitable for large inputs. If you need to test the function with large inputs, you may want to consider optimizing the function or using a different approach.