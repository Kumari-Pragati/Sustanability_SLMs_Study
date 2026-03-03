user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_73_code import smallest_change
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
        smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
        smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
        smallest_change([1, 2, 3, 2, 1]) == 0
    """
    ans = 0
    for i in range(len(arr) // 2):
        if arr[i]!= arr[len(arr) - i - 1]:
            ans += 1
    return ansassistant

Here is the unittest test script for the `smallest_change` function:

import unittest
from HumanEval_73_code import smallest_change

class TestSmallestChange(unittest.TestCase):
    def test_smallest_change(self):
        # Test case 1: [1, 2, 3, 5, 4, 7, 9, 6]
        self.assertEqual(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]), 4)

        # Test case 2: [1, 2, 3, 4, 3, 2, 2]
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)

        # Test case 3: [1, 2, 3, 2, 1]
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)

        # Test case 4: [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8]), 0)

        # Test case 5: [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9]), 0)

        # Test case 6: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 0)

        # Test case 7: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 0)

        # Test case 8: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 0)

        # Test case 9: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), 0)

        # Test case 10: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), 0)

if __name__ == '__main__':
    unittest.main()

This script tests the `smallest_change` function with 10 different test cases, covering various scenarios such as arrays with and without palindromic properties, and arrays of different lengths.