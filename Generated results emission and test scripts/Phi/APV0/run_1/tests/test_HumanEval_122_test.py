Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_122_code import add_elements
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)

 import unittest
from HumanEval_122_code import add_elements

class TestAddElements(unittest.TestCase):

    def test_add_elements_with_two_digit_elements(self):
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4), 24)

    def test_add_elements_with_no_two_digit_elements(self):
        self.assertEqual(add_elements([100, 200, 300, 4000, 5000, 6000], 3), 0)

    def test_add_elements_with_all_two_digit_elements(self):
        self.assertEqual(add_elements([11, 22, 33, 44, 55, 66], 6), 96)

    def test_add_elements_with_k_greater_than_array_length(self):
        self.assertEqual(add_elements([1, 2, 3], 5), 6)

    def test_add_elements_with_empty_array(self):
        self.assertEqual(add_elements([], 5), 0)

    def test_add_elements_with_k_equal_to_zero(self):
        self.assertEqual(add_elements([1, 2, 3], 0), 0)

    def test_add_elements_with_negative_k(self):
        self.assertEqual(add_elements([1, 2, 3], -1), 0)

if __name__ == '__main__':
    unittest.main()