system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
    return "NO"assistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_127_code import intersection

class TestIntersection(unittest.TestCase):

    def test_intersection(self):
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")
        self.assertEqual(intersection((-1, 1), (0, 4)), "NO")
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")
        self.assertEqual(intersection((1, 3), (2, 4)), "NO")
        self.assertEqual(intersection((1, 1), (1, 1)), "NO")
        self.assertEqual(intersection((1, 2), (2, 2)), "NO")
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")
        self.assertEqual(intersection((1, 2), (3, 4)), "NO")
        self.assertEqual(intersection((1, 2), (4, 5)), "NO")
        self.assertEqual(intersection((1, 2), (5, 6)), "NO")
        self.assertEqual(intersection((1, 2), (6, 7)), "NO")
        self.assertEqual(intersection((1, 2), (7, 8)), "NO")
        self.assertEqual(intersection((1, 2), (8, 9)), "NO")
        self.assertEqual(intersection((1, 2), (9, 10)), "NO")
        self.assertEqual(intersection((1, 2), (10, 11)), "NO")
        self.assertEqual(intersection((1, 2), (11, 12)), "NO")
        self.assertEqual(intersection((1, 2), (12, 13)), "NO")
        self.assertEqual(intersection((1, 2), (13, 14)), "NO")
        self.assertEqual(intersection((1, 2), (14, 15)), "NO")
        self.assertEqual(intersection((1, 2), (15, 16)), "NO")
        self.assertEqual(intersection((1, 2), (16, 17)), "NO")
        self.assertEqual(intersection((1, 2), (17, 18)), "NO")
        self.assertEqual(intersection((1, 2), (18, 19)), "NO")
        self.assertEqual(intersection((1, 2), (19, 20)), "NO")
        self.assertEqual(intersection((1, 2), (20, 21)), "NO")
        self.assertEqual(intersection((1, 2), (21, 22)), "NO")
        self.assertEqual(intersection((1, 2), (22, 23)), "NO")
        self.assertEqual(intersection((1, 2), (23, 24)), "NO")
        self.assertEqual(intersection((1, 2), (24, 25)), "NO")
        self.assertEqual(intersection((1, 2), (25, 26)), "NO")
        self.assertEqual(intersection((1, 2), (26, 27)), "NO")
        self.assertEqual(intersection((1, 2), (27, 28)), "NO")
        self.assertEqual(intersection((1, 2), (28, 29)), "NO")
        self.assertEqual(intersection((1, 2), (29, 30)), "NO")
        self.assertEqual(intersection((1, 2), (30, 31)), "NO")
        self.assertEqual(intersection((1, 2), (31, 32)), "NO")
        self.assertEqual(intersection((1, 2), (32, 33)), "NO")
        self.assertEqual(intersection((1, 2), (33, 34)), "NO")
        self.assertEqual(intersection((1, 2), (34, 35)), "NO")
        self.assertEqual(intersection((1, 2), (35, 36)), "NO")
        self.assertEqual(intersection((1, 2), (36, 37)), "NO")
        self.assertEqual(intersection((1, 2), (37, 38)), "NO")
        self.assertEqual(intersection((1, 2), (38, 39)), "NO")
        self.assertEqual(intersection((1, 2), (39, 40)), "NO")
        self.assertEqual(intersection((1, 2), (40, 41)), "NO")
        self.assertEqual(intersection((1, 2), (41, 42)), "NO")
        self.assertEqual(intersection((1, 2), (42, 43)), "NO")
        self.assertEqual(intersection((1, 2), (43, 44)), "NO")
        self.assertEqual(intersection((1, 2), (44, 45)), "NO")
        self.assertEqual(inter