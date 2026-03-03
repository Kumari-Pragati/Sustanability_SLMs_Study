You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_118_code import get_closest_vowel

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    if len(word) < 3:
        return ""

    vowels = {"a", "e", "i", "o", "u", "A", "E", "O", "U", "I"}
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            if (word[i + 1] not in vowels) and (word[i - 1] not in vowels):
                return word[i]
    return ""

 Here is a comprehensive unittest test suite for the given Python function `get_closest_vowel`.


import unittest
from HumanEval_118_code import get_closest_vowel

class TestGetClosestVowel(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(get_closest_vowel(""), "")
        self.assertEqual(get_closest_vowel(" "), "")

    def test_single_consonant(self):
        self.assertEqual(get_closest_vowel("a"), "")
        self.assertEqual(get_closest_vowel("b"), "")
        self.assertEqual(get_closest_vowel("c"), "")
        self.assertEqual(get_closest_vowel("d"), "")
        self.assertEqual(get_closest_vowel("e"), "")
        self.assertEqual(get_closest_vowel("f"), "")
        self.assertEqual(get_closest_vowel("g"), "")
        self.assertEqual(get_closest_vowel("h"), "")
        self.assertEqual(get_closest_vowel("j"), "")
        self.assertEqual(get_closest_vowel("k"), "")
        self.assertEqual(get_closest_vowel("l"), "")
        self.assertEqual(get_closest_vowel("m"), "")
        self.assertEqual(get_closest_vowel("n"), "")
        self.assertEqual(get_closest_vowel("o"), "")
        self.assertEqual(get_closest_vowel("p"), "")
        self.assertEqual(get_closest_vowel("q"), "")
        self.assertEqual(get_closest_vowel("r"), "")
        self.assertEqual(get_closest_vowel("s"), "")
        self.assertEqual(get_closest_vowel("t"), "")
        self.assertEqual(get_closest_vowel("u"), "")
        self.assertEqual(get_closest_vowel("v"), "")
        self.assertEqual(get_closest_vowel("w"), "")
        self.assertEqual(get_closest_vowel("x"), "")
        self.assertEqual(get_closest_vowel("y"), "")
        self.assertEqual(get_closest_vowel("z"), "")

    def test_single_vowel(self):
        self.assertEqual(get_closest_vowel("a"), "")
        self.assertEqual(get_closest_vowel("e"), "")
        self.assertEqual(get_closest_vowel("i"), "")
        self.assertEqual(get_closest_vowel("o"), "")
        self.assertEqual(get_closest_vowel("u"), "")
        self.assertEqual(get_closest_vowel("A"), "")
        self.assertEqual(get_closest_vowel("E"), "")
        self.assertEqual(get_closest_vowel("I"), "")
        self.assertEqual(get_closest_vowel("O"), "")
        self.assertEqual(get_closest_vowel("U"), "")

    def test_vowel_at_beginning(self):
        self.assertEqual(get_closest_vowel("ae"), "")
        self.assertEqual(get_closest_vowel("ei"), "")
        self.assertEqual(get_closest_vowel("io"), "")
        self.assertEqual(get_closest_vowel("ou"), "")
        self.assertEqual(get_closest_vowel("ui"), "")
        self.assertEqual(get_closest_vowel("Ae"), "")
        self.assertEqual(get_closest_vowel("Ei"), "")
        self.assertEqual(get_closest_vowel("Io"), "")
        self.assertEqual(get_closest_vowel("Ou"), "")
        self.assertEqual(get_closest_vowel("Ui"), "")

    def test_vowel_at_end(self):
        self.assertEqual(get_closest_vowel("abc"), "")
        self.assertEqual(get_closest_vowel("def