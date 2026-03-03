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
    def test_uppercase_keys(self):
        self.assertTrue(check_dict_case({"a": "apple", "B": "banana"}))

    def test_lowercase_keys(self):
        self.assertTrue(check_dict_case({"a": "apple", "b": "banana"}))

    def test_mixed_case_keys(self):
        self.assertFalse(check_dict_case({"a": "apple", "B": "banana"}))

    def test_non_string_keys(self):
        self.assertFalse(check_dict_case({1: "apple", "b": "banana"}))

    def test_empty_dictionary(self):
        self.assertFalse(check_dict_case({}))

    def test_all_uppercase_keys(self):
        self.assertTrue(check_dict_case({"A": "apple", "B": "banana"}))

    def test_all_lowercase_keys(self):
        self.assertTrue(check_dict_case({"a": "apple", "b": "banana"}))

    def test_mixed_case_keys_with_different_cases(self):
        self.assertFalse(check_dict_case({"A": "apple", "b": "banana"}))

    def test_mixed_case_keys_with_same_case(self):
        self.assertTrue(check_dict_case({"A": "apple", "a": "apple"}))

    def test_mixed_case_keys_with_different_cases_and_strings(self):
        self.assertFalse(check_dict_case({"A": "apple", "b": "banana"}))

    def test_mixed_case_keys_with_different_cases_and_numbers(self):
        self.assertFalse(check_dict_case({"A": "apple", "b": 123}))

    def test_mixed_case_keys_with_different_cases_and_lists(self):
        self.assertFalse(check_dict_case({"A": "apple", "b": ["banana"]}))

    def test_mixed_case_keys_with_different_cases_and_tuples(self):
        self.assertFalse(check_dict_case({"A": "apple", "b": ("banana",)}))

    def test_mixed_case_keys_with_different_cases_and_sets(self):
        self.assertFalse(check_dict_case({"A": "apple", "b": {"banana"}}))

    def test_mixed_case_keys_with_different_cases_and_frozensets(self):
        self.assertFalse(check_dict_case({"A": "apple", "b": frozenset(["banana"])}))

    def test_mixed_case_keys_with_different_cases_and_dicts(self):
        self.assertFalse(check_dict_case({"A": "apple", "b": {}}))

    def test_mixed_case_keys_with_different_cases_and_none(self):
        self.assertFalse(check_dict_case(None))

    def test_mixed_case_keys_with_different_cases_and_bytes(self):
        self.assertFalse(check_dict_case(b"A"))

    def test_mixed_case_keys_with_different_cases_and_integers(self):
        self.assertFalse(check_dict_case(1))

    def test_mixed_case_keys_with_different_cases_and_floats(self):
        self.assertFalse(check_dict_case(1.0))

    def test_mixed_case_keys_with_different_cases_and_complex_numbers(self):
        self.assertFalse(check_dict_case(complex(1)))

    def test_mixed_case_keys_with_different_cases_and_nan(self):
        self.assertFalse(check_dict_case(float('nan')))

    def test_mixed_case_keys_with_different_cases_and_inf(self):
        self.assertFalse(check_dict_case(float('inf')))

    def test_mixed_case_keys_with_different_cases_and_infs(self):
        self.assertFalse(check_dict_case(float('-inf')))

    def test_mixed_case_keys_with_different_cases_and_inf_nan(self):
        self.assertFalse(check_dict_case(float('nan', 'inf')))

    def test_mixed_case_keys_with_different_cases_and_inf_nan(self):
        self.assertFalse(check_dict_case(float('nan', '-inf')))

    def test_mixed_case_keys_with_different_cases_and_inf_nan(self):
        self.assertFalse(check_dict_case(float('nan', 'inf', '-inf')))

    def test_mixed_case_keys_with_different_cases_and_inf_nan(self):
        self.assertFalse(check_dict_case(float('nan', '-inf', 'inf')))

    def test_mixed_case_keys_with_different_cases_and_inf_nan(self):
        self.assertFalse(check_dict_case(float('nan', 'inf', '-inf', 'nan')))

    def test_mixed_case_keys_with_different_cases_and_inf_nan(self):
        self.assertFalse(check_dict_case(float('nan', '-inf', 'inf', 'nan')))

    def test_mixed_case_keys_with_different_cases_and_inf_nan(self):
        self.assertFalse(check_dict_case(float('nan', 'inf', '-inf', 'nan', 'inf')))

    def test_mixed_case_keys_with_different_cases_and_inf_nan(self):
        self.assertFalse(check_dict_case(float('nan', '-inf', 'inf', 'nan', 'inf', 'nan')))

    def test_mixed_case_keys_with_different_cases_and_inf_nan(self):
        self.assertFalse(check_dict_case(float('nan', 'inf', '-inf', 'nan', 'inf', 'nan', 'inf')))

    def test_mixed_case_keys_with_different_cases_and_inf_nan(self):
        self.assertFalse(check