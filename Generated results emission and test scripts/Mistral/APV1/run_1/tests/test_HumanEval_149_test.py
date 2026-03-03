You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
    return sorted(new_lst, key=len)

 Here is a comprehensive unittest test suite for the `sorted_list_sum` function:


import unittest
from HumanEval_149_code import sorted_list_sum

class TestSortedListSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sorted_list_sum([]), [])

    def test_single_element(self):
        self.assertEqual(sorted_list_sum(["a"]), ["a"])

    def test_odd_length_strings(self):
        self.assertEqual(sorted_list_sum(["aa", "a", "aaa"]), ["aa"])
        self.assertEqual(sorted_list_sum(["ab", "a", "aaa", "cd"]), ["ab", "cd"])

    def test_duplicates(self):
        self.assertEqual(sorted_list_sum(["aa", "aa", "a"]), ["aa", "a"])
        self.assertEqual(sorted_list_sum(["aa", "aa", "aa"]), ["aa", "aa", "aa"])

    def test_mixed_lengths(self):
        self.assertEqual(sorted_list_sum(["aaa", "aa", "a"]), ["aa", "aaa"])
        self.assertEqual(sorted_list_sum(["aa", "aaa", "a"]), ["aa", "aaa"])
        self.assertEqual(sorted_list_sum(["a", "aa", "aaa"]), ["a", "aa", "aaa"])

    def test_multiple_odd_length_strings(self):
        self.assertEqual(sorted_list_sum(["a", "b"]), [])
        self.assertEqual(sorted_list_sum(["a", "b", "c"]), [])
        self.assertEqual(sorted_list_sum(["a", "b", "c", "d"]), [])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios such as an empty list, single-element lists, lists with duplicates, lists with mixed lengths, and lists containing only odd-length strings. The test cases are designed to ensure that the function works correctly for various inputs and returns the expected output.