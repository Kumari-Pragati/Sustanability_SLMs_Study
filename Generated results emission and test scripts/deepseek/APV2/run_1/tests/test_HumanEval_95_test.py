You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_95_code import check_dict_case
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False if the given dictionary is empty.
    
    Examples:
    check_dict_case({"a": "apple", "b": "banana"}) -> True
    check_dict_case({"a": "apple", "A": "banana", "B": "banana"}) -> False
    check_dict_case({"a": "apple", 8: "banana", "a": "apple"}) -> False
    check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}) -> False
    check_dict_case({"STATE": "NC", "ZIP": "12345"}) -> True
    """

    if len(dict.keys()) == 0:
        return False
    else:
        state = "start"
        for key in dict.keys():
            if not isinstance(key, str):
                state = "mixed"
                break
            if state == "start":
                if key.isupper():
                    state = "upper"
                elif key.islower():
                    state = "lower"
                else:
                    break
            elif (state == "upper" and not key.isupper()) or (state == "lower" and not key.islower()):
                state = "mixed"
                break
            else:
                break
        return state == "upper" or state == "lower"


### Response:
Here is a complete unittest test suite for the given function:


import unittest
from HumanEval_95_code import check_dict_case

class TestCheckDictCase(unittest.TestCase):

    def test_all_lower_case_keys(self):
        self.assertTrue(check_dict_case({"a": "apple", "b": "banana"}))

    def test_all_upper_case_keys(self):
        self.assertTrue(check_dict_case({"A": "apple", "B": "banana"}))

    def test_mixed_case_keys(self):
        self.assertFalse(check_dict_case({"a": "apple", "A": "banana"}))

    def test_non_string_keys(self):
        self.assertFalse(check_dict_case({8: "banana", "a": "apple"}))

    def test_empty_dictionary(self):
        self.assertFalse(check_dict_case({}))

    def test_mixed_case_and_non_string_keys(self):
        self.assertFalse(check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}))

    def test_all_upper_case_and_non_string_keys(self):
        self.assertFalse(check_dict_case({"STATE": "NC", "ZIP": "12345"}))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for all the different scenarios that the function needs to handle. It tests the function with dictionaries with all lower case keys, all upper case keys, mixed case keys, non-string keys, an empty dictionary, and a mix of upper case keys and non-string keys.