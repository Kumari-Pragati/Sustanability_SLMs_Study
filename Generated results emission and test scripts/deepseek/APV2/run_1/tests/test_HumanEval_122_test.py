You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_122_code import add_elements

class TestAddElements(unittest.TestCase):

    def test_add_elements(self):
        # Test with a list of integers
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4), 24)

        # Test with a list of single digit numbers
        self.assertEqual(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 4), 10)

        # Test with a list of numbers with more than two digits
        self.assertEqual(add_elements([111, 222, 333, 444, 555, 666, 777, 888, 999], 4), 0)

        # Test with a list of negative numbers
        self.assertEqual(add_elements([-111, -21, -3, -4000, -5, -6, -7, -8, -9], 4), -24)

        # Test with a list of numbers with leading zeros
        self.assertEqual(add_elements([101, 202, 303, 404, 505, 606, 707, 808, 909], 4), 1010)

        # Test with k=1
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 1), 111)

        # Test with k=len(arr)
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 9), 24)

        # Test with an empty list
        self.assertEqual(add_elements([], 4), 0)

        # Test with k=0
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 0), 0)

        # Test with a list with a single digit number at the kth position
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 5), 21)

        # Test with a list with a number with more than two digits at the kth position
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 666, 7, 8, 9], 5), 21)

        # Test with a list with a number with leading zeros at the kth position
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 606, 7, 8, 9], 5), 21)

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure that the function is working correctly under a variety of conditions.