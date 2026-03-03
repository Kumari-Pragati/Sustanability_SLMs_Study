system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_98_code import count_upper
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    Examples:
    count_upper('aBCdEf') ➞ 1
    count_upper('abcdefg') ➞ 0
    count_upper('dBBE') ➞ 0
    """

    count = 0
    for i in range(0, len(s), 2):
        if s[i] in "AEIOU":
            count += 1
    return count


assistant

import unittest

# Function to be tested
from HumanEval_98_code import count_upper

class TestCountUpper(unittest.TestCase):

    def test_count_upper(self):
        self.assertEqual(count_upper('aBCdEf'), 1)
        self.assertEqual(count_upper('abcdefg'), 0)
        self.assertEqual(count_upper('dBBE'), 0)

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and `count_upper` from the provided code file. It then defines a class `TestCountUpper` that inherits from `unittest.TestCase`. Within this class, there is a method `test_count_upper` which contains assertions to check the correctness of the `count_upper` function using predefined data points. Finally, it calls `unittest.main()` to run all tests.