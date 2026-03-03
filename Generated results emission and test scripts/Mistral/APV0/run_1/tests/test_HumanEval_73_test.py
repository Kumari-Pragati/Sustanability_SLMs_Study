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
        if arr[i] != arr[len(arr) - i - 1]:
            ans += 1
    return ans

 Here is a unittest test script for the `smallest_change` function:


import unittest
from HumanEval_73_code import smallest_change

class TestSmallestChange(unittest.TestCase):

    def test_smallest_change(self):
        self.assertEqual(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]), 4)
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)
        self.assertEqual(smallest_change([1, 1, 1, 1, 1]), 0)
        self.assertEqual(smallest_change([1, 2, 2, 1, 2]), 1)
        self.assertEqual(smallest_change([10, 10, 10, 10, 10]), 0)
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9]), 9)
        self.assertEqual(smallest_change([1, 1, 1, 1, 1, 1]), 0)
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to ensure the function works correctly for various inputs. You can run this script directly to test the `smallest_change` function.