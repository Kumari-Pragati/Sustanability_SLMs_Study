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

 Here is a unittest test script for the `add_elements` function:


import unittest
from HumanEval_122_code import add_elements

class TestAddElements(unittest.TestCase):
    def test_add_elements(self):
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4), 24)
        self.assertEqual(add_elements([1, 2, 3, 400, 5, 6, 7, 8, 9], 8), 21)
        self.assertEqual(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 27)
        self.assertEqual(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 100], 10), 30)
        self.assertEqual(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 1000], 11), 30)

if __name__ == '__main__':
    unittest.main()


This test script includes five test cases to cover different scenarios, including the edge cases where the length of the array and the value of k are at their minimum and maximum values. The test cases are defined in the `TestAddElements` class, and the test suite is run using `unittest.main()`.