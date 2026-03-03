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

from HumanEval_143_code import words_in_sentence

class TestWordsInSentence(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(words_in_sentence("This is a test"), "is")

    def test_edge_case(self):
        self.assertEqual(words_in_sentence("lets go for swimming"), "for")

    def test_empty_string(self):
        self.assertEqual(words_in_sentence(""), "")

    def test_single_word(self):
        self.assertEqual(words_in_sentence("a"), "a")

    def test_multiple_words(self):
        self.assertEqual(words_in_sentence("one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred"), "twenty thirty forty fifty sixty seventy eighty ninety hundred")

    def test_large_number(self):
        self.assertEqual(words_in_sentence("The quick brown fox jumps over the lazy dog"), "quick brown fox jumps over the lazy dog")

    def test_special_characters(self):
        self.assertEqual(words_in_sentence("Hello World!"), "World!")

    def test_all_caps(self):
        self.assertEqual(words_in_sentence("HELLO WORLD!"), "WORLD!")

    def test_mixed_case(self):
        self.assertEqual(words_in_sentence("hello world!"), "world!")

    def test_whitespace(self):
        self.assertEqual(words_in_sentence(" "), "")


If `words_in_sentence` is defined correctly, this test suite will cover various cases including empty strings, single words, multi-word sentences, large numbers, special characters, mixed case, and whitespace.