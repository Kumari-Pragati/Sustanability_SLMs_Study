Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_159_code import eat
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    You should return a list of:
        [ total number of eaten carrots after your meals,
          the number of carrots left after your meals ]
    If there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    
    Examples:
    eat(5, 6, 10) -> [11, 4]
    eat(4, 8, 9) -> [12, 1]
    eat(1, 10, 10) -> [11, 0]
    eat(2, 11, 5) -> [7, 0]
    """
    if need <= remaining:
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]

 Here is a unittest test script for the `eat` function:


import unittest
from HumanEval_159_code import eat

class TestEatFunction(unittest.TestCase):

    def test_eat(self):
        self.assertEqual(eat(5, 6, 10), [11, 4])
        self.assertEqual(eat(4, 8, 9), [12, 1])
        self.assertEqual(eat(1, 10, 10), [11, 0])
        self.assertEqual(eat(2, 11, 5), [7, 0])
        self.assertEqual(eat(0, 10, 10), [10, 0])
        self.assertEqual(eat(10, 1, 1), [11, 0])
        self.assertEqual(eat(0, 0, 10), [0, 10])
        self.assertEqual(eat(10, 11, 5), [0, 0])
        self.assertEqual(eat(10, 11, 4), [11, 0])

if __name__ == '__main__':
    unittest.main()


This test script includes a test function `test_eat` that tests the `eat` function with various inputs. If the function works correctly, the test will pass. If not, the test will fail, and you'll be able to see the expected and actual outputs to help you debug the issue.