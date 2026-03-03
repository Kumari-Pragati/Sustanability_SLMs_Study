user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
        if q[i]!= q[j]:
            return False
        i += 1
        j -= 1
    return Trueassistant

Here is the unittest test script for the function `will_it_fly`:

import unittest
from HumanEval_72_code import will_it_fly

class TestWillItFly(unittest.TestCase):
    def test_unbalanced_and_overweight(self):
        self.assertFalse(will_it_fly([1, 2], 5))

    def test_balanced_and_overweight(self):
        self.assertFalse(will_it_fly([3, 2, 3], 1))

    def test_balanced_and_just_right(self):
        self.assertTrue(will_it_fly([3, 2, 3], 9))

    def test_single_element_and_just_right(self):
        self.assertTrue(will_it_fly([3], 5))

    def test_single_element_and_underweight(self):
        self.assertTrue(will_it_fly([3], 2))

    def test_empty_list(self):
        self.assertTrue(will_it_fly([], 0))

    def test_list_with_zero(self):
        self.assertTrue(will_it_fly([0], 0))

    def test_list_with_negative(self):
        self.assertFalse(will_it_fly([-1, 2], 3))

if __name__ == '__main__':
    unittest.main()

This script includes 7 test cases to cover various scenarios:

1. Unbalanced and overweight
2. Balanced and overweight
3. Balanced and just right
4. Single element and just right
5. Single element and underweight
6. Empty list
7. List with zero
8. List with negative numbers

Each test case uses the `assertFalse` or `assertTrue` method to verify that the output of the `will_it_fly` function matches the expected result.