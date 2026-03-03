You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_117_code import select_words
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    result = []
    for word in s.split():
        n_consonants = 0
        for i in range(0, len(word)):
            if word[i].lower() not in ["a", "e", "i", "o", "u"]:
                n_consonants += 1
        if n_consonants == n:
            result.append(word)
    return result


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_117_code import select_words

class TestSelectWords(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(select_words("", 4), [])

    def test_no_matching_words(self):
        self.assertEqual(select_words("simple white space", 2), [])

    def test_one_matching_word(self):
        self.assertEqual(select_words("Hello world", 4), ["world"])

    def test_multiple_matching_words(self):
        self.assertEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])

    def test_one_matching_word(self):
        self.assertEqual(select_words("Uncle sam", 3), ["Uncle"])

if __name__ == '__main__':
    unittest.main()


This script includes a test class `TestSelectWords` that inherits from `unittest.TestCase`. Each method in this class is a test case that tests a specific scenario. The `assertEqual` method is used to check if the output of the `select_words` function matches the expected output.

To run the tests, you can simply execute this script. If you are using a command line, you can do so by typing `python test_script.py` (replace `test_script.py` with the name of this script). If you are using an IDE, you can usually run the script by right-clicking on it and selecting "Run".

Note: The function `select_words` is not defined in this script. You should define it in a separate file named `HumanEval_117_code.py` for the tests to work.