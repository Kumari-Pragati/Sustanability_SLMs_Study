system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Test case class
class TestWordsInSentence(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(words_in_sentence("This is a test"), "is")

    def test_example_2(self):
        self.assertEqual(words_in_sentence("lets go for swimming"), "go for")

    def test_empty_string(self):
        self.assertEqual(words_in_sentence(""), "")

    def test_single_letter_words(self):
        self.assertEqual(words_in_sentence("a b c d e f g h i j k l m n o p q r s t u v w x y z"), "z")

    def test_multiple_prime_length_words(self):
        self.assertEqual(words_in_sentence("one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred"), "twenty thirty forty fifty sixty seventy eighty ninety hundred")

    def test_all_non_prime_length_words(self):
        self.assertEqual(words_in_sentence("apple banana cherry date elderberry fig grape"), "grape")

    def test_mixed_case_words(self):
        self.assertEqual(words_in_sentence("One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety Hundred"), "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety Hundred")

    def test_special_characters(self):
        self.assertEqual(words_in_sentence("Hello World!"), "World!")

if __name__ == '__main__':
    unittest.main()


Explanation:

- The `TestWordsInSentence` class inherits from `unittest.TestCase`.
- It contains several test methods (`test_example_1`, `test_example_2`, etc.) to cover different scenarios.
- Each method calls the `words_in_sentence` function with specific inputs and checks if the output matches the expected result using assertions.
- If any assertion fails, it will raise an error indicating which test failed.
- Finally, the `if __name__ == '__main__':` block runs all the tests defined in the `TestWordsInSentence` class when the script is executed directly.