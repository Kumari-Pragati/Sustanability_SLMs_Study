system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest
from HumanEval_70_code import strange_sort_list

class TestStrangeSortList(unittest.TestCase):

    def test_strange_sort_list(self):
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])
        self.assertEqual(strange_sort_list([]), [])
        self.assertEqual(strange_sort_list([-1, -2, -3, -4]), [-1, -4, -2, -3])
        self.assertEqual(strange_sort_list([9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 9, 2, 8, 3, 7, 4, 6, 5])

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestStrangeSortList` class that inherits from `unittest.TestCase`. It contains a single method `test_strange_sort_list`, which tests the `strange_sort_list` function using several test cases. The `assertEqual` methods compare the output of `strange_sort_list` against expected results, ensuring the function behaves as intended across different scenarios.