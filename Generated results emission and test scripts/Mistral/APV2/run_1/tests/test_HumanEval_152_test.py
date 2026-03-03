You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_152_code import compare
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def compare(game, guess):
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    
    
    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    return [abs(x - y) for x, y in zip(game, guess)]

 Here is the complete unittest test suite for the `compare` function:


import unittest
from HumanEval_152_code import compare

class TestCompareFunction(unittest.TestCase):

    def test_compare_equal_scores(self):
        self.assertEqual(compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]), [0, 0, 0, 0, 3, 3])
        self.assertEqual(compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]), [4, 4, 1, 0, 0, 6])
        self.assertEqual(compare([1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]), [0, 0, 0, 0, 0, 0])

    def test_compare_different_scores(self):
        self.assertEqual(compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 3, -2]), [0, 0, 0, 0, 2, 3])
        self.assertEqual(compare([0, 5, 0, 0, 0, 4], [4, 2, 1, 0, 0, -2]), [4, 3, 1, 0, 0, 6])
        self.assertEqual(compare([1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6]), [0, 1, 2, 3, 4, 5])

    def test_empty_lists(self):
        self.assertEqual(compare([], []), [])
        self.assertEqual(compare([], [1]), [1])
        self.assertEqual(compare([1], []), 1)

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover different scenarios, such as equal scores, different scores, and empty lists. The `assertEqual` function is used to compare the expected and actual results. If the test cases pass, the test suite will not raise any exceptions, indicating that the `compare` function is working correctly. If any test case fails, an `AssertionError` will be raised, and the specific test case that failed will be reported.