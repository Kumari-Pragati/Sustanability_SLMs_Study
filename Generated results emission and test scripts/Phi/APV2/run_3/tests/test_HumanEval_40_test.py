You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
        self.assertFalse(triples_sum_to_zero([1, 3, 5, 0]), msg="Should return False for a list without triplets summing to zero")

    def test_triplets_sum_to_zero(self):
        self.assertTrue(triples_sum_to_zero([1, 3, -2, 1]), msg="Should return True for a list with triplets summing to zero")
        self.assertTrue(triples_sum_to_zero([2, 4, -5, 3, 9, 7]), msg="Should return True for a list with triplets summing to zero")

    def test_single_element_list(self):
        self.assertFalse(triples_sum_to_zero([1]), msg="Should return False for a list with a single element")

    def test_no_triplets_in_sorted_list(self):
        self.assertFalse(triples_sum_to_zero([-5, -3, -1, 0, 1, 3]), msg="Should return False for a sorted list without triplets summing to zero")

    def test_duplicate_elements(self):
        self.assertFalse(triples_sum_to_zero([1, 1, -1, 0]), msg="Should return False for a list with duplicate elements that do not form a triplet summing to zero")

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios to ensure that the `triples_sum_to_zero` function behaves as expected. It includes tests for lists that do not contain any triplets summing to zero, lists that do contain such triplets, lists with a single element, sorted lists without triplets summing to zero, and lists with duplicate elements that do not form a triplet summing to zero. Each test case is accompanied by a message that will be displayed if the test fails, providing additional context for the failure.