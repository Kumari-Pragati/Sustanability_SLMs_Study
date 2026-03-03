user

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
        return state == "upper" or state == "lower"assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_95_code import check_dict_case

class TestCheckDictCase(unittest.TestCase):

    def test_empty_dict(self):
        self.assertFalse(check_dict_case({}))

    def test_all_lower(self):
        self.assertTrue(check_dict_case({"a": "apple", "b": "banana"}))

    def test_all_upper(self):
        self.assertTrue(check_dict_case({"STATE": "NC", "ZIP": "12345"}))

    def test_mixed_case(self):
        self.assertFalse(check_dict_case({"a": "apple", "A": "banana", "B": "banana"}))

    def test_mixed_types(self):
        self.assertFalse(check_dict_case({"a": "apple", 8: "banana", "a": "apple"}))

    def test_mixed_case_and_types(self):
        self.assertFalse(check_dict_case({"a": "apple", "Name": "John", "Age": "36", "City": "Houston"}))

    def test_all_lower_and_upper(self):
        self.assertFalse(check_dict_case({"a": "apple", "STATE": "NC", "ZIP": "12345"}))

if __name__ == '__main__':
    unittest.main()


This script includes 6 test cases:

- `test_empty_dict`: Tests that an empty dictionary returns `False`.
- `test_all_lower`: Tests that a dictionary with all lower case keys returns `True`.
- `test_all_upper`: Tests that a dictionary with all upper case keys returns `True`.
- `test_mixed_case`: Tests that a dictionary with mixed case keys returns `False`.
- `test_mixed_types`: Tests that a dictionary with mixed types (strings and non-strings) returns `False`.
- `test_mixed_case_and_types`: Tests that a dictionary with mixed case and types returns `False`.
- `test_all_lower_and_upper`: Tests that a dictionary with both lower and upper case keys returns `False`.

Each test case checks the output of the `check_dict_case` function against the expected result.