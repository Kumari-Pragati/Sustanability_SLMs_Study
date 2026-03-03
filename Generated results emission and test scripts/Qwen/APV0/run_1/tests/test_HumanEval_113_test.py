system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Function to be tested
from HumanEval_113_code import odd_count

class TestOddCount(unittest.TestCase):
    def test_odd_count(self):
        # Test case 1
        self.assertEqual(odd_count(["1234567"]), ["the number of odd elements 4 in the string 4 of the input.",])
        
        # Test case 2
        self.assertEqual(odd_count(["3", "11111111"]), ["the number of odd elements 1 in the string 1 of the input.", "the number of odd elements 8 in the string 8 of the input."])

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` module, defines the `odd_count` function as provided, and then creates a test class `TestOddCount` that inherits from `unittest.TestCase`. It includes two test cases (`test_odd_count`) using the `assertEqual` method to verify the correctness of the `odd_count` function against the expected outputs. Finally, it runs the tests when executed directly.