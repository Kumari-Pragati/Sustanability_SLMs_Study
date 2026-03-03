You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_49_code import modp
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_49_code import modp

class TestModp(unittest.TestCase):
    def test_modp(self):
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(3, 11), 8)
        self.assertEqual(modp(100, 101), 1)

if __name__ == '__main__':
    unittest.main()


This script creates a test case for the `modp` function and checks if the function's output matches the expected output for the given inputs. If the function's output does not match the expected output, the test case will fail.

Please note that you need to have the `HumanEval_49_code` module with the `modp` function defined in it for this script to work. If the `modp` function is not defined in a separate module, you can replace `from HumanEval_49_code import modp` with `modp` and define the function within the script.

To run the script, you can use the following command in your terminal:


python test_modp.py


Replace `test_modp.py` with the name of your script.