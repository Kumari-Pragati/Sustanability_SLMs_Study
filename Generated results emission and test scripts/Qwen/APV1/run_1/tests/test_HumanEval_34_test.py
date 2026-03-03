system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
from HumanEval_34_code import unique

class TestUnique(unittest.TestCase):
    def test_unique(self):
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

    def test_empty_list(self):
        self.assertEqual(unique([]), [])

    def test_single_element(self):
        self.assertEqual(unique([7]), [7])

    def test_duplicate_elements(self):
        self.assertEqual(unique([1, 1, 1, 1, 1]), [1])

    def test_mixed_types(self):
        self.assertEqual(unique([1, 'a', True, None, 1.0]), ['a', False, None, 1.0])

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestUnique` class that inherits from `unittest.TestCase`. It contains several test methods to ensure the `unique` function works as expected under different scenarios:

- The `test_unique` method tests the function with a typical input and checks if it returns the correct output.
- The `test_empty_list` method ensures the function handles an empty list correctly.
- The `test_single_element` method verifies the function's behavior when provided with a single-element list.
- The `test_duplicate_elements` method confirms the function can handle lists with duplicate elements without repetition.
- The `test_mixed_types` method demonstrates how the function should work with mixed data types in the input list.

The `if __name__ == '__main__':` block at the end of the script runs all the test cases defined within the `TestUnique` class using the `unittest.main()` function.