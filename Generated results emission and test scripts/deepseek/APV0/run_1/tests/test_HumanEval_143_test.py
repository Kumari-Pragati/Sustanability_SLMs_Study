You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_143_code import words_in_sentence

class TestWordsInSentence(unittest.TestCase):
    def test_words_in_sentence(self):
        self.assertEqual(words_in_sentence("This is a test"), "is")
        self.assertEqual(words_in_sentence("lets go for swimming"), "go for")
        self.assertEqual(words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z"), "a b c d e f g h i j k l m n o p q r s t u v w x y z")
        self.assertEqual(words_in_sentence("prime number test"), "prime number")
        self.assertEqual(words_in_sentence("one two three four five six seven eight nine ten"), "one two three four five six seven eight nine")
        self.assertEqual(words_in_sentence("one"), "one")
        self.assertEqual(words_in_sentence("two"), "")
        self.assertEqual(words_in_sentence("three"), "three")
        self.assertEqual(words_in_sentence("four"), "")
        self.assertEqual(words_in_sentence("five"), "five")
        self.assertEqual(words_in_sentence("six"), "")
        self.assertEqual(words_in_sentence("seven"), "seven")
        self.assertEqual(words_in_sentence("eight"), "")
        self.assertEqual(words_in_sentence("nine"), "nine")
        self.assertEqual(words_in_sentence("ten"), "")

if __name__ == '__main__':
    unittest.main()


This script includes a test class `TestWordsInSentence` that inherits from `unittest.TestCase`. Inside this class, there is a method `test_words_in_sentence` that tests the `words_in_sentence` function with a variety of inputs. Each test case checks if the output of the function matches the expected output.

The `unittest.main()` at the end of the script runs all the test cases when the script is run directly.

Please note that the function `words_in_sentence` is not provided in the question. You need to have the function in a file named `HumanEval_143_code.py` in the same directory as this unittest script for it to work.