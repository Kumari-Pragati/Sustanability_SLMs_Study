system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
    return n ** 2assistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_41_code import car_race_collision

class TestCarRaceCollision(unittest.TestCase):

    def test_car_race_collision(self):
        # Test case 1: n = 0
        self.assertEqual(car_race_collision(0), 0)

        # Test case 2: n = 1
        self.assertEqual(car_race_collision(1), 0)

        # Test case 3: n = 2
        self.assertEqual(car_race_collision(2), 1)

        # Test case 4: n = 3
        self.assertEqual(car_race_collision(3), 4)

        # Test case 5: n = 4
        self.assertEqual(car_race_collision(4), 9)

        # Test case 6: n = 5
        self.assertEqual(car_race_collision(5), 16)

        # Test case 7: n = 10
        self.assertEqual(car_race_collision(10), 100)

        # Test case 8: n = 20
        self.assertEqual(car_race_collision(20), 400)

        # Test case 9: n = 30
        self.assertEqual(car_race_collision(30), 900)

        # Test case 10: n = 40
        self.assertEqual(car_race_collision(40), 1600)

if __name__ == '__main__':
    unittest.main()