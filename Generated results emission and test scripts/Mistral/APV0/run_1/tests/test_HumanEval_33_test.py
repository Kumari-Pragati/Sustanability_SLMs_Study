Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return l

 Here is a unittest test script for the `sort_third` function:


import unittest
from HumanEval_33_code import sort_third

class TestSortThird(unittest.TestCase):

    def test_sort_third(self):
        self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])
        self.assertEqual(sort_third([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(sort_third([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 6, 5])
        self.assertEqual(sort_third([1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(sort_third([1, 2, 3, 4, 5, 6, 7, 8]), [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the `sort_third` function with various input lists of different lengths. It uses the `assertEqual` method to check if the output of the function matches the expected output. If the function works correctly, all the test cases will pass. If any test case fails, the test script will indicate which test case failed and provide the expected and actual outputs.