Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_111_code import histogram
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """

    dict1 = {}
    list1 = test.split(" ")
    t = 0

    for i in list1:
        if (list1.count(i) > t) and i != '':
            t = list1.count(i)
    if t > 0:
        for i in list1:
            if list1.count(i) == t:
                dict1[i] = t
    return dict1

 Here is a unittest test script for the provided `histogram` function. I've added several test cases to cover various scenarios, including edge cases.


import unittest
from HumanEval_111_code import histogram

class TestHistogram(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(histogram(''), {})

    def test_single_letter(self):
        self.assertEqual(histogram('a'), {'a': 1})
        self.assertEqual(histogram('b'), {'b': 1})
        self.assertEqual(histogram('c'), {'c': 1})

    def test_multiple_letters(self):
        self.assertEqual(histogram('a b c'), {'a': 1, 'b': 1, 'c': 1})
        self.assertEqual(histogram('a b b a'), {'a': 2, 'b': 2})
        self.assertEqual(histogram('a b c a b'), {'a': 2, 'b': 2})
        self.assertEqual(histogram('b b b b a'), {'b': 4, 'a': 1})
        self.assertEqual(histogram('A B C'), {'a': 1, 'b': 1, 'c': 1})
        self.assertEqual(histogram('1 2 3'), {})

    def test_duplicate_spaces(self):
        self.assertEqual(histogram('a   b   c'), {'a': 1, 'b': 1, 'c': 1})

    def test_case_insensitive(self):
        self.assertEqual(histogram('a B c'), {'a': 1, 'b': 1, 'c': 1})

if __name__ == '__main__':
    unittest.main()


This test script includes tests for an empty string, single letters, multiple letters, duplicate spaces, and case insensitivity. You can run this script directly to test your `histogram` function.