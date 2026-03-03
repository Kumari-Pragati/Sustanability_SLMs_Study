You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_112_code import reverse_delete
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def reverse_delete(s, c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd', False)
    For s = "abcdef", c = "b"  the result should be ('acdef', False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc', True)
    """

    s = ''.join([char for char in s if char not in c])
    return (s, s[::-1] == s)


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_112_code import reverse_delete

class TestReverseDelete(unittest.TestCase):
    def test_reverse_delete(self):
        self.assertEqual(reverse_delete("abcde", "ae"), ('bcd', False))
        self.assertEqual(reverse_delete("abcdef", "b"), ('acdef', False))
        self.assertEqual(reverse_delete("abcdedcba", "ab"), ('cdedc', True))
        self.assertEqual(reverse_delete("aabbcc", "abc"), ('', True))
        self.assertEqual(reverse_delete("abc", "abc"), ('', True))
        self.assertEqual(reverse_delete("abc", ""), ('abc', True))
        self.assertEqual(reverse_delete("", "abc"), ('', True))

if __name__ == '__main__':
    unittest.main()


This script creates a test class `TestReverseDelete` that inherits from `unittest.TestCase`. Inside this class, there is a method `test_reverse_delete` that tests the `reverse_delete` function with various inputs and expected outputs.

The `assertEqual` method is used to check if the actual output of the function matches the expected output. If the actual output does not match the expected output, the test will fail.

The script ends with `unittest.main()`, which runs the test when the script is executed.

Please note that you need to have the `HumanEval_112_code` module with the `reverse_delete` function defined in it for this script to work.