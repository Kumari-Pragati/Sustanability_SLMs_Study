You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given function:


import unittest
from HumanEval_121_code import solution

class TestSolution(unittest.TestCase):
    def test_odd_in_even_positions(self):
        self.assertEqual(solution([5, 8, 7, 1]), 12)
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)
        self.assertEqual(solution([30, 13, 24, 321]), 0)
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]), 10)
        self.assertEqual(solution([10, 11, 12, 13, 14, 15]), 26)
        self.assertEqual(solution([1, 3, 5, 7, 9]), 0)
        self.assertEqual(solution([2, 4, 6, 8, 10]), 0)
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 11)

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover different scenarios. The test `test_odd_in_even_positions` checks the function with lists containing odd numbers in even positions, even numbers in even positions, odd numbers in odd positions, even numbers in odd positions, and lists with no odd numbers in even positions.

Please note that the function `solution` is expected to be in a file named `HumanEval_121_code.py` in the same directory as the test file.