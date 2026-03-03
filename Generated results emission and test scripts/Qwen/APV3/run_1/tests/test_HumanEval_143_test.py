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
   - Include from HumanEval_143_code import words_in_sentence
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

user
### Immediate Task
Write the complete unittest test suite for the following Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_143_code import words_in_sentence
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    new_lst = []
    for word in sentence.split():
        flg = 0
        if len(word) == 1:
            flg = 1
        for i in range(2, len(word)):
            if len(word) % i == 0:
                flg = 1
        if flg == 0 or len(word) == 2:
            new_lst.append(word)
    return " ".join(new_lst)


assistant

import unittest

# Importing the function from the provided code snippet
from HumanEval_143_code import words_in_sentence

class TestWordsInSentence(unittest.TestCase):
    
    # Test case for positive examples
    def test_positive_examples(self):
        self.assertEqual(words_in_sentence("This is a test"), "is")
        self.assertEqual(words_in_sentence("lets go for swimming"), "go for")

    # Test case for negative examples (empty input)
    def test_empty_input(self):
        self.assertEqual(words_in_sentence(""), "")

    # Test case for edge cases (single character words)
    def test_single_character_words(self):
        self.assertEqual(words_in_sentence("a"), "")
        self.assertEqual(words_in_sentence("test"), "")

    # Test case for edge cases (two-character words)
    def test_two_character_words(self):
        self.assertEqual(words_in_sentence("aa"), "")
        self.assertEqual(words_in_sentence("ab"), "")

    # Test case for edge cases (three-character words)
    def test_three_character_words(self):
        self.assertEqual(words_in_sentence("abc"), "")
        self.assertEqual(words_in_sentence("aba"), "")

    # Test case for edge cases (four-character words)
    def test_four_character_words(self):
        self.assertEqual(words_in_sentence("abcd"), "")
        self.assertEqual(words_in_sentence("bacd"), "")

    # Test case for edge cases (five-character words)
    def test_five_character_words(self):
        self.assertEqual(words_in_sentence("abcdef"), "")
        self.assertEqual(words_in_sentence("bacdfg"), "")

    # Test case for edge cases (six-character words)
    def test_six_character_words(self):
        self.assertEqual(words_in_sentence("abcdefgh"), "")
        self.assertEqual(words_in_sentence("bacadef"), "")

    # Test case for edge cases (seven-character words)
    def test_seven_character_words(self):
        self.assertEqual(words_in_sentence("ABCDEFGH"), "")
        self.assertEqual(words_in_sentence("BACEDGH"), "")

    # Test case for edge cases (eight-character words)
    def test_eight_character_words(self):
        self.assertEqual(words_in_sentence("ABCDEFGHI"), "")
        self.assertEqual(words_in_sentence("BACEDFGH"), "")

    # Test case for edge cases (nine-character words)
    def test_nine_character_words(self):
        self.assertEqual(words_in_sentence("AEGHIJFKL"), "")
        self.assertEqual(words_in_sentence("BAECDHGFI"), "")

    # Test case for edge cases (ten-character words)
    def test_ten_character_words(self):
        self.assertEqual(words_in_sentence("AFGHIJKLMN"), "")
        self.assertEqual(words_in_sentence("BAEHFGLIJ"), "")

    # Test case for edge cases (eleven-character words)
    def test_eleven_character_words(self):
        self.assertEqual(words_in_sentence("AGHILJKLMNO"), "")
        self.assertEqual(words_in_sentence("BAEKFLMNOI"), "")

    # Test case for edge cases (twelve-character words)
    def test_twelve_character_words(self):
        self.assertEqual(words_in_sentence("AHKLMNOPQRS"), "")
        self.assertEqual(words_in_sentence("BAELNMQORSP"), "")

    # Test case for edge cases (thirteen-character words)
    def test_thirteen_character_words(self):
        self.assertEqual(words_in_sentence("BHLMNOPQRSU"), "")
        self.assertEqual(words_in_sentence("BAENRPSUTWV"), "")

    # Test case for edge cases (fourteen-character words)
    def test_fourteen_character_words(self):
        self.assertEqual(words_in_sentence("CHLMNOPQRST"), "")
        self.assertEqual(words_in_sentence("BAEPRTSUVWX"), "")

    # Test case for edge cases (fifteen-character words)
    def test_fifteen_character_words(self):
        self.assertEqual(words_in_sentence("DHLMNOPQRSTUVWXYZ"), "")
        self.assertEqual(words_in_sentence("BAEQWRTYZUXC"), "")

    # Test case for edge cases (sixteen-character words)
    def test_sixteen_character_words(self):
        self.assertEqual(words_in_sentence("EHLMNOPQRSTUVWXYZ"), "")
        self.assertEqual(words_in_sentence("BAFWXZCYDQ"), "")

    # Test case for edge cases (seventeen-character words)
    def test_seventeen_character_words(self):
        self.assertEqual(words_in_sentence("FHLMNOPQRSTUVWXYZ"), "")
        self.assertEqual(words_in_sentence("BAIXYZWCVDE"), "")

    # Test case for edge cases (eighteen-character words)
    def test_eighteen_character_words(self):
        self.assertEqual(words_in_sentence("GHLMNOPQRSTUVWXYZ"), "")
        self.assertEqual(words_in_sentence("BAJVCXYDTFS"), "")

    # Test case for edge cases (nineteen-character words)
    def test_nineteen_character_words(self):
        self.assertEqual(words_in_sentence("IHLMNOPQRSTUVWXYZ"), "")
        self.assertEqual(words_in_sentence("BAKVLXYDFST"), "")

    # Test case for edge cases (twenty-character words)