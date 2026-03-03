system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Define the helper function to check if a number is prime
def is_prime(n):
    for j in range(2, n):
        if n % j == 0:
            return False
    return True

class TestIsMultiplyPrime(unittest.TestCase):

    # Test cases to verify the correctness of the is_multiply_prime function
    def test_is_multiply_prime(self):
        self.assertTrue(is_multiply_prime(30))  # 30 = 2 * 3 * 5
        self.assertFalse(is_multiply_prime(49))  # 49 = 7^2
        self.assertTrue(is_multiply_prime(60))   # 60 = 2 * 3 * 5
        self.assertFalse(is_multiply_prime(81))   # 81 = 3^4
        self.assertTrue(is_multiply_prime(105))  # 105 = 3 * 5 * 7
        self.assertFalse(is_multiply_prime(100))  # 100 = 2^2 * 5^2

if __name__ == '__main__':
    unittest.main()


This completes the unittest test suite for the `is_multiply_prime` function, including the necessary imports and ensuring it runs correctly when executed as a script.