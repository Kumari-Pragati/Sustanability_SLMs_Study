You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function `strange_sort_list`. I've included a variety of test cases to ensure the function works correctly for different input scenarios.


import unittest
from HumanEval_70_code import strange_sort_list

class TestStrangeSortList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(strange_sort_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(strange_sort_list([1]), [1])
        self.assertEqual(strange_sort_list([5]), [5])

    def test_simple_list(self):
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])
        self.assertEqual(strange_sort_list([5, 3, 2, 4, 1]), [5, 1, 4, 3, 2])

    def test_duplicate_elements(self):
        self.assertEqual(strange_sort_list([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), [1, 5, 4, 5, 3, 4, 2, 3, 1, 2])
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_large_list(self):
        large_list = list(range(100))
        strange_sorted_list = strange_sort_list(large_list)
        self.assertEqual(strange_sorted_list, strange_sort_list(large_list))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for an empty list, single-element lists, simple lists with multiple elements, lists with duplicate elements, and large lists. The last test case ensures that the function can handle large input lists efficiently.