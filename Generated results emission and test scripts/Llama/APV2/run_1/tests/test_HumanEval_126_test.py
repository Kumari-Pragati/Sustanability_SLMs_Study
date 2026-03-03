system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_126_code import is_sorted
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        count_digit[i] += 1 
    if any(count_digit[i] > 2 for i in lst):
        return False
    if all(lst[i - 1] <= lst[i] for i in range(1, len(lst))):
        return True
    else:
        return Falseassistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_126_code import is_sorted

class TestIsSorted(unittest.TestCase):

    def test_is_sorted(self):
        self.assertTrue(is_sorted([5]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))
        self.assertFalse(is_sorted([1, 3, 2, 4, 5]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6, 7]))
        self.assertFalse(is_sorted([1, 3, 2, 4, 5, 6, 7]))
        self.assertTrue(is_sorted([1, 2, 2, 3, 3, 4]))
        self.assertFalse(is_sorted([1, 2, 2, 2, 3, 4]))

    def test_is_sorted_empty_list(self):
        self.assertTrue(is_sorted([]))

    def test_is_sorted_single_element_list(self):
        self.assertTrue(is_sorted([1]))

    def test_is_sorted_duplicates(self):
        self.assertFalse(is_sorted([1, 1, 1, 1, 1]))

    def test_is_sorted_descending(self):
        self.assertFalse(is_sorted([5, 4, 3, 2, 1]))

    def test_is_sorted_empty_list(self):
        self.assertTrue(is_sorted([]))

if __name__ == '__main__':
    unittest.main()