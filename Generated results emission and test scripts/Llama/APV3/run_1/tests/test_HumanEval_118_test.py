system

### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_118_code import get_closest_vowel
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()user

### Immediate Task
Write the complete unittest test suite for the following Python function.

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

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_118_code import get_closest_vowel

class TestGetClosestVowel(unittest.TestCase):
    def test_yogurt(self):
        self.assertEqual(get_closest_vowel("yogurt"), "u")

    def test_full(self):
        self.assertEqual(get_closest_vowel("FULL"), "U")

    def test_quick(self):
        self.assertEqual(get_closest_vowel("quick"), "")

    def test_ab(self):
        self.assertEqual(get_closest_vowel("ab"), "")

    def test_vowel_at_start(self):
        self.assertEqual(get_closest_vowel("a"), "")

    def test_vowel_at_end(self):
        self.assertEqual(get_closest_vowel("helloa"), "")

    def test_no_vowel(self):
        self.assertEqual(get_closest_vowel("bcdfghjklmnpqrstvwxyz"), "")

    def test_multiple_vowels(self):
        self.assertEqual(get_closest_vowel("aeiou"), "")

    def test_vowel_between_consonants(self):
        self.assertEqual(get_closest_vowel("bcudef"), "u")

    def test_vowel_between_consonants_at_end(self):
        self.assertEqual(get_closest_vowel("bcdefu"), "u")

if __name__ == '__main__':
    unittest.main()