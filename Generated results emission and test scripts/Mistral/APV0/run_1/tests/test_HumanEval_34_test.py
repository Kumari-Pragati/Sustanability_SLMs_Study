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

 Here is a unittest test script for the `unique` function:


import unittest
from HumanEval_34_code import unique

class TestUnique(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(unique([]), [])

    def test_single_element_list(self):
        self.assertEqual(unique([1]), [1])

    def test_duplicate_elements(self):
        self.assertEqual(unique([1, 1, 2, 2, 3, 3]), [1, 2, 3])

    def test_mixed_data_types(self):
        self.assertEqual(unique([1, 'a', 2, 'a', 3]), [1, 'a', 2, 3])

    def test_large_list(self):
        large_list = list(range(100))
        large_list_unique = unique(large_list)
        self.assertEqual(len(large_list), len(large_list_unique))

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios such as an empty list, single-element list, duplicate elements, mixed data types, and a large list. The test cases use the `assertEqual` method to compare the expected output with the actual output of the `unique` function.