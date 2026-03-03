You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_152_code import compare

class TestCompare(unittest.TestCase):

    def test_compare(self):
        self.assertEqual(compare([1,2,3,4,5,1],[1,2,3,4,2,-2]), [0,0,0,0,3,3])
        self.assertEqual(compare([0,5,0,0,0,4],[4,1,1,0,0,-2]), [4,4,1,0,0,6])
        self.assertEqual(compare([10,20,30,40,50],[10,20,30,40,50]), [0,0,0,0,0])
        self.assertEqual(compare([-1,-2,-3,-4,-5],[-1,-2,-3,-4,-5]), [0,0,0,0,0])
        self.assertEqual(compare([1,2,3,4,5],[5,4,3,2,1]), [4,2,0,2,4])

if __name__ == '__main__':
    unittest.main()


This script creates a test class `TestCompare` that inherits from `unittest.TestCase`. Inside this class, there is a method `test_compare` that tests the `compare` function with different inputs. The `assertEqual` method is used to check if the output of the `compare` function is as expected.

The `if __name__ == '__main__': unittest.main()` line at the end is used to run the tests when the script is run directly.

Please note that you need to have the `HumanEval_152_code` module with the `compare` function defined in it to run this script.