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

 import unittest
from HumanEval_70_code import strange_sort_list

class TestStrangeSortList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(strange_sort_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(strange_sort_list([5]), [5])

    def test_list_with_all_same_elements(self):
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_list_with_increasing_elements(self):
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])

    def test_list_with_decreasing_elements(self):
        self.assertEqual(strange_sort_list([4, 3, 2, 1]), [1, 4, 2, 3])

    def test_list_with_mixed_elements(self):
        self.assertEqual(strange_sort_list([3, 1, 4, 2]), [1, 4, 2, 3])

    def test_list_with_negative_elements(self):
        self.assertEqual(strange_sort_list([-1, -3, -2, -4]), [-4, -1, -3, -2])

    def test_list_with_zero_elements(self):
        self.assertEqual(strange_sort_list([0]), [0])

    def test_list_with_large_numbers(self):
        self.assertEqual(strange_sort_list([1000, 2000, 3000, 4000]), [1000, 4000, 2000, 3000])

if __name__ == '__main__':
    unittest.main()