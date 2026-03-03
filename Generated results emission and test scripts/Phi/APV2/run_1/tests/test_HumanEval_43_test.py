You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_43_code import pairs_sum_to_zero
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    It returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False

 import unittest
from HumanEval_43_code import pairs_sum_to_zero

class TestPairsSumToZero(unittest.TestCase):

    def test_no_zero_sum_pairs(self):
        self.assertFalse(pairs_sum_to_zero([1, 3, 5, 0]), msg="Should return False for a list without zero sum pairs")

    def test_no_zero_sum_pairs_with_single_element(self):
        self.assertFalse(pairs_sum_to_zero([1]), msg="Should return False for a list with a single element")

    def test_no_zero_sum_pairs_with_negative_numbers(self):
        self.assertFalse(pairs_sum_to_zero([1, 3, -2, 1]), msg="Should return False for a list with negative numbers but no zero sum pairs")

    def test_no_zero_sum_pairs_with_positive_numbers(self):
        self.assertFalse(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]), msg="Should return False for a list with only positive numbers but no zero sum pairs")

    def test_zero_sum_pairs_present(self):
        self.assertTrue(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]), msg="Should return True for a list with zero sum pairs")

if __name__ == '__main__':
    unittest.main()