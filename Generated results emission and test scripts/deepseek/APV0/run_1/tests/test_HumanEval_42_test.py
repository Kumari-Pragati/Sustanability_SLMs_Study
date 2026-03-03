You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_42_code import incr_list
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [e + 1 for e in l]


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_42_code import incr_list

class TestIncrList(unittest.TestCase):
    def test_incr_list(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])
        self.assertEqual(incr_list([]), [])
        self.assertEqual(incr_list([0]), [1])
        self.assertEqual(incr_list([-1, -2, -3]), [0, -1, -2])

if __name__ == '__main__':
    unittest.main()


This script creates a test case class `TestIncrList` that inherits from `unittest.TestCase`. Inside this class, there is a method `test_incr_list` that tests the `incr_list` function with various inputs. The `assertEqual` method is used to check if the output of `incr_list` matches the expected output.

The script ends with `if __name__ == '__main__': unittest.main()`, which means that the tests will be run when the script is executed directly.

Please note that you need to have the `HumanEval_42_code` module with the `incr_list` function defined in it for this script to work.