You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is a complete unittest test suite for the `smallest_change` function:


import unittest
from HumanEval_73_code import smallest_change

class TestSmallestChange(unittest.TestCase):

    def test_smallest_change(self):
        self.assertEqual(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]), 4)
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)
        self.assertEqual(smallest_change([1, 1, 1, 1]), 0)
        self.assertEqual(smallest_change([2, 2, 2, 2]), 0)
        self.assertEqual(smallest_change([1, 2, 2, 1]), 1)
        self.assertEqual(smallest_change([1, 1, 2, 2, 1, 1]), 2)
        self.assertEqual(smallest_change([10, 10, 10, 10]), 0)
        self.assertEqual(smallest_change([1, 1, 1, 1, 1]), 0)
        self.assertEqual(smallest_change([1, 2, 3, 4, 5]), 5)

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover various scenarios, including arrays that are already palindromic, arrays that require a single change to become palindromic, and arrays that require multiple changes. The test cases are designed to be comprehensive and cover edge cases as well.