Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_40_code import triples_sum_to_zero
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    It returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False

 import unittest
from HumanEval_40_code import triples_sum_to_zero

class TestTriplesSumToZero(unittest.TestCase):

    def test_no_triplets_sum_to_zero(self):
        self.assertFalse(triples_sum_to_zero([1, 3, 5, 0]))

    def test_triplets_sum_to_zero(self):
        self.assertTrue(triples_sum_to_zero([1, 3, -2, 1]))

    def test_no_triplets_in_empty_list(self):
        self.assertFalse(triples_sum_to_zero([]))

    def test_no_triplets_in_single_element_list(self):
        self.assertFalse(triples_sum_to_zero([1]))

    def test_no_triplets_in_two_element_list(self):
        self.assertFalse(triples_sum_to_zero([1, 2]))

    def test_triplets_sum_to_zero_with_duplicates(self):
        self.assertTrue(triples_sum_to_zero([2, 4, -5, 3, 9, 7]))

    def test_triplets_sum_to_zero_with_negative_numbers(self):
        self.assertTrue(triples_sum_to_zero([-1, 0, 1, -1]))

    def test_triplets_sum_to_zero_with_positive_numbers(self):
        self.assertTrue(triples_sum_to_zero([1, 2, -3, 4]))

    def test_triplets_sum_to_zero_with_zero(self):
        self.assertTrue(triples_sum_to_zero([0, 0, 0]))

if __name__ == '__main__':
    unittest.main()