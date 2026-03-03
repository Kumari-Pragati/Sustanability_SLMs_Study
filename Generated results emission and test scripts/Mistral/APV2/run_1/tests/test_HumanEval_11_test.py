You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the `string_xor` function:


import unittest
from HumanEval_11_code import string_xor

class TestStringXor(unittest.TestCase):

    def test_string_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')
        self.assertEqual(string_xor('101', '011'), '110')
        self.assertEqual(string_xor('100010', '110111'), '010101')
        self.assertEqual(string_xor('0', '0'), '0')
        self.assertEqual(string_xor('1', '1'), '0')
        self.assertEqual(string_xor('0', '1'), '1')

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover different scenarios, such as different input lengths, all zeros, all ones, and a mix of zeros and ones. The `assertEqual` function is used to compare the expected output with the actual output of the `string_xor` function.