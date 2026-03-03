system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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


assistant

import unittest
from HumanEval_44_code import change_base

class TestChangeBase(unittest.TestCase):

    def test_change_base(self):
        self.assertEqual(change_base(8, 3), "22")
        self.assertEqual(change_base(8, 2), "1000")
        self.assertEqual(change_base(7, 2), "111")

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestChangeBase` class that inherits from `unittest.TestCase`. It contains a single method `test_change_base`, which tests the `change_base` function using assertions. The `assertEqual` methods check if the output of `change_base` matches the expected results for different inputs and bases. If any assertion fails, it will raise an error indicating which test failed.