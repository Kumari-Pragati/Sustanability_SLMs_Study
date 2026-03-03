You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_72_code import will_it_fly

class TestWillItFly(unittest.TestCase):

    def test_sum_greater_than_weight(self):
        self.assertEqual(will_it_fly([1, 2], 1), False)
        self.assertEqual(will_it_fly([3, 2, 3], 1), False)
        self.assertEqual(will_it_fly([3, 2, 3], 2), False)

    def test_not_balanced(self):
        self.assertEqual(will_it_fly([1, 2], 5), False)
        self.assertEqual(will_it_fly([3, 2, 3], 9), False)

    def test_balanced_and_sum_less_than_weight(self):
        self.assertEqual(will_it_fly([3, 2, 3], 9), True)
        self.assertEqual(will_it_fly([3], 5), True)
        self.assertEqual(will_it_fly([1, 2, 1], 5), True)

    def test_single_element(self):
        self.assertEqual(will_it_fly([3], 5), True)
        self.assertEqual(will_it_fly([3], 3), True)
        self.assertEqual(will_it_fly([3], 2), False)

if __name__ == '__main__':
    unittest.main()


This script includes tests for different scenarios:

- When the sum of the elements is greater than the maximum possible weight.
- When the list is not balanced.
- When the list is balanced and the sum of its elements is less than or equal to the maximum possible weight.
- When the list contains only one element.

The script can be run directly to execute the tests.