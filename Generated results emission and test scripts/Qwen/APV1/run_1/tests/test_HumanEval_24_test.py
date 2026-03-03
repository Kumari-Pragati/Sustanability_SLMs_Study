system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

# Function to be tested
from HumanEval_24_code import largest_divisor

class TestLargestDivisor(unittest.TestCase):
    def test_largest_divisor(self):
        self.assertEqual(largest_divisor(15), 5)
        self.assertEqual(largest_divisor(28), 7)
        self.assertEqual(largest_divisor(100), 50)
        self.assertEqual(largest_divisor(99), 99)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestLargestDivisor` class within the `unittest` module, which inherits from `TestCase`. The `test_largest_divisor` method contains assertions to check the correctness of the `largest_divisor` function against provided data points. If any assertion fails, it will raise an error indicating which test failed and what value was expected but received instead.