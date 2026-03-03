You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_58_code import common
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_58_code import common

class TestCommon(unittest.TestCase):
    def test_common(self):
        self.assertEqual(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]), [1, 5, 653])
        self.assertEqual(common([5, 3, 2, 8], [3, 2]), [2, 3])
        self.assertEqual(common([1, 2, 3, 4], [5, 6, 7, 8]), [])
        self.assertEqual(common([1, 1, 1, 1], [1, 1, 1, 1]), [1])
        self.assertEqual(common([], []), [])
        self.assertEqual(common([1], [1]), [1])
        self.assertEqual(common([1], []), [])
        self.assertEqual(common([], [1]), [])

if __name__ == '__main__':
    unittest.main()


This script creates a test class `TestCommon` that inherits from `unittest.TestCase`. It then defines a method `test_common` that tests the `common` function with various inputs. Each test case uses the `assertEqual` method to check that the output of the `common` function matches the expected output.

The script ends with `if __name__ == '__main__': unittest.main()`, which means that the tests will be run when the script is executed directly.

Please note that you need to have the function `common` in a file named `HumanEval_58_code.py` in the same directory as this test script for it to work.