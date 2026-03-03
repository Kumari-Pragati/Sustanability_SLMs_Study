user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_104_code import unique_digits
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    odd_digit_elements = []
    for i in x:
        if all(int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_104_code import unique_digits

class TestUniqueDigits(unittest.TestCase):

    def test_unique_digits(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])
        self.assertEqual(unique_digits([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])
        self.assertEqual(unique_digits([2, 4, 6, 8, 10]), [])
        self.assertEqual(unique_digits([11, 13, 15, 17, 19]), [11, 13, 15, 17, 19])
        self.assertEqual(unique_digits([20, 22, 24, 26, 28]), [])
        self.assertEqual(unique_digits([1, 2, 3, 4, 5]), [1, 3, 5])
        self.assertEqual(unique_digits([10, 20, 30, 40, 50]), [])
        self.assertEqual(unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 3, 5, 7, 9])

if __name__ == '__main__':
    unittest.main()


This script includes 9 test cases to cover different scenarios. Each test case checks if the output of the `unique_digits` function matches the expected output.