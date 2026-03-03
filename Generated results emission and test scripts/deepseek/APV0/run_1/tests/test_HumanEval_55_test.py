You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_55_code import fib
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_55_code import fib

class TestFib(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(8), 21)
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(6), 8)
        self.assertEqual(fib(7), 13)

if __name__ == '__main__':
    unittest.main()


This script includes a test class `TestFib` that inherits from `unittest.TestCase`. Inside this class, there is a method `test_fib` that tests the `fib` function with a variety of inputs. The `assertEqual` method is used to check if the output of the `fib` function matches the expected output.

The script ends with `if __name__ == '__main__': unittest.main()`, which means the tests will be run when the script is run directly.

Please note that the function `fib` is not efficient for large inputs because it uses a lot of redundant computation. It's a good idea to add a test for a large input to make sure the function doesn't crash, but it's not a good idea to test the output of a function that's not efficient for large inputs.