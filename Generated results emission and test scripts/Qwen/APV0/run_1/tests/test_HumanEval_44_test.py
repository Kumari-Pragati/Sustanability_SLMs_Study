system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


This script imports `unittest` and includes the `change_base` function from the provided code. It then defines a class `TestChangeBase` that inherits from `unittest.TestCase`. The `test_change_base` method contains assertions to check if the `change_base` function returns the expected results for different inputs. Finally, it runs all tests when the script is executed directly using `unittest.main()`.