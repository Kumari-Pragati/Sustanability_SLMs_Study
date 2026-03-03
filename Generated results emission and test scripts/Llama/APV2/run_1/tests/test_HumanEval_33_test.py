system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_33_code import sort_third
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indices that are not divisible by three, while its values at the indices that are divisible by three are equal
    to the values of the corresponding indices of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l = list(l)
    l[::3] = sorted(l[::3])
    return lassistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_33_code import sort_third

class TestSortThird(unittest.TestCase):

    def test_sort_third_empty_list(self):
        self.assertEqual(sort_third([]), [])

    def test_sort_third_single_element(self):
        self.assertEqual(sort_third([1]), [1])

    def test_sort_third_multiple_elements(self):
        self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])

    def test_sort_third_list_with_duplicates(self):
        self.assertEqual(sort_third([1, 2, 3, 3, 4, 5, 5]), [1, 2, 3, 3, 4, 5, 5])

    def test_sort_third_list_with_negative_numbers(self):
        self.assertEqual(sort_third([-1, -2, -3]), [-1, -2, -3])
        self.assertEqual(sort_third([-5, -6, -3, -4, -8, -9, -2]), [-2, -6, -3, -4, -8, -9, -5])

    def test_sort_third_list_with_mixed_types(self):
        with self.assertRaises(TypeError):
            sort_third([1, 2, 'a', 3, 4, 'b', 5])

if __name__ == '__main__':
    unittest.main()