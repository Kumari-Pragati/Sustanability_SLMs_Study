system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Function to be tested
from HumanEval_149_code import sorted_list_sum

class TestSortedListSum(unittest.TestCase):
    def test_sorted_list_sum(self):
        # Test case 1
        self.assertEqual(sorted_list_sum(["aa", "a", "aaa"]), ["aa"])
        
        # Test case 2
        self.assertEqual(sorted_list_sum(["ab", "a", "aaa", "cd"]), ["ab", "cd"])
        
        # Test case 3 (with duplicates)
        self.assertEqual(sorted_list_sum(["hello", "world", "hi", "there"]), ["hi", "hello", "world"])
        
        # Test case 4 (empty list)
        self.assertEqual(sorted_list_sum([]), [])
        
        # Test case 5 (single element)
        self.assertEqual(sorted_list_sum(["one"]), ["one"])

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines a test class `TestSortedListSum` which contains a method `test_sorted_list_sum`. Each test case uses assertions to verify the correctness of the `sorted_list_sum` function. The `assertEqual` methods check if the output of the function matches the expected result. Finally, the `unittest.main()` call runs all tests when the script is executed.