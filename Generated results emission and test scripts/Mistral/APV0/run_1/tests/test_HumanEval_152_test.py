Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `compare` function:


import unittest
from HumanEval_152_code import compare

class TestCompareFunction(unittest.TestCase):

    def test_compare(self):
        self.assertEqual(compare([1,2,3,4,5,1], [1,2,3,4,2,-2]), [0,0,0,0,3,3])
        self.assertEqual(compare([0,5,0,0,0,4], [4,1,1,0,0,-2]), [4,4,1,0,0,6])
        self.assertEqual(compare([1,2,3,4,5], [1,2,3,4,5]), [0,0,0,0,0])
        self.assertEqual(compare([1,2,3,4,5], [1,2,3,4,6]), [0,0,0,0,1])
        self.assertEqual(compare([], []), [])
        self.assertEqual(compare([1], [1]), [0])
        self.assertEqual(compare([1], [2]), [1])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to ensure the function works correctly for different inputs. The test cases cover scenarios where the guesses are correct, off by a small amount, off by a large amount, empty lists, and single element lists.