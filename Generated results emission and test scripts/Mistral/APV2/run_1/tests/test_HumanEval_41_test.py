You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_41_code import car_race_collision
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right; simultaneously, a different set of n cars
    are driving right to left. The two sets of cars start out being very far from
    each other. All cars move at the same speed. Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """
    return n ** 2

 Here is the complete unittest test suite for the `car_race_collision` function:


import unittest
from HumanEval_41_code import car_race_collision

class TestCarRaceCollision(unittest.TestCase):

    def test_car_race_collision(self):
        self.assertEqual(car_race_collision(1), 1)
        self.assertEqual(car_race_collision(2), 4)
        self.assertEqual(car_race_collision(3), 9)
        self.assertEqual(car_race_collision(4), 16)
        self.assertEqual(car_race_collision(5), 25)

if __name__ == '__main__':
    unittest.main()


This test suite includes a single test case class `TestCarRaceCollision` with a single test method `test_car_race_collision`. The test method checks the function's output for various input values (1, 2, 3, 4, and 5) using the `assertEqual` method. If the function's output matches the expected output for the given input, the test passes; otherwise, it fails.