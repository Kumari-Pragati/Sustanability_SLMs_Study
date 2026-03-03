You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_73_code import smallest_change

class TestSmallestChange(unittest.TestCase):

    def test_palindromic_array(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 1]), 0)
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)
        self.assertEqual(smallest_change([1, 1, 1, 1, 1]), 0)

    def test_non_palindromic_array(self):
        self.assertEqual(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]), 4)
        self.assertEqual(smallest_change([1, 2, 3, 5, 4, 7]), 4)
        self.assertEqual(smallest_change([1, 2, 3, 5, 4]), 3)

    def test_single_element_array(self):
        self.assertEqual(smallest_change([1]), 0)
        self.assertEqual(smallest_change([2]), 0)

    def test_empty_array(self):
        self.assertEqual(smallest_change([]), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for palindromic arrays, non-palindromic arrays, arrays with a single element, and an empty array. It checks that the function returns the correct number of changes needed to make the array palindromic.