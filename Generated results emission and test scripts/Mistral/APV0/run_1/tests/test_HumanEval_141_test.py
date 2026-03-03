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

 Here is a unittest test script for the `file_name_check` function:


import unittest
from HumanEval_141_code import file_name_check

class TestFileNameCheck(unittest.TestCase):
    def test_valid_file_name(self):
        self.assertEqual(file_name_check("example.txt"), "Yes")
        self.assertEqual(file_name_check("Report.txt"), "Yes")
        self.assertEqual(file_name_check("My_Document.dll"), "Yes")

    def test_invalid_file_name(self):
        self.assertEqual(file_name_check("1example.txt"), "No")
        self.assertEqual(file_name_check("example1.txt"), "No")
        self.assertEqual(file_name_check("example.dll1"), "No")
        self.assertEqual(file_name_check("example.exe.txt"), "No")
        self.assertEqual(file_name_check("example.txt.txt"), "No")
        self.assertEqual(file_name_check("example.txt.dll"), "No")
        self.assertEqual(file_name_check("example.txt.123"), "No")
        self.assertEqual(file_name_check("example.txt.aBc"), "No")
        self.assertEqual(file_name_check("example.exe"), "No")
        self.assertEqual(file_name_check("example.dll"), "No")

if __name__ == '__main__':
    unittest.main()


This test script includes two test cases: `test_valid_file_name` and `test_invalid_file_name`. The first one tests valid file names, and the second one tests invalid file names according to the given conditions. You can run this script directly to test the `file_name_check` function.