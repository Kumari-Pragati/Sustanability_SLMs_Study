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

user
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


assistant

import unittest

# Importing the function we want to test
from HumanEval_91_code import is_bored

class TestIsBored(unittest.TestCase):
    
    # Test case for positive numbers
    def test_positive_numbers(self):
        self.assertEqual(is_bored("Hello world"), 0)
        
    # Test case for negative numbers
    def test_negative_numbers(self):
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)
        
    # Test case for empty list
    def test_empty_list(self):
        self.assertEqual(is_bored(""), 0)
        
    # Test case for mixed sentences
    def test_mixed_sentences(self):
        self.assertEqual(is_bored("I am happy. What about you? I hope it's nice outside."), 1)
        
    # Test case for complex sentences
    def test_complex_sentences(self):
        self.assertEqual(is_bored("I'm feeling bored today. Maybe I should go out and do something fun."),
                         1)
        
    # Test case for punctuation at the end of sentences
    def test_punctuation_at_end(self):
        self.assertEqual(is_bored("I'm so bored! Really?"),
                         1)
        
    # Test case for no 'I' in the sentence
    def test_no_I_in_sentence(self):
        self.assertEqual(is_bored("This is boring."),
                         0)
        
    # Test case for multiple 'I' in the sentence
    def test_multiple_I_in_sentence(self):
        self.assertEqual(is_bored("I am I am very bored."),
                         1)
        
    # Test case for long sentences
    def test_long_sentences(self):
        self.assertEqual(is_bored("I have been waiting for this moment since yesterday. It's finally here."),
                         1)
        
    # Test case for short sentences
    def test_short_sentences(self):
        self.assertEqual(is_bored("I'm bored."),
                         1)
        
    # Test case for sentences starting with other than 'I'
    def test_other_than_I(self):
        self.assertEqual(is_bored("What a great day!"),
                         0)
        
    # Test case for sentences ending with punctuation but not 'I'
    def test_sentences_with_punctuation_not_I(self):
        self.assertEqual(is_bored("I'm bored! Really?"),
                         1)
        
    # Test case for sentences containing multiple spaces before 'I'
    def test_multiple_spaces_before_I(self):
        self.assertEqual(is_bored("I  am  bored."),
                         1)
        
    # Test case for sentences containing multiple spaces after 'I'
    def test_multiple_spaces_after_I(self):
        self.assertEqual(is_bored("I am bored "),
                         1)
        
    # Test case for sentences containing multiple spaces around 'I'
    def test_multiple_spaces_around_I(self):
        self.assertEqual(is_bored("I am bored too."),
                         1)
        
    # Test case for sentences containing multiple spaces inside 'I'
    def test_multiple_spaces_inside_I(self):
        self.assertEqual(is_bored("I am bored too I"),
                         1)
        
    # Test case for sentences containing multiple spaces between 'I' and 'bored'
    def test_multiple_spaces_between_I_and_bored(self):
        self.assertEqual(is_bored("I am bored too I am bored too"),
                         1)
        
    # Test case for sentences containing multiple spaces around 'bored'
    def test_multiple_spaces_around_bored(self):
        self.assertEqual(is_bored("I am bored too I am bored too I"),
                         1)
        
    # Test case for sentences containing multiple spaces inside 'bored'
    def test_multiple_spaces_inside_bored(self):
        self.assertEqual(is_bored("I am bored too I am bored too I am bored too"),
                         1)
        
    # Test case for sentences containing multiple spaces between 'bored' and 'too'
    def test_multiple_spaces_between_bored_and_too(self):
        self.assertEqual(is_bored("I am bored too I am bored too I am bored too I am bored too"),
                         1)
        
    # Test case for sentences containing multiple spaces around 'too'
    def test_multiple_spaces_around_too(self):
        self.assertEqual(is_bored("I am bored too I am bored too I am bored too I am bored too I am bored too"),
                         1)
        
    # Test case for sentences containing multiple spaces inside 'too'
    def test_multiple_spaces_inside_too(self):
        self.assertEqual(is_bored("I am bored too I am bored too I am bored too I am bored too I am bored too I am bored too"),
                         1)
        
    # Test case for sentences containing multiple spaces between 'too' and 'I'
    def test_multiple_spaces_between_too_and_I(self):
        self.assertEqual(is_bored("I am bored too I am bored too I am bored too