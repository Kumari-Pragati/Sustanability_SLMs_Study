user

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
        return lst2assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_74_code import total_match

class TestTotalMatch(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(total_match([], []), [])

    def test_lists_with_same_length(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'Hi']), ['hI', 'Hi'])

    def test_lists_with_diff_length(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])

    def test_lists_with_same_chars(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']), ['hI', 'hi', 'hi'])

    def test_lists_with_diff_chars(self):
        self.assertEqual(total_match(['4'], ['1', '2', '3', '4', '5']), ['4'])

    def test_lists_with_empty_strings(self):
        self.assertEqual(total_match(['', ''], ['', '']), ['', ''])

    def test_lists_with_single_element(self):
        self.assertEqual(total_match(['hi'], ['hI']), ['hI'])

    def test_lists_with_multiple_elements(self):
        self.assertEqual(total_match(['hi', 'admin', 'project'], ['hI', 'hi', 'hi', 'admin']), ['hi', 'admin', 'project'])

    def test_lists_with_long_strings(self):
        self.assertEqual(total_match(['hello', 'world'], ['helloworld', 'world']), ['hello', 'world'])

if __name__ == '__main__':
    unittest.main()


This test suite covers a variety of scenarios, including:

- Empty lists
- Lists with the same length
- Lists with different lengths
- Lists with the same number of characters
- Lists with different numbers of characters
- Lists with empty strings
- Lists with single elements
- Lists with multiple elements
- Lists with long strings

Each test case uses the `assertEqual` method to check if the output of the `total_match` function matches the expected output.