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
    return sorted(odd_digit_elements)

 Here is a unittest test script for the `unique_digits` function:


import unittest
from HumanEval_104_code import unique_digits

class TestUniqueDigits(unittest.TestCase):

    def test_unique_digits(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])
        self.assertEqual(unique_digits([1, 3, 5, 7, 9, 15, 33, 1422, 1]), [1, 3, 5, 7, 9, 15, 33])
        self.assertEqual(unique_digits([10, 20, 30, 40, 50]), [])
        self.assertEqual(unique_digits([1000000000000000000]), [])
        self.assertEqual(unique_digits([]), [])
        self.assertEqual(unique_digits([0]), [])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to ensure the function works correctly for various inputs. The test cases cover the base case (empty list), a list with only even numbers, a list with only odd numbers, a list with a mix of odd and even numbers, and large numbers. The test cases also cover edge cases such as an empty list and a list containing only zeros.