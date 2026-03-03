You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_41_code import car_race_collision

class TestCarRaceCollision(unittest.TestCase):

    def test_car_race_collision(self):
        self.assertEqual(car_race_collision(0), 0)
        self.assertEqual(car_race_collision(1), 1)
        self.assertEqual(car_race_collision(2), 4)
        self.assertEqual(car_race_collision(3), 9)
        self.assertEqual(car_race_collision(10), 100)
        self.assertEqual(car_race_collision(100), 10000)

if __name__ == '__main__':
    unittest.main()


This test suite includes a single test case `test_car_race_collision` that tests the function with a variety of input values. The `assertEqual` method is used to check that the output of the function matches the expected result.

Please note that the function `car_race_collision(n: int)` is supposed to return the square of `n`, as per the provided description. The test cases in the unittest test suite are based on this assumption. If the function's behavior changes in the future, the test cases should be updated accordingly.