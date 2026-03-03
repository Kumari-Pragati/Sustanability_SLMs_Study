user

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
    return ""assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_118_code import get_closest_vowel

class TestGetClosestVowel(unittest.TestCase):

    def test_get_closest_vowel(self):
        self.assertEqual(get_closest_vowel("yogurt"), "u")
        self.assertEqual(get_closest_vowel("FULL"), "U")
        self.assertEqual(get_closest_vowel("quick"), "")
        self.assertEqual(get_closest_vowel("ab"), "")
        self.assertEqual(get_closest_vowel("aeiou"), "")
        self.assertEqual(get_closest_vowel("bcdf"), "")
        self.assertEqual(get_closest_vowel("xyz"), "")
        self.assertEqual(get_closest_vowel("a"), "")
        self.assertEqual(get_closest_vowel("z"), "")
        self.assertEqual(get_closest_vowel(""), "")
        self.assertEqual(get_closest_vowel("aabbcc"), "")
        self.assertEqual(get_closest_vowel("bcdfgh"), "")
        self.assertEqual(get_closest_vowel("ijklmn"), "")
        self.assertEqual(get_closest_vowel("opqrstu"), "")
        self.assertEqual(get_closest_vowel("vwxyz"), "")

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure the function is working correctly. It tests the function with different inputs, including words with vowels, words without vowels, and words with only one or two letters. The expected output for each test case is specified using the `assertEqual` method.