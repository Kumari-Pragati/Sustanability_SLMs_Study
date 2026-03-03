You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

 
import unittest
from HumanEval_121_code import solution

class TestSolution(unittest.TestCase):

    def test_solution_with_odd_elements_in_even_positions(self):
        self.assertEqual(solution([5, 8, 7, 1]), 12)

    def test_solution_with_all_odd_numbers(self):
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)

    def test_solution_with_no_odd_elements_in_even_positions(self):
        self.assertEqual(solution([30, 13, 24, 321]), 0)

    def test_solution_with_empty_list(self):
        self.assertEqual(solution([]), 0)

    def test_solution_with_single_element(self):
        self.assertEqual(solution([1]), 0)

    def test_solution_with_all_even_elements(self):
        self.assertEqual(solution([2, 4, 6, 8]), 0)

    def test_solution_with_mixed_elements(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6]), 0)

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios to ensure that the `solution` function behaves as expected. It tests the function with different lists, including cases with odd elements in even positions, all odd numbers, no odd elements in even positions, empty lists, single-element lists, and lists with mixed elements. Each test case uses the `assertEqual` method to compare the output of the `solution` function with the expected result. Running this test suite will execute all the tests and report any failures or errors.