Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_113_code import odd_count
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> odd_count(['3', "11111111"])
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    """

    res = []
    for arr in lst:
        n = sum(int(d) % 2 == 1 for d in arr)
        res.append(
            "the number of odd elements "
            + str(n)
            + "n the str"
            + str(n)
            + "ng "
            + str(n)
            + " of the "
            + str(n)
            + "nput."
        )
    return res

 Here is the unittest test script for the `odd_count` function:


import unittest
from HumanEval_113_code import odd_count

class TestOddCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(odd_count([]), [])

    def test_single_element(self):
        self.assertEqual(odd_count(['1234567']), ["the number of odd elements 4n the str4ng 4 of the 4nput."])

    def test_multiple_elements(self):
        self.assertEqual(odd_count(['3', "11111111"]), ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."])

    def test_odd_digits_only(self):
        self.assertEqual(odd_count(['1', '3', '5', '7', '9']), ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 1n the str3ng 3 of the 3nput.", "the number of odd elements 1n the str5ng 5 of the 5nput.", "the number of odd elements 1n the str7ng 7 of the 7nput.", "the number of odd elements 1n the str9ng 9 of the 9nput."])

    def test_even_digits_only(self):
        self.assertEqual(odd_count(['0', '2', '4', '6', '8']), ["the number of odd elements 0n the str0ng 0 of the 0nput.", "the number of odd elements 0n the str2ng 2 of the 2nput.", "the number of odd elements 0n the str4ng 4 of the 4nput.", "the number of odd elements 0n the str6ng 6 of the 6nput.", "the number of odd elements 0n the str8ng 8 of the 8nput."])

    def test_mixed_digits(self):
        self.assertEqual(odd_count(['123', '456', '7890']), ["the number of odd elements 1n the str123ng 123 of the 123nput.", "the number of odd elements 2n the str456ng 456 of the 456nput.", "the number of odd elements 3n the str7890ng 7890 of the 7890nput."])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as an empty list, single element, multiple elements, odd digits only, even digits only, and mixed digits. You can run this script directly to test the `odd_count` function.