You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_86_code import anti_shuffle
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string is a string where all words (separated by space)
    are replaced by a new word where all the characters are arranged in
    ascending order based on ASCII value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """

    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_86_code import anti_shuffle

class TestAntiShuffle(unittest.TestCase):

    def test_anti_shuffle(self):
        self.assertEqual(anti_shuffle('Hi'), 'Hi')
        self.assertEqual(anti_shuffle('hello'), 'ehllo')
        self.assertEqual(anti_shuffle('Hello World!!!'), 'Hello !!!Wdlor')
        self.assertEqual(anti_shuffle(''), '')
        self.assertEqual(anti_shuffle('a b c d e'), 'abcde')
        self.assertEqual(anti_shuffle('123 456 789'), '123 456 789')
        self.assertEqual(anti_shuffle('abc def ghi'), 'abcdefghi')
        self.assertEqual(anti_shuffle('The quick brown fox jumps over the lazy dog'), 
                         'Tbe ehikmors wbcd xf pu ojrv lzat ehdg')

if __name__ == '__main__':
    unittest.main()


This script creates a new class `TestAntiShuffle` that inherits from `unittest.TestCase`. Inside this class, a method `test_anti_shuffle` is defined, which contains a series of `assertEqual` calls to test the `anti_shuffle` function with different inputs.

The `assertEqual` method is used to check if the output of the `anti_shuffle` function matches the expected output. If the output does not match the expected output, the test will fail.

Finally, the script ends with `if __name__ == '__main__': unittest.main()`, which means that the tests will be run when the script is executed directly.

Please note that the `HumanEval_86_code` module should contain the `anti_shuffle` function for the tests to pass.