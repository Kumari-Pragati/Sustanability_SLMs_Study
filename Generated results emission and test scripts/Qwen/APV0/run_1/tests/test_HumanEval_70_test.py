system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Function to be tested
from HumanEval_70_code import strange_sort_list

class TestStrangeSortList(unittest.TestCase):

    def test_strange_sort_list(self):
        # Test case 1
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])

        # Test case 2
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])

        # Test case 3
        self.assertEqual(strange_sort_list([]), [])

        # Test case 4
        self.assertEqual(strange_sort_list([-1, -2, -3, -4]), [-1, -4, -2, -3])

        # Test case 5
        self.assertEqual(strange_sort_list([9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 9, 2, 8, 3, 7, 4, 6, 5])

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines a test class `TestStrangeSortList`. It includes several test cases that cover different scenarios as described in the docstring of the `strange_sort_list` function. The `assertEqual` method checks if the output of the function matches the expected result. Finally, it calls `unittest.main()` to run all tests.