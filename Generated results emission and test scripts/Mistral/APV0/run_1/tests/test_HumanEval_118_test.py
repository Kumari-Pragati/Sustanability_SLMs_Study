Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `get_closest_vowel` function:


import unittest
from HumanEval_118_code import get_closest_vowel

class TestGetClosestVowel(unittest.TestCase):

    def test_get_closest_vowel(self):
        self.assertEqual(get_closest_vowel("yogurt"), "u")
        self.assertEqual(get_closest_vowel("FULL"), "U")
        self.assertEqual(get_closest_vowel("quick"), "")
        self.assertEqual(get_closest_vowel("ab"), "")
        self.assertEqual(get_closest_vowel("example"), "a")
        self.assertEqual(get_closest_vowel("Hello"), "")
        self.assertEqual(get_closest_vowel("aeiou"), "")
        self.assertEqual(get_closest_vowel("AEIOU"), "")
        self.assertEqual(get_closest_vowel("123"), "")
        self.assertEqual(get_closest_vowel("consonant"), "")
        self.assertEqual(get_closest_vowel("vowel"), "")
        self.assertEqual(get_closest_vowel("vowel1"), "")
        self.assertEqual(get_closest_vowel("vowel1a"), "a")
        self.assertEqual(get_closest_vowel("vowel1a1"), "")
        self.assertEqual(get_closest_vowel("vowel1a1b"), "")
        self.assertEqual(get_closest_vowel("vowel1a1b1"), "")
        self.assertEqual(get_closest_vowel("vowel1a1b1c"), "")
        self.assertEqual(get_closest_vowel("vowel1a1b1c1"), "")
        self.assertEqual(get_closest_vowel("vowel1a1b1c1d"), "a")
        self.assertEqual(get_closest_vowel("vowel1a1b1c1d1"), "")
        self.assertEqual(get_closest_vowel("vowel1a1b1c1d1e"), "e")

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases to ensure the function works correctly for different inputs. It covers the edge cases, such as words with only consonants, words with only vowels, words with a single vowel, and words with multiple vowels. It also checks the case sensitivity of the function.