You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_37_code import sort_even
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    evens = l[::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans

 import unittest
from HumanEval_37_code import sort_even

class TestSortEven(unittest.TestCase):

    def test_sort_even_identical_odd_indices(self):
        self.assertEqual(sort_even([1, 2, 3]), [1, 2, 3])

    def test_sort_even_mixed_values(self):
        self.assertEqual(sort_even([5, 6, 3, 4]), [3, 6, 5, 4])

    def test_sort_even_uneven_length(self):
        self.assertEqual(sort_even([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_sort_even_empty_list(self):
        self.assertEqual(sort_even([]), [])

    def test_sort_even_single_element(self):
        self.assertEqual(sort_even([5]), [5])

    def test_sort_even_all_even_numbers(self):
        self.assertEqual(sort_even([2, 4, 6, 8]), [2, 4, 6, 8])

    def test_sort_even_all_odd_numbers(self):
        self.assertEqual(sort_even([1, 3, 5, 7]), [1, 3, 5, 7])

    def test_sort_even_mixed_even_odd(self):
        self.assertEqual(sort_even([1, 3, 2, 4, 5, 6]), [1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
    unittest.main()