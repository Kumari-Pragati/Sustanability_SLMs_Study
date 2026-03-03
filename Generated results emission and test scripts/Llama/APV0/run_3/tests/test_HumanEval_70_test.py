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
    return resassistant

Here is the unittest test script for the `strange_sort_list` function:

import unittest
from HumanEval_70_code import strange_sort_list

class TestStrangeSortList(unittest.TestCase):
    def test_strange_sort_list(self):
        # Test case 1: [1, 2, 3, 4]
        self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])
        # Test case 2: [5, 5, 5, 5]
        self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])
        # Test case 3: []
        self.assertEqual(strange_sort_list([]), [])
        # Test case 4: [1, 3, 2, 4]
        self.assertEqual(strange_sort_list([1, 3, 2, 4]), [1, 4, 2, 3])
        # Test case 5: [2, 1, 3, 4]
        self.assertEqual(strange_sort_list([2, 1, 3, 4]), [1, 4, 2, 3])
        # Test case 6: [1, 2, 3, 4, 5]
        self.assertEqual(strange_sort_list([1, 2, 3, 4, 5]), [1, 5, 2, 4, 3])

if __name__ == '__main__':
    unittest.main()

This script defines a `TestStrangeSortList` class that contains several test methods, each testing a specific input to the `strange_sort_list` function. The `assertEqual` method is used to check that the output of the function matches the expected output.

You can run this script directly to execute the tests. If all tests pass, you should see a message indicating that all tests were successful. If any tests fail, you will see an error message indicating which test failed and why.