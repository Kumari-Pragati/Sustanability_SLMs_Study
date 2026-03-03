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
    return sorted(list(set(l)))assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_34_code import unique

class TestUniqueFunction(unittest.TestCase):

    def test_unique(self):
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])
        self.assertEqual(unique([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(unique(['a', 'b', 'c', 'd', 'e']), ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(unique([1, 1, 1, 1, 1]), [1])
        self.assertEqual(unique([]), [])
        self.assertEqual(unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            unique("hello")
        with self.assertRaises(TypeError):
            unique((1, 2, 3))
        with self.assertRaises(TypeError):
            unique({"a": 1, "b": 2})

if __name__ == '__main__':
    unittest.main()


This script includes two test cases: `test_unique` and `test_non_list_input`. The `test_unique` test case checks the function with different inputs, including lists of integers and strings. The `test_non_list_input` test case checks that the function raises a TypeError when given non-list inputs, such as strings, tuples, or dictionaries.