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

 Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_121_code import solution

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([5, 8, 7, 1]), 12)
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)
        self.assertEqual(solution([30, 13, 24, 321]), 0)
        self.assertEqual(solution([1, 3, 5, 7, 9]), 12)
        self.assertEqual(solution([2, 4, 6, 8, 10]), 0)
        self.assertEqual(solution([1, 2, 3, 4, 5]), 0)
        self.assertEqual(solution([1, 3, 5, 7, 9, 11]), 30)
        self.assertEqual(solution([1, 3, 5, 7, 9, 11, 13]), 60)
        self.assertEqual(solution([1, 3, 5, 7, 9, 11, 13, 15]), 90)
        self.assertEqual(solution([1, 3, 5, 7, 9, 11, 13, 15, 17]), 120)

if __name__ == '__main__':
    unittest.main()


This test suite includes multiple test cases to cover various scenarios, such as lists with even and odd numbers, lists with only even or odd numbers, and lists with a mix of even and odd numbers. The test cases are designed to ensure that the function works correctly for different input lists.