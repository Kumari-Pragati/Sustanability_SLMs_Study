You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 import unittest
from HumanEval_73_code import smallest_change

class TestSmallestChange(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(smallest_change([]), 0)

    def test_single_element_array(self):
        self.assertEqual(smallest_change([1]), 0)

    def test_palindromic_array(self):
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)

    def test_non_palindromic_array_with_one_change(self):
        self.assertEqual(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]), 4)

    def test_non_palindromic_array_with_no_changes(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)

    def test_non_palindromic_array_with_multiple_changes(self):
        self.assertEqual(smallest_change([1, 2, 3, 5, 6, 7, 9, 4]), 4)

    def test_non_palindromic_array_with_large_changes(self):
        self.assertEqual(smallest_change([1, 2, 3, 5, 8, 9, 7, 6]), 4)

    def test_non_palindromic_array_with_all_different_elements(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 5, 6, 7, 8]), 4)

if __name__ == '__main__':
    unittest.main()