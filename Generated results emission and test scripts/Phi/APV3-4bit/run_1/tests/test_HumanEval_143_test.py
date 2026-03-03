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

 import unittest
from HumanEval_143_code import words_in_sentence

class TestWordsInSentence(unittest.TestCase):

    def test_single_word_prime_length(self):
        sentence = "is"
        result = words_in_sentence(sentence)
        self.assertEqual(result, sentence)

    def test_multiple_words_prime_length(self):
        sentence = "go for"
        result = words_in_sentence(sentence)
        self.assertEqual(result, "go for")

    def test_empty_sentence(self):
        sentence = ""
        result = words_in_sentence(sentence)
        self.assertEqual(result, "")

    def test_single_word_not_prime_length(self):
        sentence = "test"
        result = words_in_sentence(sentence)
        self.assertEqual(result, "")

    def test_multiple_words_not_prime_length(self):
        sentence = "lets go for swimming"
        result = words_in_sentence(sentence)
        self.assertEqual(result, "go for")

    def test_single_word_prime_length_with_space(self):
        sentence = "is "
        result = words_in_sentence(sentence)
        self.assertEqual(result, "is ")

    def test_multiple_words_prime_length_with_space(self):
        sentence = "go for "
        result = words_in_sentence(sentence)
        self.assertEqual(result, "go for ")

    def test_single_word_not_prime_length_with_space(self):
        sentence = "test "
        result = words_in_sentence(sentence)
        self.assertEqual(result, "")

    def test_multiple_words_not_prime_length_with_space(self):
0
        sentence = "lets go for swimming "
        result = words_in_sentence(sentence)
        self.assertEqual(result, "go for ")

if __name__ == '__main__':
    unittest.main()