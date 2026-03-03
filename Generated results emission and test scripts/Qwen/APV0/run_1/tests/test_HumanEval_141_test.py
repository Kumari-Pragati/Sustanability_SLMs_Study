system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

# Importing the function we want to test
from HumanEval_141_code import file_name_check

class TestFileCheck(unittest.TestCase):

    def test_valid_file(self):
        self.assertEqual(file_name_check("example.txt"), "Yes")
    
    def test_invalid_file_start_with_number(self):
        self.assertEqual(file_name_check("1example.txt"), "No")

    def test_invalid_file_after_dot_not_one_of_the_allowed_extensions(self):
        self.assertEqual(file_name_check("example..txt"), "No")

    def test_invalid_file_before_dot_empty_string(self):
        self.assertEqual(file_name_check(".example.txt"), "No")

    def test_invalid_file_before_dot_starts_with_non_alpha_char(self):
        self.assertEqual(file_name_check("_example.txt"), "No")

    def test_invalid_file_before_dot_too_many_digits(self):
        self.assertEqual(file_name_check("123example.txt"), "No")

    def test_invalid_file_after_dot_not_in_list(self):
        self.assertEqual(file_name_check("example.txt.exe"), "No")

if __name__ == '__main__':
    unittest.main()


This script imports the `file_name_check` function and creates a class named `TestFileCheck`. It then defines several test cases using the `assertEqual` method to check that the function behaves as expected under different scenarios. Finally, it runs the tests when executed directly.