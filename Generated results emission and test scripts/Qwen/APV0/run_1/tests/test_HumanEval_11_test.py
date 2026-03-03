system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_11_code import string_xor
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor(i: str, j: str) -> str:
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))


assistant

import unittest

# Importing the function to be tested
from HumanEval_11_code import string_xor

class TestStringXOR(unittest.TestCase):
    
    # Test cases to verify the correctness of the string_xor function
    def test_string_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')
        self.assertEqual(string_xor('101', '011'), '110')
        self.assertEqual(string_xor('000', '000'), '000')
        self.assertEqual(string_xor('111', '111'), '000')
        self.assertEqual(string_xor('', ''), '')
        self.assertEqual(string_xor('1', '0'), '1')

if __name__ == '__main__':
    unittest.main()


This script imports the `unittest` module and the `string_xor` function from the `HumanEval_11_code` package. It then defines a class `TestStringXOR` that inherits from `unittest.TestCase`. Within this class, there is a method `test_string_xor` which contains several assertions to check various scenarios of input strings and their expected output. Finally, it calls `unittest.main()` to run all tests when the script is executed directly.