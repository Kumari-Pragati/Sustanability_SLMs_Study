You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_105_code import by_length
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """

    dic = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    sorted_arr = sorted(arr, reverse=True)
    new_arr = []
    for var in sorted_arr:
        try:
            new_arr.append(dic[var])
        except:
            pass
    return new_arr


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_105_code import by_length

class TestByLength(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(by_length([]), [])

    def test_single_digit(self):
        self.assertEqual(by_length([1]), ['One'])

    def test_multiple_digits(self):
        self.assertEqual(by_length([2, 1, 1, 4, 5, 8, 2, 3]), 
                         ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One'])

    def test_negative_number(self):
        self.assertEqual(by_length([1, -1, 55]), ['One'])

    def test_non_integer(self):
        self.assertEqual(by_length(['a', 'b', 'c']), [])

    def test_large_number(self):
        self.assertEqual(by_length([10, 20, 30]), [])

    def test_mixed_numbers(self):
        self.assertEqual(by_length([1, 2, 'a', 4, 5, 8, 2, 3]), ['Three', 'Two', 'Two', 'One', 'One'])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

1. An empty array.
2. An array with a single digit.
3. An array with multiple digits.
4. An array with a negative number.
5. An array with non-integer values.
6. An array with large numbers.
7. An array with a mix of valid and invalid numbers.

Each test checks that the function returns the expected output for a given input.