system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_149_code import sorted_list_sum
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    lst.sort()
    new_lst = []
    for i in lst:
        if len(i) % 2 == 0:
            new_lst.append(i)
    return sorted(new_lst, key=len)assistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_149_code import sorted_list_sum

class TestSortedListSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sorted_list_sum([]), [])

    def test_single_element_list(self):
        self.assertEqual(sorted_list_sum(["aa"]), ["aa"])

    def test_list_with_odd_length_strings(self):
        self.assertEqual(sorted_list_sum(["a", "aa", "aaa"]), [])

    def test_list_with_even_length_strings(self):
        self.assertEqual(sorted_list_sum(["aa", "aaa"]), ["aa"])

    def test_list_with_duplicates(self):
        self.assertEqual(sorted_list_sum(["aa", "aa", "aaa"]), ["aa"])

    def test_list_with_multiple_elements(self):
        self.assertEqual(sorted_list_sum(["ab", "a", "aaa", "cd"]), ["ab", "cd"])

    def test_list_with_multiple_elements_and_duplicates(self):
        self.assertEqual(sorted_list_sum(["aa", "aa", "ab", "aaa", "cd"]), ["aa", "ab", "cd"])

if __name__ == '__main__':
    unittest.main()