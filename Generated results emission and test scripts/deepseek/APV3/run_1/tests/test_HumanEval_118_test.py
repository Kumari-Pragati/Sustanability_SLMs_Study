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
    unittest.main()
### Instruction:
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
    return ""


### Response:
import unittest
from HumanEval_118_code import get_closest_vowel

class TestGetClosestVowel(unittest.TestCase):
    def test_single_vowel(self):
        self.assertEqual(get_closest_vowel("yogurt"), "u")
        self.assertEqual(get_closest_vowel("FULL"), "U")
        self.assertEqual(get_closest_vowel("quick"), "")
        self.assertEqual(get_closest_vowel("ab"), "")
        self.assertEqual(get_closest_vowel("a"), "")
        self.assertEqual(get_closest_vowel("A"), "")
        self.assertEqual(get_closest_vowel("i"), "")
        self.assertEqual(get_closest_vowel("I"), "")
        self.assertEqual(get_closest_vowel("o"), "")
        self.assertEqual(get_closest_vowel("O"), "")
        self.assertEqual(get_closest_vowel("u"), "")
        self.assertEqual(get_closest_vowel("U"), "")

    def test_no_vowel(self):
        self.assertEqual(get_closest_vowel("bcd"), "")
        self.assertEqual(get_closest_vowel("cdf"), "")
        self.assertEqual(get_closest_vowel("def"), "")

    def test_multiple_vowels(self):
        self.assertEqual(get_closest_vowel("bgeh"), "e")
        self.assertEqual(get_closest_vowel("bgei"), "e")
        self.assertEqual(get_closest_vowel("bgeo"), "e")
        self.assertEqual(get_closest_vowel("bgeu"), "e")
        self.assertEqual(get_closest_vowel("bgeA"), "e")
        self.assertEqual(get_closest_vowel("bgeE"), "e")
        self.assertEqual(get_closest_vowel("bgeI"), "e")
        self.assertEqual(get_closest_vowel("bgeO"), "e")
        self.assertEqual(get_closest_vowel("bgeU"), "e")

if __name__ == '__main__':
    unittest.main()