You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_121_code import solution

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    
    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==> 0
    """
    return sum([x for idx, x in enumerate(lst) if idx % 2 == 0 and x % 2 == 1])

 import unittest
from HumanEval_121_code import solution

class TestSolution(unittest.TestCase):

    def test_sum_of_odd_elements_in_even_positions(self):
        self.assertEqual(solution([5, 8, 7, 1]), 12)
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)
        self.assertEqual(solution([30, 13, 24, 321]), 0)
        self.assertEqual(solution([1, 2, 3, 4, 5, 6]), 0)
        self.assertEqual(solution([11, 12, 13, 14, 15]), 13)
        self.assertEqual(solution([21, 22, 23, 24, 25]), 23)
        self.assertEqual(solution([100, 101, 102, 103, 104]), 101)
        self.assertEqual(solution([7, 8, 9, 10, 11, 12]), 0)
        self.assertEqual(solution([2, 4, 6, 8, 10]), 0)
        self.assertEqual(solution([1, 3, 5, 7, 9, 11]), 16)
        self.assertEqual(solution([2, 4, 6, 8, 10, 12]), 0)
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 16)
        self.assertEqual(solution([11, 13, 15, 17, 19, 21]), 34)
        self.assertEqual(solution([2, 4, 6, 8, 10, 12, 14]), 0)
        self.assertEqual(solution([1, 3, 5, 7, 9, 11, 13]), 28)
        self.assertEqual(solution([2, 4, 6, 8, 10, 12, 14, 16]), 0)
        self.assertEqual(solution([1, 3, 5, 7, 9, 11, 13, 15]), 24)
        self.assertEqual(solution([2, 4, 6, 8, 10, 12, 14, 16, 18]), 0)
        self.assertEqual(solution([1, 3, 5, 7, 9, 11, 13, 15, 17]), 36)
        self.assertEqual(solution([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]), 0)
        self.assertEqual(solution([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]), 40)
        self.assertEqual(solution([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]), 0)
        self.assertEqual(solution([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]), 56)
        self.assertEqual(solution([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]), 0)
        self.assertEqual(solution([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]), 6