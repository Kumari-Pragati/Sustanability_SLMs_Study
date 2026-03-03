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

 Here is a unittest test script for the `string_xor` function:


import unittest
from HumanEval_11_code import string_xor

class TestStringXor(unittest.TestCase):
    def test_string_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')
        self.assertEqual(string_xor('101', '011'), '110')
        self.assertEqual(string_xor('100010', '110111'), '010101')
        self.assertEqual(string_xor('', '1'), '1')
        self.assertEqual(string_xor('1', ''), '1')
        self.assertEqual(string_xor('0', '0'), '0')
        self.assertEqual(string_xor('1', '1'), '0')

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the function with various input combinations, including empty strings and strings of different lengths. The test case uses the `assertEqual` method to check if the expected output matches the actual output of the function. If all tests pass, the test script will run the unittest.main() function, which will execute the tests and print the results.