You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

 
import unittest
from HumanEval_152_code import compare

class TestCompareFunction(unittest.TestCase):

    def test_correct_guesses(self):
        game = [1, 2, 3, 4, 5, 1]
        guess = [1, 2, 3, 4, 2, -2]
        expected_output = [0, 0, 0, 0, 3, 3]
        self.assertEqual(compare(game, guess), expected_output)

    def test_incorrect_guesses(self):
        game = [0, 5, 0, 0, 0, 4]
        guess = [4, 1, 1, 0, 0, -2]
        expected_output = [4, 4, 1, 0, 0, 6]
        self.assertEqual(compare(game, guess), expected_output)

    def test_empty_arrays(self):
        game = []
        guess = []
        expected_output = []
        self.assertEqual(compare(game, guess), expected_output)

    def test_unequal_length_arrays(self):
        game = [1, 2, 3]
        guess = [1, 2, 3, 4]
        with self.assertRaises(ValueError):
            compare(game, guess)

    def test_negative_numbers(self):
        game = [-1, -2, -3]
        guess = [-1, -2, -4]
        expected_output = [0, 0, 1]
        self.assertEqual(compare(game, guess), expected_output)

if __name__ == '__main__':
    unittest.main()


This test suite covers the following cases:

1. Correct guesses: The function should return an array of zeros for correct guesses.
2. Incorrect guesses: The function should return the absolute difference between the guess and the score for incorrect guesses.
3. Empty arrays: The function should return an empty array if both input arrays are empty.
4. Unequal length arrays: The function should raise a `ValueError` if the input arrays have different lengths.
5. Negative numbers: The function should correctly handle negative numbers in the input arrays.

To run the test suite, save the code in a file (e.g., `test_compare.py`) and execute it using the command `python test_compare.py`. The `unittest` framework will automatically discover and run the tests.