system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
    return sorted(list(set(l)))assistant

Here is the complete unittest test suite for the given Python function:


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
            unique("Hello, World!")
        with self.assertRaises(TypeError):
            unique((1, 2, 3, 4, 5))
        with self.assertRaises(TypeError):
            unique({1, 2, 3, 4, 5})

if __name__ == '__main__':
    unittest.main()