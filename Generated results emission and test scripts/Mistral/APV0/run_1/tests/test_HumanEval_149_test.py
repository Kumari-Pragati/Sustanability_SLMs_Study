Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `sorted_list_sum` function:


import unittest
from HumanEval_149_code import sorted_list_sum

class TestSortedListSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], sorted_list_sum([]))

    def test_single_element(self):
        self.assertListEqual(["aa"], sorted_list_sum(["aa"]))
        self.assertListEqual(["ab"], sorted_list_sum(["ab"]))

    def test_multiple_elements(self):
        self.assertListEqual(["aa"], sorted_list_sum(["aa", "a", "aaa"]))
        self.assertListEqual(["ab", "cd"], sorted_list_sum(["ab", "a", "aaa", "cd"]))
        self.assertListEqual(["aa", "ab"], sorted_list_sum(["ab", "aa", "a"]))
        self.assertListEqual(["aa", "ab", "cd"], sorted_list_sum(["ab", "cd", "aa"]))

    def test_duplicates(self):
        self.assertListEqual(["aa", "aa"], sorted_list_sum(["aa", "aa", "a"]))
        self.assertListEqual(["aa", "ab", "ab"], sorted_list_sum(["ab", "ab", "aa"]))

    def test_mixed_lengths(self):
        self.assertListEqual(["aa", "ab"], sorted_list_sum(["aa", "ab", "a"]))
        self.assertListEqual(["aa", "ab", "cd"], sorted_list_sum(["ab", "cd", "aa", "a"]))

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as an empty list, single-element lists, multiple elements, duplicates, and lists with mixed lengths. The test cases use the `assertListEqual` method to compare the expected output with the actual output of the `sorted_list_sum` function.