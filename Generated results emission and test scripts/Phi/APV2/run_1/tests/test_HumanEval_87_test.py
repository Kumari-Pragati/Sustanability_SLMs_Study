You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 import unittest
from HumanEval_87_code import get_row

class TestGetRow(unittest.TestCase):

    def test_get_row_with_occurrences(self):
        lst = [
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 1, 6],
            [1, 2, 3, 4, 5, 1]
        ]
        x = 1
        expected = [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
        self.assertEqual(get_row(lst, x), expected)

    def test_get_row_with_no_occurrences(self):
        lst = []
        x = 1
        expected = []
        self.assertEqual(get_row(lst, x), expected)

    def test_get_row_with_single_occurrence(self):
        lst = [[], [1], [1, 2, 3]]
        x = 3
        expected = [(2, 2)]
        self.assertEqual(get_row(lst, x), expected)

    def test_get_row_with_empty_list(self):
        lst = []
        x = 1
        expected = []
        self.assertEqual(get_row(lst, x), expected)

    def test_get_row_with_duplicate_elements(self):
        lst = [
            [1, 2, 3, 4, 5, 6],
            [1, 2, 3, 4, 1, 6],
            [1, 2, 3, 4, 5, 1],
            [1, 1, 1, 1, 1, 1]
        ]
        x = 1
        expected = [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5)]
        self.assertEqual(get_row(lst, x), expected)

if __name__ == '__main__':
    unittest.main()