You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_74_code import total_match

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    If the two lists have the same number of chars, return the first list.

    Examples:
        total_match([], []) ➞ []
        total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
        total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
        total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
        total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''
    l1 = 0
    for st in lst1:
        l1 += len(st)

    l2 = 0
    for st in lst2:
        l2 += len(st)

    if l1 <= l2:
        return lst1
    else:
        return lst2

 import unittest
from HumanEval_74_code import total_match

class TestTotalMatch(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(total_match([], []), [])

    def test_first_list_shorter(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'Hi']), ['hI', 'Hi'])

    def test_first_list_longer(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])

    def test_second_list_shorter(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']), ['hI', 'hi', 'hi'])

    def test_single_element_lists(self):
        self.assertEqual(total_match(['4'], ['1', '2', '3', '4', '5']), ['4'])

    def test_equal_length_lists(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'hi', 'hi', 'admin']), ['hI', 'hi', 'hi', 'admin'])

    def test_first_list_longer_with_duplicates(self):
        self.assertEqual(total_match(['hi', 'admin', 'admin'], ['hI', 'hi', 'hi']), ['hi', 'hi', 'hi'])

    def test_second_list_longer_with_duplicates(self):
        self.assertEqual(total_match(['hI', 'hi'], ['hi', 'admin', 'admin', 'project']), ['hi', 'admin', 'admin', 'project'])

if __name__ == '__main__':
    unittest.main()