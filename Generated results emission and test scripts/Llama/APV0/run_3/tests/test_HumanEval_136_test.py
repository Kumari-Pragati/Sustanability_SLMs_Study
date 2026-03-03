user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_136_code import largest_smallest_integers
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_136_code import largest_smallest_integers

class TestLargestSmallestIntegers(unittest.TestCase):

    def test_largest_smallest_integers(self):
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))
        self.assertEqual(largest_smallest_integers([]), (None, None))
        self.assertEqual(largest_smallest_integers([0]), (None, None))
        self.assertEqual(largest_smallest_integers([-1, 0, 1]), (-1, 1))
        self.assertEqual(largest_smallest_integers([-1, -2, 0, 1, 2]), (-2, 1))
        self.assertEqual(largest_smallest_integers([-1, -2, -3, 0, 1, 2, 3]), (-3, 1))

if __name__ == '__main__':
    unittest.main()


This script includes 6 test cases to cover different scenarios:

- Test case 1: The list contains both positive and negative integers.
- Test case 2: The list is empty.
- Test case 3: The list contains only zeros.
- Test case 4: The list contains both positive and negative integers, and the smallest positive integer is 1.
- Test case 5: The list contains both positive and negative integers, and the smallest positive integer is not 1.
- Test case 6: The list contains both positive and negative integers, and the smallest positive integer is not 1, and the largest negative integer is not -1.

Each test case uses the `assertEqual` method to check if the output of the `largest_smallest_integers` function matches the expected output.