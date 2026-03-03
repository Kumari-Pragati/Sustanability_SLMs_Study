You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_22_code import filter_integers
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """Filter given list of any Python values only for integers.
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_22_code import filter_integers

class TestFilterIntegers(unittest.TestCase):

    def test_filter_integers(self):
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])
        self.assertEqual(filter_integers([1, 'two', 3.0, 'four', 5]), [1, 3, 5])
        self.assertEqual(filter_integers([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(filter_integers([]), [])
        self.assertEqual(filter_integers(['one', 'two', 'three']), [])
        self.assertEqual(filter_integers([1, 2, 'three', 4, 'five']), [1, 2, 4])

if __name__ == '__main__':
    unittest.main()


This script creates a test class `TestFilterIntegers` that inherits from `unittest.TestCase`. It then defines a method `test_filter_integers` that tests the `filter_integers` function with various inputs. Each test case uses the `assertEqual` method to check that the output of `filter_integers` matches the expected output.

The script ends with `if __name__ == '__main__': unittest.main()`, which means that the tests will be run when the script is executed directly.

Please note that the function `filter_integers` is expected to be in a file named `HumanEval_22_code.py` in the same directory as the test script. If the function is in a different location, you will need to adjust the import statement accordingly.