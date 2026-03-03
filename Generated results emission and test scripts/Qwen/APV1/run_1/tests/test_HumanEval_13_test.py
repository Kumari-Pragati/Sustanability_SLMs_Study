system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_13_code import greatest_common_divisor

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return a


assistant

import unittest
from HumanEval_13_code import greatest_common_divisor

class TestGCD(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestGCD` class that inherits from `unittest.TestCase`. It contains a single method `test_gcd`, which uses assertions to check if the `greatest_common_divisor` function returns the correct results for the provided test cases. The `assertEqual` method compares the output of the function with expected values and raises an assertion error if they do not match. If all tests pass without errors, the program will run using the `unittest.main()` function at the end.