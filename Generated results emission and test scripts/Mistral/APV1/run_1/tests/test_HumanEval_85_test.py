You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_85_code import add

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def add(lst):
    """Given a non-empty list of integers lst. Add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0])

 Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_85_code import add

class TestAddFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(add([]), 0)

    def test_single_even_at_odd_index(self):
        self.assertEqual(add([2]), 2)

    def test_single_odd_at_odd_index(self):
        self.assertEqual(add([1]), 0)

    def test_multiple_even_at_odd_index(self):
        self.assertEqual(add([2, 4, 6]), 10)

    def test_multiple_odd_at_odd_index(self):
        self.assertEqual(add([1, 3, 5]), 0)

    def test_mixed_even_and_odd_at_odd_index(self):
        self.assertEqual(add([2, 1, 4, 3]), 2)

    def test_list_with_only_even_numbers(self):
        self.assertEqual(add([2, 4, 6]), 10)

    def test_list_with_only_odd_numbers(self):
        self.assertEqual(add([1, 3, 5]), 0)

    def test_list_with_even_and_odd_numbers(self):
        self.assertEqual(add([2, 1, 4, 3]), 2)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios such as an empty list, single even or odd numbers at odd indices, multiple even and odd numbers at odd indices, and lists with only even or odd numbers. It also covers the case when the list contains both even and odd numbers.