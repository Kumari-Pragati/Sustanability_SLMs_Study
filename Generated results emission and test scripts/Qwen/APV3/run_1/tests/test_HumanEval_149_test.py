system
### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_149_code import sorted_list_sum
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()

user
### Immediate Task
Write the complete unittest test suite for the following Python function.

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

# Provided function
from HumanEval_149_code import sorted_list_sum

class TestSortedListSum(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(sorted_list_sum(["aa", "a", "aaa"]), ["aa"])

    def test_odd_length_strings(self):
        self.assertEqual(sorted_list_sum(["ab", "a", "aaa", "cd"]), ["ab", "cd"])

    def test_duplicates(self):
        self.assertEqual(sorted_list_sum(["aa", "aa", "bb", "cc"]), ["aa", "aa", "cc"])

    def test_empty_list(self):
        self.assertEqual(sorted_list_sum([]), [])

    def test_single_element(self):
        self.assertEqual(sorted_list_sum(["hello"]), ["hello"])

    def test_all_even_length(self):
        self.assertEqual(sorted_list_sum(["aaaa", "bbbb", "cccc"]), ["aaaa", "bbbb", "cccc"])

    def test_mixed_case(self):
        self.assertEqual(sorted_list_sum(["Aaa", "Bb", "Cc", "Dd"]), ["Aaa", "Bb", "Cc", "Dd"])

    def test_multiple_words(self):
        self.assertEqual(sorted_list_sum(["apple", "banana", "cherry", "date"]), ["apple", "banana", "cherry", "date"])

    def test_sorted_by_length_and_alpha(self):
        self.assertEqual(sorted_list_sum(["cat", "dog", "elephant", "fox"]), ["cat", "dog", "fox", "elephant"])

    def test_sorted_by_alpha_only(self):
        self.assertEqual(sorted_list_sum(["apple", "banana", "cherry", "date"]), ["apple", "banana", "cherry", "date"])

    def test_sorted_by_length_first(self):
        self.assertEqual(sorted_list_sum(["cat", "dog", "elephant", "fox"]), ["cat", "dog", "fox", "elephant"])

    def test_sorted_by_alpha_last(self):
        self.assertEqual(sorted_list_sum(["apple", "banana", "cherry", "date"]), ["date", "apple", "banana", "cherry"])

    def test_sorted_by_length_and_alpha_descending(self):
        self.assertEqual(sorted_list_sum(["cat", "dog", "elephant", "fox"]), ["elephant", "fox", "dog", "cat"])

    def test_sorted_by_alpha_and_length_descending(self):
        self.assertEqual(sorted_list_sum(["apple", "banana", "cherry", "date"]), ["date", "banana", "cherry", "apple"])

    def test_sorted_by_length_and_alpha_increasing(self):
        self.assertEqual(sorted_list_sum(["cat", "dog", "elephant", "fox"]), ["cat", "dog", "fox", "elephant"])

    def test_sorted_by_alpha_and_length_increasing(self):
        self.assertEqual(sorted_list_sum(["apple", "banana", "cherry", "date"]), ["apple", "banana", "cherry", "date"])

    def test_sorted_by_length_and_alpha_decreasing(self):
        self.assertEqual(sorted_list_sum(["cat", "dog", "elephant", "fox"]), ["fox", "elephant", "dog", "cat"])

    def test_sorted_by_alpha_and_length_decreasing(self):
        self.assertEqual(sorted_list_sum(["apple", "banana", "cherry", "date"]), ["date", "banana", "cherry", "apple"])

    def test_sorted_by_length_and_alpha_random(self):
        self.assertEqual(sorted_list_sum(["cat", "dog", "elephant", "fox"]), ["cat", "dog", "fox", "elephant"])

    def test_sorted_by_alpha_and_length_random(self):
        self.assertEqual(sorted_list_sum(["apple", "banana", "cherry", "date"]), ["apple", "banana", "cherry", "date"])

    def test_sorted_by_length_and_alpha_alternating(self):
        self.assertEqual(sorted_list_sum(["cat", "dog", "elephant", "fox"]), ["cat", "dog", "fox", "elephant"])

    def test_sorted_by_alpha_and_length_alternating(self):
        self.assertEqual(sorted_list_sum(["apple", "banana", "cherry", "date"]), ["apple", "banana", "cherry", "date"])

    def test_sorted_by_length_and_alpha_reverse(self):
        self.assertEqual(sorted_list_sum(["cat", "dog", "elephant", "fox"]), ["fox", "elephant", "dog", "cat"])

    def test_sorted_by_alpha_and_length_reverse(self):
        self.assertEqual(sorted_list_sum(["apple", "banana", "cherry", "date"]), ["date", "banana", "cherry", "apple"])

    def test_sorted_by_length_and_alpha_custom(self):
        self.assertEqual(sorted_list_sum(["cat", "dog", "elephant", "fox"]), ["cat", "dog", "fox", "elephant"])

    def test_sorted_by_alpha_and_length_custom(self):
        self.assertEqual(sorted_list_sum(["apple", "