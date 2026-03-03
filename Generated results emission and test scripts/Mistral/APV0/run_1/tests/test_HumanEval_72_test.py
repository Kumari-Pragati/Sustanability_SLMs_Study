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
        if q[i] != q[j]:
            return False
        i += 1
        j -= 1
    return True

 Here is a unittest test script for the `will_it_fly` function:


import unittest
from HumanEval_72_code import will_it_fly

class TestWillItFly(unittest.TestCase):

    def test_will_it_fly(self):
        self.assertFalse(will_it_fly([1, 2], 5))
        self.assertFalse(will_it_fly([3, 2, 3], 1))
        self.assertTrue(will_it_fly([3, 2, 3], 9))
        self.assertTrue(will_it_fly([3], 5))
        self.assertTrue(will_it_fly([1, 2, 1], 4))
        self.assertFalse(will_it_fly([1, 2, 3], 4))
        self.assertTrue(will_it_fly([10, 20, 30, 40, 50], 150))
        self.assertFalse(will_it_fly([10, 20, 30, 40, 51], 150))
        self.assertTrue(will_it_fly([], 0))
        self.assertFalse(will_it_fly([1], 0))

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to ensure the function works correctly for various inputs. The test cases cover scenarios where the object will not fly (unbalanced or exceeding the maximum possible weight), scenarios where the object will fly (balanced and within the maximum possible weight), and edge cases (empty list, single-element list, and a list with an odd number of elements).