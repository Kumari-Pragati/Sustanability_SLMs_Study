system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_18_code import how_many_times
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def how_many_times(string: str, substring: str) -> int:
    """Find how many times a given substring can be found in the original string. Count overlapping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    times = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            times += 1
    return times


assistant

import unittest

# Function to be tested
from HumanEval_18_code import how_many_times

class TestHowManyTimes(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)
        
    def test_single_char_substring(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)
        
    def test_multiple_occurrences(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines a class `TestHowManyTimes` that inherits from `unittest.TestCase`. It contains three test methods (`test_empty_string`, `test_single_char_substring`, and `test_multiple_occurrences`) that use assertions to verify the correctness of the `how_many_times` function against provided data points. The `if __name__ == '__main__':` block ensures that when this script is run as the main program, it will execute all tests defined within the `TestHowManyTimes` class.