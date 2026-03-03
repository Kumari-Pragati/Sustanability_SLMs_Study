You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_30_code import get_positive
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [e for e in l if e > 0]


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_30_code import get_positive

class TestGetPositive(unittest.TestCase):
    def test_get_positive(self):
        self.assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])
        self.assertEqual(get_positive([]), [])
        self.assertEqual(get_positive([-1, -2, -3]), [])
        self.assertEqual(get_positive([1, 2, 3]), [1, 2, 3])
        self.assertEqual(get_positive([0, 0, 0]), [])

if __name__ == '__main__':
    unittest.main()


This script creates a test case class `TestGetPositive` that inherits from `unittest.TestCase`. It then defines a test method `test_get_positive` that tests the `get_positive` function with various input lists. The `assertEqual` method is used to check if the output of `get_positive` is as expected.

The script ends with `if __name__ == '__main__': unittest.main()`, which means the tests will be run when the script is executed directly.

Please note that you need to have the `HumanEval_30_code` module with the `get_positive` function defined in it for this script to work.