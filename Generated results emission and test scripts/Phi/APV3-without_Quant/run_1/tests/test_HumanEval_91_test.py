### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_91_code import is_bored
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
2. Include: from HumanEval_91_code import is_bored
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """

    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence.startswith('I ') for sentence in sentences if sentence)

 import unittest
from HumanEval_91_code import is_bored

class TestIsBored(unittest.TestCase):
    def test_no_boredoms(self):
        self.assertEqual(is_bored("Hello world"), 0)

    def test_single_boredom(self):
        self.assertEqual(is_bored("The sky is blue. I love the stars!"), 1)

    def test_multiple_boredom(self):
        self.assertEqual(is_bored("The sky is blue. I love the stars! I am bored. I wish I could sleep."), 3)

    def test_no_sentences(self):
        self.assertEqual(is_bored(""), 0)

    def test_empty_sentence(self):
        self.assertEqual(is_bored("I."), 1)

    def test_sentence_with_multiple_I(self):
        self.assertEqual(is_bored("I am happy. I am excited. I am bored."), 3)

    def test_sentence_with_no_I(self):
        self.assertEqual(is_bored("The cat is on the mat."), 0)

    def test_sentence_with_I_at_end(self):
        self.assertEqual(is_bored("I am tired."), 1)

    def test_sentence_with_I_in_middle(self):
        self.assertEqual(is_bored("I am a student. I study hard."), 2)

    def test_sentence_with_I_at_beginning_and_end(self):
        self.assertEqual(is_bored("I am a student. I study hard. I am a good student."), 3)

    def test_sentence_with_I_in_middle_and_end(self):
        self.assertEqual(is_bored("I am a student. I study hard. I am a good student. I am tired."), 4)

    def test_sentence_with_I_in_middle_and_beginning(self):
        self.assertEqual(is_bored("I am a student. I study hard. I am a good student. I am tired. I am happy."), 5)

if __name__ == '__main__':
    unittest.main()