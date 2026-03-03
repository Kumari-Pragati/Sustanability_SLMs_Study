Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 import unittest
from HumanEval_41_code import car_race_collision

class TestCarRaceCollision(unittest.TestCase):

    def test_single_car(self):
        # Test with a single car
        self.assertEqual(car_race_collision(1), 1)

    def test_two_cars(self):
        # Test with two cars
        self.assertEqual(car_race_collision(2), 4)

    def test_multiple_cars(self):
        # Test with multiple cars
        self.assertEqual(car_race_collision(3), 9)
        self.assertEqual(car_race_collision(10), 100)

    def test_zero_cars(self):
        # Test with zero cars
        self.assertEqual(car_race_collision(0), 0)

    def test_negative_cars(self):
        # Test with negative number of cars (should raise an error)
        with self.assertRaises(ValueError):
            car_race_collision(-1)

if __name__ == '__main__':
    unittest.main()