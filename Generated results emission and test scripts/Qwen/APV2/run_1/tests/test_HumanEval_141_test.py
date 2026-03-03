system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_141_code import file_name_check
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    suf = ['txt', 'exe', 'dll']
    lst = file_name.split(sep='.')
    if len(lst) != 2:
        return 'No'
    if not lst[1] in suf:
        return 'No'
    if len(lst[0]) == 0:
        return 'No'
    if not lst[0][0].isalpha():
        return 'No'
    t = len([x for x in lst[0] if x.isdigit()])
    if t > 3:
        return 'No'
    return 'Yes'


assistant

import unittest

# Provided function to be tested
from HumanEval_141_code import file_name_check

class TestFileCheck(unittest.TestCase):

    def test_valid_file(self):
        self.assertEqual(file_name_check("example.txt"), "Yes")

    def test_invalid_dot_count(self):
        self.assertEqual(file_name_check("example..txt"), "No")

    def test_invalid_extension(self):
        self.assertEqual(file_name_check("example.exe"), "No")
    
    def test_empty_prefix(self):
        self.assertEqual(file_name_check(".txt"), "No")

    def test_non_alpha_prefix(self):
        self.assertEqual(file_name_check("1example.txt"), "No")

    def test_more_than_three_digits(self):
        self.assertEqual(file_name_check("123example.txt"), "No")

    def test_all_conditions_met(self):
        self.assertEqual(file_name_check("abc.txt"), "Yes")

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various scenarios as described in the problem statement, ensuring that the `file_name_check` function behaves correctly under different conditions.