You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is a complete unittest test suite for the provided Python function:


import unittest
from HumanEval_121_code import solution

class TestSolution(unittest.TestCase):

    def test_solution_1(self):
        self.assertEqual(solution([5, 8, 7, 1]), 12)

    def test_solution_2(self):
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)

    def test_solution_3(self):
        self.assertEqual(solution([30, 13, 24, 321]), 0)

    def test_solution_4(self):
        self.assertEqual(solution([1, 3, 5, 7]), 10)

    def test_solution_5(self):
        self.assertEqual(solution([0, 2, 4, 6]), 0)

    def test_solution_6(self):
        self.assertEqual(solution([1, 2, 3, 4]), 2)

    def test_solution_7(self):
        self.assertEqual(solution([]), 0)

    def test_solution_8(self):
        self.assertEqual(solution([1]), 0)

    def test_solution_9(self):
        self.assertEqual(solution([2, 2, 2, 2]), 0)

    def test_solution_10(self):
        self.assertEqual(solution([1, 2, 3, 4, 5]), 10)

if __name__ == '__main__':
    unittest.main()


This test suite includes 10 test cases to cover various scenarios, such as empty lists, lists with only even or odd numbers, and lists with a mix of even and odd numbers.