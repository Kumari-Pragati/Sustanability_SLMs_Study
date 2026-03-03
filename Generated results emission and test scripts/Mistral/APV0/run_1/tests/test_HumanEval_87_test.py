Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `get_row` function:


import unittest
from HumanEval_87_code import get_row

class TestGetRow(unittest.TestCase):

    def test_get_row(self):
        data1 = [[1, 2, 3, 4, 5, 6],
                 [1, 2, 3, 4, 1, 6],
                 [1, 2, 3, 4, 5, 1]]
        self.assertEqual(get_row(data1, 1), [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)])

        data2 = []
        self.assertEqual(get_row(data2, 1), [])

        data3 = [[], [1], [1, 2, 3]]
        self.assertEqual(get_row(data3, 3), [(2, 2)])

        data4 = [[1, 1], [2, 2], [1, 1]]
        self.assertEqual(get_row(data4, 1), [(0, 0), (1, 0)])

        data5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(get_row(data5, 5), [(1, 1), (1, 2)])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as an empty list, a list with no occurrences of the given number, and a list with multiple occurrences of the given number in different rows and columns. The test cases are designed to ensure that the function correctly finds the occurrences of the given number and returns the coordinates in the correct order.