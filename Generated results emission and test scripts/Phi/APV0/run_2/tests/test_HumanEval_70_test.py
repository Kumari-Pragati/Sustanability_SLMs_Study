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

 import unittest
from HumanEval_70_code import strange_sort_list

class TestStrangeSortList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(strange_sort_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(strange_sort_list([5]), [5])

    def test_list_with_all_same_elements(self):
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_normal_list(self):
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])

    def test_negative_numbers(self):
        self.assertEqual(strange_sort_list([-1, -2, -3, -4]), [-1, -4, -2, -3])

    def test_mixed_numbers(self):
        self.assertEqual(strange_sort_list([1, -2, 3, -4]), [1, -4, 3, -2])

    def test_large_numbers(self):
        self.assertEqual(strange_sort_list([100, 200, 300, 400]), [100, 400, 200, 300])

    def test_zero_numbers(self):
        self.assertEqual(strange_sort_list([0]), [0])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            strange_sort_list([1, "2", 3, 4])

if __name__ == '__main__':
    unittest.main()