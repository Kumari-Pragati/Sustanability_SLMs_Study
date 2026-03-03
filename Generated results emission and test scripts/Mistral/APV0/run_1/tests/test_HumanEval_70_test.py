Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_70_code import strange_sort_list
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
        strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
        strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
        strange_sort_list([]) == []
    '''
    res, switch = [], True
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res

 Here is a unittest test script for the `strange_sort_list` function:


import unittest
from HumanEval_70_code import strange_sort_list

class TestStrangeSortList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(strange_sort_list([]), [])

    def test_single_element(self):
        self.assertEqual(strange_sort_list([1]), [1])

    def test_simple_list(self):
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])

    def test_duplicate_elements(self):
        self.assertEqual(strange_sort_list([1, 1, 2, 2, 3, 3, 4, 4]), [1, 4, 2, 4, 1, 3, 2, 3])

    def test_all_same_elements(self):
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_large_list(self):
        self.assertEqual(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 9, 2, 8, 3, 7, 4, 6, 5])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as an empty list, a single-element list, a simple list, duplicate elements, all the same elements, and a large list. You can run this script directly to test the `strange_sort_list` function.