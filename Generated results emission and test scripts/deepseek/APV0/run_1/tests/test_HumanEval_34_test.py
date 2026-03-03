You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_34_code import unique
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(list(set(l)))


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_34_code import unique

class TestUnique(unittest.TestCase):

    def test_unique(self):
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])
        self.assertEqual(unique([1, 1, 1, 1]), [1])
        self.assertEqual(unique([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(unique([]), [])
        self.assertEqual(unique([1]), [1])
        self.assertEqual(unique(['a', 'b', 'a', 'c', 'b']), ['a', 'b', 'c'])
        self.assertEqual(unique(['a', 'a', 'a', 'a']), ['a'])

if __name__ == '__main__':
    unittest.main()


This script creates a test class `TestUnique` that inherits from `unittest.TestCase`. Inside this class, there is a method `test_unique` that tests the `unique` function with various inputs. The `assertEqual` method is used to check if the output of the `unique` function is as expected.

The script ends with `unittest.main()`, which runs the test cases when the script is run directly.

Please note that the `HumanEval_34_code` module should contain the `unique` function for the test to pass.