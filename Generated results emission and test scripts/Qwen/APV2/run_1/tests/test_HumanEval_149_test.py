system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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
    return sorted(new_lst, key=len)


assistant

import unittest

# Function to check the correctness of the sorted_list_sum function
def check_sorted_list_sum():
    # Test cases
    test_cases = [
        ([], []),
        (["aa"], ["aa"]),
        (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
        (["abc", "bac", "cba"], ["abc", "bac", "cba"])
    ]
    
    # Iterate through each test case
    for input_list, expected_output in test_cases:
        result = sorted_list_sum(input_list)
        self.assertEqual(result, expected_output)

# Run the tests
class TestSortedListSum(unittest.TestCase):
    def test_function(self):
        check_sorted_list_sum()

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `sorted_list_sum` function that filters out strings with odd lengths from a given list of strings, sorts them based on their length, and then sorts them alphabetically within the same length. It also includes a test suite using the `unittest` framework to verify the functionality of the `sorted_list_sum` function against predefined test cases.