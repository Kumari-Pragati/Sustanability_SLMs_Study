system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
    return sum([math.ceil(sum(arr) / capacity) for arr in grid])


assistant

import unittest
from HumanEval_115_code import max_fill

class TestMaxFill(unittest.TestCase):
    def test_example_1(self):
        grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
        self.assertEqual(max_fill(grid, 1), 6)

    def test_example_2(self):
        grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
        self.assertEqual(max_fill(grid, 2), 5)

    def test_example_3(self):
        grid = [[0,0,0], [0,0,0]]
        self.assertEqual(max_fill(grid, 5), 0)

    def test_empty_grid(self):
        grid = []
        self.assertEqual(max_fill(grid, 1), 0)

    def test_single_well(self):
        grid = [[1]]
        self.assertEqual(max_fill(grid, 1), 1)

    def test_large_grid(self):
        grid = [[1]*100 for _ in range(10)]
        self.assertEqual(max_fill(grid, 1), 99)

if __name__ == '__main__':
    unittest.main()


This code defines a `TestMaxFill` class that inherits from `unittest.TestCase`. It contains several test methods to verify the correctness of the `max_fill` function against various scenarios as described in the problem statement. The `test_example_1`, `test_example_2`, `test_example_3`, `test_empty_grid`, `test_single_well`, and `test_large_grid` methods call the `max_fill` function with different inputs and assert that the output matches the expected result. If any of these tests fail, the corresponding assertion will raise an error, indicating that there's something wrong with the implementation of the `max_fill` function.