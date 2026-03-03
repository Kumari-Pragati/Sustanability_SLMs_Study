You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_98_code import count_upper

class TestCountUpper(unittest.TestCase):
    def test_count_upper(self):
        self.assertEqual(count_upper('aBCdEf'), 1)
        self.assertEqual(count_upper('abcdefg'), 0)
        self.assertEqual(count_upper('dBBE'), 0)
        self.assertEqual(count_upper('AaBbCc'), 1)
        self.assertEqual(count_upper('dEfGhI'), 1)
        self.assertEqual(count_upper('JkLmNoP'), 0)
        self.assertEqual(count_upper('QrStUvWx'), 0)
        self.assertEqual(count_upper('Yz'), 0)
        self.assertEqual(count_upper(''), 0)
        self.assertEqual(count_upper('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 5)

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases, including both upper and lower case letters, and letters at even and odd indices. It also tests the function with an empty string and a string of all uppercase letters.