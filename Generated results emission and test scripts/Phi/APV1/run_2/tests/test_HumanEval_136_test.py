You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
    return (max(smallest) if smallest else None, min(largest) if largest else None)

 import unittest
from HumanEval_136_code import largest_smallest_integers

class TestLargestSmallestIntegers(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(largest_smallest_integers([]), (None, None))

    def test_no_negative_integers(self):
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))

    def test_no_positive_integers(self):
        self.assertEqual(largest_smallest_integers([-2, -4, -1, -3, -5, -7]), (-7, None))

    def test_no_negative_and_no_positive_integers(self):
        self.assertEqual(largest_smallest_integers([0]), (None, None))

    def test_only_negative_integers(self):
        self.assertEqual(largest_smallest_integers([-2, -4, -1, -3, -5, -7]), (-1, None))

    def test_only_positive_integers(self):
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))

    def test_mixed_integers(self):
        self.assertEqual(largest_smallest_integers([-2, -4, -1, 3, 5, 7]), (-1, 3))

    def test_mixed_with_zero(self):
        self.assertEqual(largest_smallest_integers([-2, -4, -1, 0, 5, 7]), (-1, 0))

if __name__ == '__main__':
    unittest.main()