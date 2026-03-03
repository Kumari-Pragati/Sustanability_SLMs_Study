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
   - Include from HumanEval_86_code import anti_shuffle
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
2. Include: from HumanEval_86_code import anti_shuffle
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string is a string where all words (separated by space)
    are replaced by a new word where all the characters are arranged in
    ascending order based on ASCII value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """

    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])


assistant

import unittest

from HumanEval_86_code import anti_shuffle

class TestAntiShuffle(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(anti_shuffle('Hi'), 'Hi')
    
    def test_negative_numbers(self):
        self.assertEqual(anti_shuffle('hello'), 'ehllo')
    
    def test_empty_string(self):
        self.assertEqual(anti_shuffle(""), "")
    
    def test_single_word(self):
        self.assertEqual(anti_shuffle("World"), "dWlr")
    
    def test_multiple_words(self):
        self.assertEqual(anti_shuffle("Hello World!!!"), "Hello !!!Wdlor")
    
    def test_mixed_case(self):
        self.assertEqual(anti_shuffle("This Is A Test!"), "hsiht !siA tset!")
    
    def test_special_characters(self):
        self.assertEqual(anti_shuffle("Special $%^&*()"), "$%^&*()seltS")

if __name__ == '__main__':
    unittest.main()