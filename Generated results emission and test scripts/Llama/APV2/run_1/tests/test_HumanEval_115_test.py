system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_115_code import max_fill
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def max_fill(grid, capacity):
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    import math
    return sum([math.ceil(sum(arr) / capacity) for arr in grid])assistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_115_code import max_fill

class TestMaxFill(unittest.TestCase):

    def test_example1(self):
        grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
        capacity = 1
        self.assertEqual(max_fill(grid, capacity), 6)

    def test_example2(self):
        grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
        capacity = 2
        self.assertEqual(max_fill(grid, capacity), 5)

    def test_example3(self):
        grid = [[0,0,0], [0,0,0]]
        capacity = 5
        self.assertEqual(max_fill(grid, capacity), 0)

    def test_grid_with_all_zeros(self):
        grid = [[0,0,0,0], [0,0,0,0], [0,0,0,0]]
        capacity = 1
        self.assertEqual(max_fill(grid, capacity), 0)

    def test_grid_with_all_ones(self):
        grid = [[1,1,1,1], [1,1,1,1], [1,1,1,1]]
        capacity = 1
        self.assertEqual(max_fill(grid, capacity), 12)

    def test_grid_with_mixed_values(self):
        grid = [[0,1,0,1], [1,0,1,0], [0,1,1,0]]
        capacity = 1
        self.assertEqual(max_fill(grid, capacity), 6)

    def test_grid_with_capacity_one(self):
        grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
        capacity = 1
        self.assertEqual(max_fill(grid, capacity), 6)

    def test_grid_with_capacity_five(self):
        grid = [[0,0,0], [0,0,0]]
        capacity = 5
        self.assertEqual(max_fill(grid, capacity), 0)

    def test_grid_with_capacity_zero(self):
        grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
        capacity = 0
        with self.assertRaises(ZeroDivisionError):
            max_fill(grid, capacity)

    def test_grid_with_invalid_input(self):
        grid = 'invalid input'
        capacity = 1
        with self.assertRaises(TypeError):
            max_fill(grid, capacity)

if __name__ == '__main__':
    unittest.main()