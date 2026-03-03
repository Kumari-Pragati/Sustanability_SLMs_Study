You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

 import unittest
from HumanEval_105_code import by_length

class TestByLengthFunction(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(by_length([]), [])

    def test_single_digit_array(self):
        self.assertEqual(by_length([1]), ["One"])
        self.assertEqual(by_length([2]), ["Two"])
        self.assertEqual(by_length([3]), ["Three"])
        self.assertEqual(by_length([4]), ["Four"])
        self.assertEqual(by_length([5]), ["Five"])
        self.assertEqual(by_length([6]), ["Six"])
        self.assertEqual(by_length([7]), ["Seven"])
        self.assertEqual(by_length([8]), ["Eight"])
        self.assertEqual(by_length([9]), ["Nine"])

    def test_mixed_digit_array(self):
        self.assertEqual(by_length([9, 5, 1, 4, 3, 2]), ["Nine", "Five", "Four", "Three", "Two", "One"])

    def test_negative_numbers(self):
        self.assertEqual(by_length([-1, 1, 55]), ["One"])

    def test_non_digit_numbers(self):
        self.assertEqual(by_length([1, -1, 55]), ["One"])

    def test_array_with_non_digit_numbers(self):
        self.assertEqual(by_length([1, -1, 55, 10]), ["One", "One"])

    def test_array_with_zero(self):
        self.assertEqual(by_length([0, 9, 8, 7]), ["Nine", "Eight", "Seven"])

    def test_array_with_non_unique_digits(self):
        self.assertEqual(by_length([9, 9, 8, 7]), ["Nine", "Nine", "Eight", "Seven"])

    def test_array_with_multiple_digits(self):
        self.assertEqual(by_length([99, 88, 77]), ["Nine", "Nine", "Seven"])

if __name__ == '__main__':
    unittest.main()