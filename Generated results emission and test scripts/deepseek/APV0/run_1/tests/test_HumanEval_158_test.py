You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_158_code import find_max
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    Examples:
    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    """
    return sorted(words, key=lambda x: (-len(set(x)), x))[0]


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_158_code import find_max

class TestFindMax(unittest.TestCase):

    def test_find_max(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")
        self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")
        self.assertEqual(find_max(["apple", "banana", "cherry"]), "banana")
        self.assertEqual(find_max(["abc", "def", "ghi"]), "abc")
        self.assertEqual(find_max(["123", "456", "789"]), "123")
        self.assertEqual(find_max(["aaa", "bbb", "ccc"]), "aaa")
        self.assertEqual(find_max(["aaaa", "bbbb", "cccc"]), "aaaa")
        self.assertEqual(find_max(["aaaaa", "bbbbb", "ccccc"]), "aaaaa")
        self.assertEqual(find_max(["aaaaaa", "bbbbbb", "cccccc"]), "aaaaaa")

if __name__ == '__main__':
    unittest.main()


This script includes a test case for the `find_max` function with different inputs. The `assertEqual` method is used to check if the output of the function matches the expected output. If the function's output does not match the expected output, the test case will fail.

Please note that the function `find_max` is expected to be in a file named `HumanEval_158_code.py` in the same directory as the test script. If the function is in a different file, you will need to import it accordingly.

To run the test script, you can simply execute it in a Python environment. The `unittest` module will automatically run all the test cases in the `TestFindMax` class. If all the test cases pass, the script will exit without any output. If any test case fails, the script will output a message indicating which test case failed and why.