system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_24_code import largest_divisor
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def largest_divisor(n: int) -> int:
    """For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in reversed(range(n)):
        if n % i == 0:
            return i


assistant

import unittest

# Importing the function to be tested
from HumanEval_24_code import largest_divisor

class TestLargestDivisor(unittest.TestCase):
    def test_largest_divisor(self):
        self.assertEqual(largest_divisor(15), 5)
        self.assertEqual(largest_divisor(28), 7)
        self.assertEqual(largest_divisor(100), 50)
        self.assertEqual(largest_divisor(99), 99)

if __name__ == '__main__':
    unittest.main()


This script imports the `largest_divisor` function and defines a test class `TestLargestDivisor` within the `unittest` module. It includes several test cases using the `assertEqual` method to verify that the function returns the correct results for different inputs. The `unittest.main()` call at the end makes the tests executable when run as a standalone script.