system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
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
    return Falseassistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_40_code import triples_sum_to_zero

class TestTriplesSumToZero(unittest.TestCase):

    def test_triples_sum_to_zero(self):
        self.assertFalse(triples_sum_to_zero([1, 3, 5, 0]))
        self.assertTrue(triples_sum_to_zero([1, 3, -2, 1]))
        self.assertFalse(triples_sum_to_zero([1, 2, 3, 7]))
        self.assertTrue(triples_sum_to_zero([2, 4, -5, 3, 9, 7]))
        self.assertFalse(triples_sum_to_zero([1]))

    def test_empty_list(self):
        self.assertFalse(triples_sum_to_zero([]))

    def test_single_element_list(self):
        self.assertFalse(triples_sum_to_zero([1]))

    def test_two_element_list(self):
        self.assertFalse(triples_sum_to_zero([1, 2]))

    def test_three_element_list(self):
        self.assertFalse(triples_sum_to_zero([1, 2, 3]))

    def test_four_element_list(self):
        self.assertFalse(triples_sum_to_zero([1, 2, 3, 4]))

    def test_five_element_list(self):
        self.assertTrue(triples_sum_to_zero([1, 2, 3, 4, -5]))

if __name__ == '__main__':
    unittest.main()