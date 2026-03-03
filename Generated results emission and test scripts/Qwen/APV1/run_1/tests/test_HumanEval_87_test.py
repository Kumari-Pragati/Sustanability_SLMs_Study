system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_87_code import get_row

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def get_row(lst, x):
    """
    You are given a 2 dimensional data, as nested lists,
    which is similar to a matrix; however, unlike matrices,
    each row may contain a different number of columns.
    Given lst and integer x, find occurrences of x in the list,
    and return a list of tuples [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, column), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    get_row([
      [1, 2, 3, 4, 5, 6],
      [1, 2, 3, 4, 1, 6],
      [1, 2, 3, 4, 5, 1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """

    coords = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])


assistant

import unittest

# Function to be tested
from HumanEval_87_code import get_row

class TestGetRow(unittest.TestCase):
    def test_get_row(self):
        # Test case 1
        self.assertEqual(get_row([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 1),
                         [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)])

        # Test case 2
        self.assertEqual(get_row([], 1), [])

        # Test case 3
        self.assertEqual(get_row([[[]], [1], [1, 2, 3]], 3),
                         [(2, 2)])

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestGetRow` class that inherits from `unittest.TestCase`. It contains two test cases (`test_get_row`) using the `assertEqual` method to verify the correctness of the `get_row` function against provided test inputs and expected outputs. The `if __name__ == '__main__':` block ensures that when this script is run directly, it will execute all tests defined within the `TestGetRow` class.