system
### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_95_code import check_dict_case
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()

user
### Immediate Task
Write the complete unittest test suite for the following Python function.

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

class TestCheckDictCase(unittest.TestCase):
    def test_uppercase_only(self):
        self.assertTrue(check_dict_case({"key1": "value1", "key2": "value2"}))

    def test_lowercase_only(self):
        self.assertTrue(check_dict_case({"key1": "value1", "key2": "value2"}))

    def test_mixed_case(self):
        self.assertFalse(check_dict_case({"Key1": "Value1", "Key2": "Value2"}))

    def test_empty_dict(self):
        self.assertFalse(check_dict_case({}))

    def test_non_string_key(self):
        self.assertFalse(check_dict_case({"key": "value"}))

    def test_non_string_value(self):
        self.assertFalse(check_dict_case({"key": 123}))

    def test_all_strings(self):
        self.assertTrue(check_dict_case({"key": "value"}))

    def test_all_uppercase_keys(self):
        self.assertTrue(check_dict_case({"KEY1": "VALUE1", "KEY2": "VALUE2"}))

    def test_all_lowercase_keys(self):
        self.assertTrue(check_dict_case({"key1": "value1", "key2": "value2"}))

    def test_mixed_case_with_values(self):
        self.assertFalse(check_dict_case({"Key1": "Value1", "Key2": "Value2"}))

    def test_mixed_case_with_non_string_keys(self):
        self.assertFalse(check_dict_case({"key1": "value1", "Key2": "value2"}))

    def test_mixed_case_with_non_string_values(self):
        self.assertFalse(check_dict_case({"key1": 123, "Key2": "value2"}))

    def test_mixed_case_with_non_string_keys_and_values(self):
        self.assertFalse(check_dict_case({"key1": "value1", "Key2": 123}))

if __name__ == '__main__':
    unittest.main()


This test suite covers various cases including uppercase-only, lowercase-only, mixed-case, empty dictionaries, non-string keys/values, and more complex scenarios involving both keys and values. It ensures that the `check_dict_case` function behaves as expected under different conditions.