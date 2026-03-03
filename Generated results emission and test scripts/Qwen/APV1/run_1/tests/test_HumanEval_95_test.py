system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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


assistant

import unittest
from HumanEval_95_code import check_dict_case

class TestCheckDictCase(unittest.TestCase):

    def test_check_dict_case(self):
        self.assertTrue(check_dict_case({"a": "apple", "b": "banana"}))
        self.assertFalse(check_dict_case({"a": "apple", "A": "banana", "B": "banana"}))
        self.assertFalse(check_dict_case({"a": "apple", 8: "banana", "a": "apple"}))
        self.assertFalse(check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}))
        self.assertTrue(check_dict_case({"STATE": "NC", "ZIP": "12345"}))

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestCheckDictCase` class that inherits from `unittest.TestCase`. It contains a single method `test_check_dict_case`, which tests various cases of the `check_dict_case` function using assertions. If any assertion fails, it will raise an error indicating which specific case failed. This ensures that the function behaves as expected across different scenarios.