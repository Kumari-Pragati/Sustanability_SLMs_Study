### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_127_code import intersection
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()
 ### Immediate Task
Write the complete unittest test suite for the following Python function.

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

 import unittest
from HumanEval_127_code import intersection

class TestIntersection(unittest.TestCase):

    def test_no_intersection(self):
        self.assertEqual(intersection((1, 2), (3, 4)), "NO")

    def test_length_not_prime(self):
        self.assertEqual(intersection((-1, 1), (0, 4)), "NO")

    def test_length_prime(self):
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")

    def test_length_zero(self):
        self.assertEqual(intersection((0, 0), (0, 0)), "NO")

    def test_length_one(self):
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")

    def test_length_two(self):
        self.assertEqual(intersection((2, 3), (2, 5)), "NO")

    def test_length_three(self):
        self.assertEqual(intersection((1, 4), (3, 5)), "YES")

    def test_length_four(self):
        self.assertEqual(intersection((1, 5), (2, 6)), "NO")

    def test_length_five(self):
        self.assertEqual(intersection((1, 6), (2, 7)), "YES")

if __name__ == '__main__':
    unittest.main()