You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_127_code import intersection

class TestIntersection(unittest.TestCase):
    def test_intersection_yes(self):
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")
        self.assertEqual(intersection((-1, 1), (0, 4)), "NO")

    def test_intersection_no(self):
        self.assertEqual(intersection((1, 2), (3, 4)), "NO")
        self.assertEqual(intersection((-1, 1), (-2, -1)), "NO")
        self.assertEqual(intersection((-3, -1), (-4, -2)), "NO")

    def test_intersection_edge_cases(self):
        self.assertEqual(intersection((1, 1), (1, 1)), "NO")
        self.assertEqual(intersection((1, 2), (2, 2)), "NO")
        self.assertEqual(intersection((-1, -1), (-2, -2)), "NO")

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_intersection_yes` - This test case checks the function with intervals that should return "YES".
2. `test_intersection_no` - This test case checks the function with intervals that should return "NO".
3. `test_intersection_edge_cases` - This test case checks the function with edge cases, such as intervals with a single element or two equal elements.

Please note that the function `intersection` should be defined in a separate file named `HumanEval_127_code.py` for this test suite to work.