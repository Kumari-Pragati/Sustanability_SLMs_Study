You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a Python script for the unittest:


import unittest
from HumanEval_127_code import intersection

class TestIntersection(unittest.TestCase):
    def test_intersection(self):
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")
        self.assertEqual(intersection((-1, 1), (0, 4)), "NO")
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")
        self.assertEqual(intersection((1, 3), (2, 4)), "NO")
        self.assertEqual(intersection((0, 10), (5, 15)), "YES")
        self.assertEqual(intersection((-10, 0), (1, 10)), "NO")
        self.assertEqual(intersection((1, 1), (1, 1)), "NO")
        self.assertEqual(intersection((-1, 0), (-1, 0)), "YES")
        self.assertEqual(intersection((1, 2), (3, 4)), "NO")
        self.assertEqual(intersection((-1, -1), (-1, -1)), "YES")

if __name__ == '__main__':
    unittest.main()


This script includes a class `TestIntersection` that inherits from `unittest.TestCase`. Inside this class, there is a method `test_intersection` that tests the `intersection` function with different inputs and checks if the output is as expected.

The `unittest.main()` at the end runs the test cases.

Please note that the `HumanEval_127_code` module should contain the `intersection` function for the test to pass.