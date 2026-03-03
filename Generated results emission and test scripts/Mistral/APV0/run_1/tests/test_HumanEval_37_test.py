Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `sort_even` function:


import unittest
from HumanEval_37_code import sort_even

class TestSortEven(unittest.TestCase):

    def test_sort_even(self):
        self.assertEqual(sort_even([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_even([5, 6, 3, 4]), [3, 6, 5, 4])
        self.assertEqual(sort_even([2, 1, 3]), [2, 1, 3])
        self.assertEqual(sort_even([4, 3, 2, 1]), [2, 3, 4, 1])
        self.assertEqual(sort_even([6, 5, 4, 3, 2, 1]), [2, 3, 4, 5, 6])
        self.assertEqual(sort_even([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(sort_even([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(sort_even([1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(sort_even([1, 2, 3, 4, 5, 6, 7, 8]), [1, 2, 3, 4, 5, 6, 7, 8])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to ensure the function works correctly for various input lists. The test cases cover the base case (empty list), odd-length lists, even-length lists, and lists with more than 6 elements.