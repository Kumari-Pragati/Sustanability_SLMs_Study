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

 import unittest
from HumanEval_149_code import sorted_list_sum

class TestSortedListSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sorted_list_sum([]), [])

    def test_single_element_list(self):
        self.assertEqual(sorted_list_sum(["aa"]), ["aa"])

    def test_multiple_elements_list(self):
        self.assertEqual(sorted_list_sum(["ab", "a", "aaa", "cd"]), ["ab", "cd"])

    def test_all_odd_length_strings(self):
        self.assertEqual(sorted_list_sum(["aa", "a", "aaa", "cd"]), ["cd"])

    def test_all_even_length_strings(self):
        self.assertEqual(sorted_list_sum(["aa", "aaa"]), ["aa", "aaa"])

    def test_duplicate_elements(self):
        self.assertEqual(sorted_list_sum(["aa", "aa", "ab", "ab"]), ["aa", "ab"])

    def test_alphabetical_order_within_same_length(self):
        self.assertEqual(sorted_list_sum(["ba", "aa", "ca"]), ["aa", "ba", "ca"])

    def test_same_length_but_different_words(self):
        self.assertEqual(sorted_list_sum(["ba", "aa", "ca", "da"]), ["aa", "ba", "ca", "da"])

if __name__ == '__main__':
    unittest.main()