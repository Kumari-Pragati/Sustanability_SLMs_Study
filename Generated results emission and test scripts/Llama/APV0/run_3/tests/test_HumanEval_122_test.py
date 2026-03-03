user

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
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_122_code import add_elements

class TestAddElements(unittest.TestCase):

    def test_add_elements(self):
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4), 24)
        self.assertEqual(add_elements([1, 2, 3, 4, 5], 5), 15)
        self.assertEqual(add_elements([100, 200, 300, 400, 500], 5), 1500)
        self.assertEqual(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 45)
        self.assertEqual(add_elements([100, 200, 300, 400, 500, 600, 700, 800, 900], 9), 2700)
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 1), 111)
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 0), 0)
        self.assertEqual(add_elements([], 5), 0)
        self.assertEqual(add_elements([1, 2, 3, 4, 5], 0), 0)

    def test_add_elements_invalid_input(self):
        with self.assertRaises(TypeError):
            add_elements('abc', 4)
        with self.assertRaises(TypeError):
            add_elements([1, 2, 3], 'abc')
        with self.assertRaises(TypeError):
            add_elements([1, 2, 3], 4.5)

if __name__ == '__main__':
    unittest.main()


This script includes 10 test cases to cover different scenarios, including valid inputs, invalid inputs, and edge cases. The `test_add_elements` method tests the function with different inputs and expected outputs, while the `test_add_elements_invalid_input` method tests the function with invalid inputs (non-integer, non-list, or non-integer value for k) and checks if it raises a TypeError.