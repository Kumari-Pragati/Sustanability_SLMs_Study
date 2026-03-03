system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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


assistant

import unittest

# Test cases for the intersection function
class TestIntersection(unittest.TestCase):

    def test_no_intersection(self):
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")
    
    def test_negative_intervals(self):
        self.assertEqual(intersection((-1, 1), (0, 4)), "NO")

    def test_positive_intervals(self):
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")

    def test_zero_length(self):
        self.assertEqual(intersection((0, 0), (0, 0)), "YES")

    def test_large_number(self):
        self.assertEqual(intersection((1000, 1001), (999, 1000)), "YES")

    def test_small_prime_number(self):
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")

    def test_even_prime_number(self):
        self.assertEqual(intersection((1, 2), (2, 3)), "YES")

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestIntersection` class within the `unittest` module, which contains several test methods to verify the correctness of the `intersection` function. Each method tests different scenarios including no intersection, negative intervals, positive intervals, zero-length intervals, large numbers, small prime numbers, even prime numbers, and other edge cases. The `unittest.main()` call at the end makes the test suite executable when run as a standalone program.