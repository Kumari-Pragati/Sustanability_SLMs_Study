You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_98_code import count_upper

class TestCountUpper(unittest.TestCase):
    def test_count_upper(self):
        self.assertEqual(count_upper('aBCdEf'), 1)
        self.assertEqual(count_upper('abcdefg'), 0)
        self.assertEqual(count_upper('dBBE'), 0)
        self.assertEqual(count_upper('AaBbCc'), 1)
        self.assertEqual(count_upper('dEfGHi'), 1)
        self.assertEqual(count_upper(''), 0)
        self.assertEqual(count_upper('ABCDE'), 2)
        self.assertEqual(count_upper('abcde'), 0)
        self.assertEqual(count_upper('ABCDEabcde'), 2)
        self.assertEqual(count_upper('123456'), 0)
        self.assertEqual(count_upper('A1B2C3D4E5'), 2)

if __name__ == '__main__':
    unittest.main()


This script includes a test class `TestCountUpper` that inherits from `unittest.TestCase`. Inside this class, there is a method `test_count_upper` that tests the `count_upper` function with various inputs. Each `self.assertEqual` call checks if the output of `count_upper` is as expected for a given input.

The script ends with `unittest.main()`, which runs the tests when the script is run directly.

Please note that you need to have the `HumanEval_98_code` module with the `count_upper` function defined in it for this script to work.