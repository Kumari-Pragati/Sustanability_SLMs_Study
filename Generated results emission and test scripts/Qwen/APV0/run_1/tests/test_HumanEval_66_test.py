system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_66_code import digitSum
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    if s == "":
        return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)


assistant

import unittest

# Function to be tested
from HumanEval_66_code import digitSum

class TestDigitSum(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(digitSum(""), 0)

    def test_uppercase_only(self):
        self.assertEqual(digitSum("abAB"), 131)
    
    def test_mixed_case(self):
        self.assertEqual(digitSum("abcCd"), 67)
    
    def test_lowercase_only(self):
        self.assertEqual(digitSum("helloE"), 69)
    
    def test_all_lower(self):
        self.assertEqual(digitSum("woArBld"), 131)
    
    def test_all_upper(self):
        self.assertEqual(digitSum("aAaaaXa"), 153)

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines a class `TestDigitSum` that inherits from `unittest.TestCase`. Each method within this class is a test case that uses assertions to verify the correctness of the `digitSum` function. The tests cover various scenarios including empty strings, uppercase-only strings, mixed-case strings, lowercase-only strings, all-lowercase strings, and all-uppercase strings. If you run this script, it will execute all the defined test cases and report whether each one passes or fails.