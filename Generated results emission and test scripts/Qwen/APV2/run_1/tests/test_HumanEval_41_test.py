system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Provided function to be tested
from HumanEval_41_code import car_race_collision

class TestCarRaceCollision(unittest.TestCase):

    def test_zero_cars(self):
        self.assertEqual(car_race_collision(0), 0)

    def test_one_car(self):
        self.assertEqual(car_race_collision(1), 1)

    def test_two_cars(self):
        self.assertEqual(car_race_collision(2), 4)

    def test_large_number_of_cars(self):
        large_n = 1000000
        self.assertEqual(car_race_collision(large_n), large_n * large_n)

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases covering edge cases (zero cars, one car, and two cars) as well as larger numbers to ensure the function behaves correctly under various conditions.