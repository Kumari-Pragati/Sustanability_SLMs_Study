You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
Here is a complete unittest test suite for the given function:


import unittest
from HumanEval_117_code import select_words

class TestSelectWords(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(select_words("", 0), [])

    def test_no_consonants(self):
        self.assertEqual(select_words("aeiou", 0), [])

    def test_one_consonant(self):
        self.assertEqual(select_words("b", 1), ["b"])

    def test_multiple_consonants(self):
        self.assertEqual(select_words("bcd", 3), ["bcd"])

    def test_multiple_words(self):
        self.assertEqual(select_words("b c d", 1), ["b", "c", "d"])

    def test_case_insensitive(self):
        self.assertEqual(select_words("B c d", 1), ["b", "c", "d"])

    def test_consonants_in_middle(self):
        self.assertEqual(select_words("a b c d e", 2), ["b", "d"])

    def test_consonants_at_ends(self):
        self.assertEqual(select_words("a b c d e", 3), ["b", "c", "d"])

    def test_consonants_at_ends_and_middle(self):
        self.assertEqual(select_words("a b c d e", 4), ["b", "c", "d", "e"])

    def test_consonants_not_enough(self):
        self.assertEqual(select_words("a b c d e", 5), [])

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure that the function is working correctly. It tests with empty strings, strings with no consonants, strings with one consonant, strings with multiple consonants, and strings with consonants at the ends and in the middle. It also tests with different cases (upper and lower) to ensure that the function is case insensitive.