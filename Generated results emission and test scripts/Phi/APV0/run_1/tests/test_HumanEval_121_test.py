Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

class TestSolutionFunction(unittest.TestCase):

    def test_sum_of_odd_elements_in_even_positions(self):
        self.assertEqual(solution([5, 8, 7, 1]), 12)
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)
        self.assertEqual(solution([30, 13, 24, 321]), 0)
        self.assertEqual(solution([1, 2, 3, 4, 5, 6]), 0)
        self.assertEqual(solution([10, 11, 12, 13, 14, 15]), 11)
        self.assertEqual(solution([21, 22, 23, 24, 25, 26]), 23)
        self.assertEqual(solution([100, 101, 102, 103, 104, 105]), 101)
        self.assertEqual(solution([21, 22, 23, 24, 25, 26, 27]), 27)
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 7]), 0)
        self.assertEqual(solution([11, 12, 13, 14, 15, 16, 17]), 0)
        self.assertEqual(solution([11, 12, 13, 14, 15, 16, 17, 18]), 18)

    def test_empty_list(self):
        self.assertEqual(solution([]), 0)

    def test_single_element_list(self):
        self.assertEqual(solution([1]), 0)

    def test_all_odd_elements_in_even_positions(self):
        self.assertEqual(solution([1, 3, 5, 7]), 0)

    def test_all_even_elements_in_even_positions(self):
        self.assertEqual(solution([2, 4, 6, 8]), 0)

    def test_all_odd_elements_in_odd_positions(self):
        self.assertEqual(solution([1, 3, 5, 7, 9]), 0)

    def test_all_even_elements_in_odd_positions(self):
        self.assertEqual(solution([2, 4, 6, 8, 10]), 0)

if __name__ == '__main__':
    unittest.main()