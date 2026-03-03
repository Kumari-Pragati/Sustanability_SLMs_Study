You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_11_code import string_xor

class TestStringXor(unittest.TestCase):
    def test_string_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')
        self.assertEqual(string_xor('101', '000'), '101')
        self.assertEqual(string_xor('111', '111'), '000')
        self.assertEqual(string_xor('000', '000'), '000')
        self.assertEqual(string_xor('1101', '0011'), '1110')
        self.assertEqual(string_xor('10101010', '01010101'), '11111111')
        self.assertEqual(string_xor('0', '0'), '0')
        self.assertEqual(string_xor('1', '1'), '0')
        self.assertEqual(string_xor('0', '1'), '1')
        self.assertEqual(string_xor('1', '0'), '1')

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure that the function is working correctly. It tests the function with both '0' and '1' inputs, as well as longer strings. It also tests the function with different combinations of '0' and '1' to ensure that the xor operation is being performed correctly.