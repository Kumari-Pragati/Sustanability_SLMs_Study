system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_72_code import will_it_fly
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def will_it_fly(q, w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements
    is less than or equal to the maximum possible weight w.

    Example:
        will_it_fly([1, 2], 5) ➞ False 
        # 1+2 is less than the maximum possible weight, but it's unbalanced.

        will_it_fly([3, 2, 3], 1) ➞ False
        # it's balanced, but 3+2+3 is more than the maximum possible weight.

        will_it_fly([3, 2, 3], 9) ➞ True
        # 3+2+3 is less than the maximum possible weight, and it's balanced.

        will_it_fly([3], 5) ➞ True
        # 3 is less than the maximum possible weight, and it's balanced.
    '''
    if sum(q) > w:
        return False

    i, j = 0, len(q) - 1
    while i < j:
        if q[i] != q[j]:
            return False
        i += 1
        j -= 1
    return True


assistant

import unittest

# Provided function to be tested
from HumanEval_72_code import will_it_fly

class TestWillItFly(unittest.TestCase):

    def test_balanced_and_within_weight_limit(self):
        self.assertTrue(will_it_fly([1, 2], 5))
        self.assertFalse(will_it_fly([3, 2, 3], 1))

    def test_unbalanced_but_within_weight_limit(self):
        self.assertTrue(will_it_fly([3, 2, 3], 9))

    def test_balanced_exceeds_weight_limit(self):
        self.assertFalse(will_it_fly([3, 4, 5], 8))

    def test_single_element_within_weight_limit(self):
        self.assertTrue(will_it_fly([1], 5))

    def test_empty_list(self):
        self.assertTrue(will_it_fly([], 5))

if __name__ == '__main__':
    unittest.main()


This unittest test suite includes tests for various scenarios as described in the docstring of `will_it_fly` function. It checks both balanced objects within the weight limit and unbalanced objects exceeding the weight limit.