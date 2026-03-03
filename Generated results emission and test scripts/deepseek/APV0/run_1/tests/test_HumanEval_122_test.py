You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_122_code import add_elements

class TestAddElements(unittest.TestCase):
    def test_add_elements(self):
        # Test case 1: k is equal to the length of the array
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 9), 24)

        # Test case 2: k is less than the length of the array
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4), 24)

        # Test case 3: k is equal to 1
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 1), 21)

        # Test case 4: k is equal to 1 and the element is a two-digit number
        self.assertEqual(add_elements([11, 21, 3, 4000, 5, 6, 7, 8, 9], 1), 11)

        # Test case 5: k is equal to 1 and the element is a single-digit number
        self.assertEqual(add_elements([1, 21, 3, 4000, 5, 6, 7, 8, 9], 1), 1)

        # Test case 6: k is equal to 1 and the element is a four-digit number
        self.assertEqual(add_elements([1111, 21, 3, 4000, 5, 6, 7, 8, 9], 1), 0)

        # Test case 7: k is equal to 0
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 0), 0)

        # Test case 8: k is equal to 100
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 100), 24)

        # Test case 9: array is empty
        self.assertEqual(add_elements([], 1), 0)

        # Test case 10: k is greater than the length of the array
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 10), 24)

if __name__ == '__main__':
    unittest.main()


This script includes 10 test cases to cover all possible scenarios. It tests the function with different values of k and different arrays. The expected results are calculated manually based on the function's description.