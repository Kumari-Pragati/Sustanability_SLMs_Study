You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function `select_words`. The test cases cover various scenarios including empty string, single-word strings, strings with multiple words, and strings with words containing different numbers of consonants.


import unittest
from HumanEval_117_code import select_words

class TestSelectWords(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(select_words("", 4), [])

    def test_single_word(self):
        self.assertEqual(select_words("Mary", 3), [])
        self.assertEqual(select_words("lamb", 4), [])
        self.assertEqual(select_words("Hello", 4), [])
        self.assertEqual(select_words("world", 4), [])
        self.assertEqual(select_words("Uncle", 3), [])
        self.assertEqual(select_words("sam", 3), [])

    def test_multiple_words(self):
        self.assertEqual(select_words("Mary had a little lamb", 4), ["little"])
        self.assertEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])
        self.assertEqual(select_words("simple white space", 2), [])
        self.assertEqual(select_words("Hello world", 4), ["world"])
        self.assertEqual(select_words("Uncle sam", 3), ["Uncle"])

if __name__ == '__main__':
    unittest.main()


This test suite uses the built-in `unittest` module to create a test case class `TestSelectWords`. Inside this class, there are several test methods that cover different scenarios. The `assertEqual` method is used to compare the expected output with the actual output produced by the `select_words` function.