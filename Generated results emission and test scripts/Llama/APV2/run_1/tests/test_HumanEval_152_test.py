system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
    return [abs(x - y) for x, y in zip(game, guess)]assistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_152_code import compare

class TestCompareFunction(unittest.TestCase):

    def test_compare_function(self):
        self.assertEqual(compare([1,2,3,4,5,1],[1,2,3,4,2,-2]), [0,0,0,0,3,3])
        self.assertEqual(compare([0,5,0,0,0,4],[4,1,1,0,0,-2]), [4,4,1,0,0,6])
        self.assertEqual(compare([1,1,1,1,1,1],[1,1,1,1,1,1]), [0,0,0,0,0,0])
        self.assertEqual(compare([1,2,3,4,5,6],[1,2,3,4,5,7]), [0,0,0,0,1,1])
        self.assertEqual(compare([1,2,3,4,5,6],[1,2,3,4,5,0]), [0,0,0,0,0,6])
        self.assertEqual(compare([1,2,3,4,5,6],[1,2,3,4,5,8]), [0,0,0,0,1,2])

if __name__ == '__main__':
    unittest.main()