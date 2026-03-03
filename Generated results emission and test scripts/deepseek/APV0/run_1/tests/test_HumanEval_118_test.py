You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_118_code import get_closest_vowel

class TestGetClosestVowel(unittest.TestCase):
    def test_get_closest_vowel(self):
        self.assertEqual(get_closest_vowel("yogurt"), "u")
        self.assertEqual(get_closest_vowel("FULL"), "U")
        self.assertEqual(get_closest_vowel("quick"), "")
        self.assertEqual(get_closest_vowel("ab"), "")
        self.assertEqual(get_closest_vowel(""), "")
        self.assertEqual(get_closest_vowel("a"), "")
        self.assertEqual(get_closest_vowel("b"), "")
        self.assertEqual(get_closest_vowel("ba"), "")
        self.assertEqual(get_closest_vowel("bba"), "")
        self.assertEqual(get_closest_vowel("bbba"), "b")
        self.assertEqual(get_closest_vowel("bbbb"), "")
        self.assertEqual(get_closest_vowel("bbaa"), "a")
        self.assertEqual(get_closest_vowel("bbbaa"), "a")
        self.assertEqual(get_closest_vowel("bbbaab"), "a")
        self.assertEqual(get_closest_vowel("bbbaabb"), "b")
        self.assertEqual(get_closest_vowel("bbbaabbb"), "")

if __name__ == '__main__':
    unittest.main()


This script includes a test class `TestGetClosestVowel` that inherits from `unittest.TestCase`. Inside this class, there is a method `test_get_closest_vowel` that tests the `get_closest_vowel` function with a variety of inputs. Each test case uses the `assertEqual` method to check that the output of `get_closest_vowel` matches the expected output.

The `if __name__ == '__main__': unittest.main()` line at the end of the script runs the tests when the script is run directly.

Please note that you need to have the `HumanEval_118_code` module with the `get_closest_vowel` function defined in it to run this test script.