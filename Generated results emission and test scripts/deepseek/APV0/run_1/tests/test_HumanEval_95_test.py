You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
Here is a unittest script for the given function:


import unittest
from HumanEval_95_code import check_dict_case

class TestCheckDictCase(unittest.TestCase):

    def test_empty_dict(self):
        self.assertFalse(check_dict_case({}))

    def test_all_lower_case_keys(self):
        self.assertTrue(check_dict_case({"a": "apple", "b": "banana"}))

    def test_all_upper_case_keys(self):
        self.assertTrue(check_dict_case({"A": "apple", "B": "banana"}))

    def test_mixed_case_keys(self):
        self.assertFalse(check_dict_case({"a": "apple", "A": "banana"}))

    def test_mixed_case_keys_2(self):
        self.assertFalse(check_dict_case({"a": "apple", 8: "banana", "a": "apple"}))

    def test_mixed_case_keys_3(self):
        self.assertFalse(check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}))

    def test_all_upper_case_keys_2(self):
        self.assertTrue(check_dict_case({"STATE": "NC", "ZIP": "12345"}))

if __name__ == '__main__':
    unittest.main()


This script includes a class `TestCheckDictCase` that inherits from `unittest.TestCase`. It includes several test methods that test the `check_dict_case` function with different inputs. Each method asserts the expected output of the function.

To run the tests, you can simply execute the script. The `unittest.main()` call at the end will run all the test methods in the `TestCheckDictCase` class.

Please note that the function `check_dict_case` should be in a file named `HumanEval_95_code.py` in the same directory as this test script for the tests to work.