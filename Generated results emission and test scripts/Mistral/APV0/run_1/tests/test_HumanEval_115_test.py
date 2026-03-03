Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `max_fill` function:


import unittest
from HumanEval_115_code import max_fill

class TestMaxFill(unittest.TestCase):

    def test_max_fill(self):
        self.assertEqual(max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1), 6)
        self.assertEqual(max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2), 5)
        self.assertEqual(max_fill([[0, 0, 0], [0, 0, 0]], 5), 0)
        self.assertEqual(max_fill([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], 3), 17)
        self.assertEqual(max_fill([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 2), 6)
        self.assertEqual(max_fill([[1], [1], [1]], 1), 3)
        self.assertEqual(max_fill([[0], [0]], 5), 0)

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, including edge cases and cases with large grid sizes and capacities. The test cases are defined in the `test_max_fill` method, and the script ends with the standard unittest setup to run the tests.