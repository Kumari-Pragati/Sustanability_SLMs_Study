You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_44_code import change_base
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_44_code import change_base

class TestChangeBase(unittest.TestCase):
    def test_change_base(self):
        self.assertEqual(change_base(8, 3), '22')
        self.assertEqual(change_base(8, 2), '1000')
        self.assertEqual(change_base(7, 2), '111')
        self.assertEqual(change_base(10, 10), '10')
        self.assertEqual(change_base(0, 2), '0')
        self.assertEqual(change_base(15, 16), 'F')
        self.assertEqual(change_base(16, 16), '10')
        self.assertEqual(change_base(17, 16), '11')

if __name__ == '__main__':
    unittest.main()


This script includes several test cases to ensure the function is working as expected. It tests the function with different inputs and checks if the output is as expected.

Please note that the function `change_base` should be in a file named `HumanEval_44_code.py` in the same directory as this test script.

Also, please note that the function `change_base` is not designed to handle base numbers greater than 10. The function assumes that the base number is less than 10. If you want to test the function with base numbers greater than 10, you need to modify the function to handle these cases.