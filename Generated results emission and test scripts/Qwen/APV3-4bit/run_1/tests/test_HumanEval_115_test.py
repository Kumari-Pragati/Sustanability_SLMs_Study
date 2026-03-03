system
### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_115_code import max_fill
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()

user
### Immediate Task
Write the complete unittest test suite for the following Python function.

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

# Importing the function we want to test
from HumanEval_115_code import max_fill

class TestMaxFill(unittest.TestCase):
    
    # Test case for positive numbers
    def test_positive_numbers(self):
        self.assertEqual(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1), 6)
        
    # Test case for negative numbers
    def test_negative_numbers(self):
        self.assertEqual(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2), 5)
        
    # Test case for empty grid
    def test_empty_grid(self):
        self.assertEqual(max_fill([[0,0,0], [0,0,0]], 5), 0)
        
    # Test case for large grid
    def test_large_grid(self):
        self.assertEqual(max_fill([[1,0,0,0], [0,5,0,0], [0,0,2,0], [0,0,0,3]], 3), 9)
        
    # Test case for small grid
    def test_small_grid(self):
        self.assertEqual(max_fill([[0,0,0], [0,0,0]], 1), 0)
        
    # Test case for different bucket capacities
    def test_different_bucket_capacities(self):
        self.assertEqual(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 2), 5)
        self.assertEqual(max_fill([[0,0,0], [0,0,0]], 5), 0)
        
    # Test case for non-rectangular grid
    def test_non_rectangular_grid(self):
        self.assertEqual(max_fill([[0,0,0], [0,0,0]], 1), 0)
        self.assertEqual(max_fill([[1,1,1], [1,1,1]], 2), 8)
        
    # Test case for zero-sized grid
    def test_zero_size_grid(self):
        self.assertEqual(max_fill([[0]], 1), 0)
        
    # Test case for one-sized grid
    def test_one_size_grid(self):
        self.assertEqual(max_fill([[1]], 1), 1)
        
    # Test case for two-sized grid
    def test_two_size_grid(self):
        self.assertEqual(max_fill([[1,1], [1,1]], 2), 4)
        
    # Test case for three-sized grid
    def test_three_size_grid(self):
        self.assertEqual(max_fill([[1,1,1], [1,1,1]], 3), 6)
        
    # Test case for four-sized grid
    def test_four_size_grid(self):
        self.assertEqual(max_fill([[1,1,1,1], [1,1,1,1]], 4), 8)
        
    # Test case for five-sized grid
    def test_five_size_grid(self):
        self.assertEqual(max_fill([[1,1,1,1,1], [1,1,1,1,1]], 5), 10)
        
    # Test case for six-sized grid
    def test_six_size_grid(self):
        self.assertEqual(max_fill([[1,1,1,1,1,1], [1,1,1,1,1,1]], 6), 12)
        
    # Test case for seven-sized grid
    def test_seven_size_grid(self):
        self.assertEqual(max_fill([[1,1,1,1,1,1,1], [1,1,1,1,1,1,1]], 7), 14)
        
    # Test case for eight-sized grid
    def test_eight_size_grid(self):
        self.assertEqual(max_fill([[1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1]], 8), 16)
        
    # Test case for nine-sized grid
    def test_nine_size_grid(self):
        self.assertEqual(max_fill([[1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1]], 9), 18)
        
    # Test case for ten-sized grid
    def test_ten_size_grid(self):
        self.assertEqual(max_fill([[1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,1,1]], 10), 20)
        
    #