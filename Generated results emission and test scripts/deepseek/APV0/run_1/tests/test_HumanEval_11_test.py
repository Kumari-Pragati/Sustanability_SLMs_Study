You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_11_code import string_xor

class TestStringXor(unittest.TestCase):

    def test_string_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')
        self.assertEqual(string_xor('101', '000'), '101')
        self.assertEqual(string_xor('111', '111'), '000')
        self.assertEqual(string_xor('000', '000'), '000')
        self.assertEqual(string_xor('1101', '0011'), '1110')

        # Test with different length strings
        self.assertEqual(string_xor('10', '101'), '001')
        self.assertEqual(string_xor('1111', '1'), '0100')

        # Test with empty strings
        self.assertEqual(string_xor('', ''), '')

        # Test with strings containing other characters
        with self.assertRaises(ValueError):
            string_xor('010', '110a')

        with self.assertRaises(ValueError):
            string_xor('010', '11012')

        with self.assertRaises(ValueError):
            string_xor('010', '110!@#')

if __name__ == '__main__':
    unittest.main()


This script includes a test class `TestStringXor` that inherits from `unittest.TestCase`. It includes a method `test_string_xor` that tests the `string_xor` function with various inputs. The `assertEqual` method is used to check that the output of the function matches the expected output. The `assertRaises` method is used to check that the function raises a `ValueError` when given invalid input.

Please note that the function `string_xor` should be in a file named `HumanEval_11_code.py` in the same directory as this test script for it to work correctly.