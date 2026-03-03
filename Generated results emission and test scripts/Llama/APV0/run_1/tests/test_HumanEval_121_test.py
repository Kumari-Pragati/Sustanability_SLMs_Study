user

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
    return sum([x for idx, x in enumerate(lst) if idx % 2 == 0 and x % 2 == 1])assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_121_code import solution

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([5, 8, 7, 1]), 12)
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)
        self.assertEqual(solution([30, 13, 24, 321]), 0)
        self.assertEqual(solution([1, 2, 3, 4, 5]), 9)
        self.assertEqual(solution([10, 20, 30, 40, 50]), 0)
        self.assertEqual(solution([1, 3, 5, 7, 9]), 15)
        self.assertEqual(solution([2, 4, 6, 8, 10]), 0)

if __name__ == '__main__':
    unittest.main()


This script includes 7 test cases to cover different scenarios. Each test case uses the `assertEqual` method to check if the output of the `solution` function matches the expected result. If the output does not match the expected result, the test will fail and an error message will be displayed.