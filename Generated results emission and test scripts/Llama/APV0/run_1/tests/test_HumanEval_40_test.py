user

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
    return Falseassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_40_code import triples_sum_to_zero

class TestTriplesSumToZero(unittest.TestCase):

    def test_triples_sum_to_zero(self):
        self.assertFalse(triples_sum_to_zero([1, 3, 5, 0]))
        self.assertTrue(triples_sum_to_zero([1, 3, -2, 1]))
        self.assertFalse(triples_sum_to_zero([1, 2, 3, 7]))
        self.assertTrue(triples_sum_to_zero([2, 4, -5, 3, 9, 7]))
        self.assertFalse(triples_sum_to_zero([1]))
        self.assertFalse(triples_sum_to_zero([]))
        self.assertFalse(triples_sum_to_zero([0]))
        self.assertTrue(triples_sum_to_zero([-1, 1, 0]))
        self.assertFalse(triples_sum_to_zero([1, 1, 1]))

if __name__ == '__main__':
    unittest.main()


This script includes 9 test cases to cover different scenarios. The test cases are designed to test the function with different inputs, including lists with and without three distinct elements that sum to zero, as well as lists with only one or no elements. The expected output for each test case is specified using the `assertTrue` and `assertFalse` methods.