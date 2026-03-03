You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_127_code import intersection
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def intersection(interval1, interval2):
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".

    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    """
    def is_prime(num):
        if num == 1 or num == 0:
            return False
        if num == 2:
            return True
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    l = max(interval1[0], interval2[0])
    r = min(interval1[1], interval2[1])
    length = r - l
    if length > 0 and is_prime(length):
        return "YES"
    return "NO"

 Here is the complete unittest test suite for the provided `intersection` function:


import unittest
from HumanEval_127_code import intersection

class TestIntersection(unittest.TestCase):

    def test_intersection_no_intersection(self):
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")
        self.assertEqual(intersection((-1, 1), (0, 4)), "NO")

    def test_intersection_no_prime_length(self):
        self.assertEqual(intersection((1, 3), (2, 4)), "NO")
        self.assertEqual(intersection((0, 1), (1, 2)), "NO")
        self.assertEqual(intersection((-3, -1), (-5, -2)), "NO")

    def test_intersection_prime_length(self):
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")
        self.assertEqual(intersection((-5, -3), (-7, 7)), "YES")
        self.assertEqual(intersection((-7, -5), (-9, -1)), "YES")

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_intersection_no_intersection` checks that the function returns "NO" when the two intervals do not intersect.
2. `test_intersection_no_prime_length` checks that the function returns "NO" when the length of the intersection is not a prime number.
3. `test_intersection_prime_length` checks that the function returns "YES" when the length of the intersection is a prime number.

The test suite uses the built-in `unittest.TestCase` class to define test methods and the `assertEqual` method to compare the expected and actual results.