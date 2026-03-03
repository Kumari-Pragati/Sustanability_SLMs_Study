system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Importing the function to be tested
from HumanEval_34_code import unique

class TestUnique(unittest.TestCase):
    def test_unique(self):
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123], "Test case 1 failed")
        self.assertEqual(unique([]), [], "Test case 2 failed")
        self.assertEqual(unique(['a', 'b', 'a']), ['a', 'b'], "Test case 3 failed")
        self.assertEqual(unique([-1, -1, 0, 1, 1, 1]), [-1, 0, 1], "Test case 4 failed")

if __name__ == '__main__':
    unittest.main()


This script imports the `unique` function from the module `HumanEval_34_code`, defines a class `TestUnique` that inherits from `unittest.TestCase`, and includes several test cases using assertEqual methods to verify the correctness of the `unique` function. The `if __name__ == '__main__':` block ensures that the tests can be run directly when the script is executed.