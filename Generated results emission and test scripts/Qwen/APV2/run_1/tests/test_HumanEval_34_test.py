system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

# Provided function
from HumanEval_34_code import unique

class TestUnique(unittest.TestCase):

    def test_unique(self):
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

    def test_empty_list(self):
        self.assertEqual(unique([]), [])

    def test_single_element(self):
        self.assertEqual(unique([42]), [42])

    def test_duplicate_elements(self):
        self.assertEqual(unique([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])

    def test_mixed_types(self):
        self.assertEqual(unique(['a', 'b', 'c', 'a']), ['a', 'b', 'c'])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various edge cases such as empty lists, single-element lists, lists with duplicate elements, and mixed types of elements. It uses `assertEqual` to check if the function's output matches the expected results.