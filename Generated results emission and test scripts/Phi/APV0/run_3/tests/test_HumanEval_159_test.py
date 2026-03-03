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

 import unittest
from HumanEval_159_code import eat

class TestEatFunction(unittest.TestCase):

    def test_eat_enough_carrots(self):
        self.assertEqual(eat(5, 6, 10), [11, 4])

    def test_eat_more_carrots_than_available(self):
        self.assertEqual(eat(4, 8, 9), [12, 1])

    def test_eat_all_carrots(self):
        self.assertEqual(eat(1, 10, 10), [11, 0])

    def test_eat_less_carrots_than_needed(self):
        self.assertEqual(eat(2, 11, 5), [7, 0])

    def test_eat_zero_carrots(self):
        self.assertEqual(eat(0, 5, 10), [5, 5])

    def test_eat_negative_numbers(self):
        self.assertEqual(eat(-1, 5, 10), [9, 10])

    def test_eat_negative_remaining_carrots(self):
        self.assertEqual(eat(5, 6, -10), [5, -10])

    def test_eat_negative_number_of_carrots_eaten(self):
        self.assertEqual(eat(-1, 6, 10), [9, 1])

if __name__ == '__main__':
    unittest.main()