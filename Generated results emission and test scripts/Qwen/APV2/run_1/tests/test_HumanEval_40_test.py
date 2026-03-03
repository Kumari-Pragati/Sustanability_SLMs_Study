system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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
    return False


assistant

import unittest

# Provided function
from HumanEval_40_code import triples_sum_to_zero

class TestTriplesSumToZero(unittest.TestCase):

    def test_triples_sum_to_zero(self):
        self.assertEqual(triples_sum_to_zero([1, 3, 5, 0]), False)
        self.assertEqual(triples_sum_to_zero([1, 3, -2, 1]), True)
        self.assertEqual(triples_sum_to_zero([1, 2, 3, 7]), False)
        self.assertEqual(triples_sum_to_zero([2, 4, -5, 3, 9, 7]), True)
        self.assertEqual(triples_sum_to_zero([1]), False)

if __name__ == '__main__':
    unittest.main()


This test suite includes a `TestTriplesSumToZero` class with a single method `test_triples_sum_to_zero`. Each test case checks the function against various inputs to ensure it behaves as expected. The `unittest.main()` call at the end runs these tests when the script is executed directly.