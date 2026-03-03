system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_97_code import multiply

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.

    Examples:
    multiply(148, 412) ➞ 16
    multiply(19, 28) ➞ 72
    multiply(2020, 1851) ➞ 0
    multiply(14, -15) ➞ 20
    """

    return abs(a % 10) * abs(b % 10)


assistant

import unittest

# Function to be tested
from HumanEval_97_code import multiply

class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(148, 412), 16)
        self.assertEqual(multiply(19, 28), 72)
        self.assertEqual(multiply(2020, 1851), 0)
        self.assertEqual(multiply(14, -15), 20)
        self.assertEqual(multiply(-14, 15), 20)
        self.assertEqual(multiply(148, -412), 16)
        self.assertEqual(multiply(-148, 412), 16)
        self.assertEqual(multiply(148, 412), 16)
        self.assertEqual(multiply(148, -412), 16)
    
    def test_edge_cases(self):
        # Testing edge cases where one or both numbers are zero
        self.assertEqual(multiply(0, 123), 0)
        self.assertEqual(multiply(123, 0), 0)
        self.assertEqual(multiply(0, 0), 0)
        
        # Testing negative numbers
        self.assertEqual(multiply(-14, 15), -210)
        self.assertEqual(multiply(14, -15), -210)
        self.assertEqual(multiply(-148, 412), -6736)
        self.assertEqual(multiply(148, -412), -6736)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestMultiply` class within the `unittest` module, which contains several test methods to verify the correctness of the `multiply` function. The tests cover various scenarios including positive and negative numbers, as well as edge cases involving zeros.