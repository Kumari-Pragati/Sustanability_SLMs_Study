You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_70_code import strange_sort_list

class TestStrangeSortList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(strange_sort_list([]), [])

    def test_single_element(self):
        self.assertEqual(strange_sort_list([5]), [5])

    def test_two_elements(self):
        self.assertEqual(strange_sort_list([5, 3]), [3, 5])

    def test_even_length(self):
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])

    def test_odd_length(self):
        self.assertEqual(strange_sort_list([1, 2, 3, 4, 5]), [1, 5, 2, 4, 3])

    def test_duplicate_elements(self):
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_negative_elements(self):
        self.assertEqual(strange_sort_list([-1, -2, -3, -4]), [-4, -1, -2, -3])

    def test_mixed_elements(self):
        self.assertEqual(strange_sort_list([-1, 2, -3, 4]), [-3, 4, -1, 2])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different edge cases, such as empty lists, lists with a single element, lists with two elements, lists of even and odd length, lists with duplicate elements, lists with negative elements, and lists with mixed elements.