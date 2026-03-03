You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_136_code import largest_smallest_integers

class TestLargestSmallestIntegers(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(largest_smallest_integers([]), (None, None))

    def test_list_with_zero(self):
        self.assertEqual(largest_smallest_integers([0]), (None, None))

    def test_list_with_positive_integers(self):
        self.assertEqual(largest_smallest_integers([2, 4, 1, 3, 5, 7]), (None, 1))

    def test_list_with_negative_integers(self):
        self.assertEqual(largest_smallest_integers([-2, -4, -1, -3, -5, -7]), (None, None))

    def test_list_with_mixed_integers(self):
        self.assertEqual(largest_smallest_integers([-2, 4, -1, 3, 5, -7]), (-1, 3))

    def test_list_with_same_integers(self):
        self.assertEqual(largest_smallest_integers([-2, -2, -2, -2, -2]), (None, None))
        self.assertEqual(largest_smallest_integers([2, 2, 2, 2, 2]), (None, 2))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for an empty list, a list with only zero, a list with only positive integers, a list with only negative integers, a list with mixed positive and negative integers, and a list with all the same integers.