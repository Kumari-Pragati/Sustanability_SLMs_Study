### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_17_code import parse_music
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
 ### Immediate Task
Write the complete unittest test suite for the following Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_17_code import parse_music
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def parse_music(music_string: str) -> List[int]:
    """Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return a list of integers corresponding to how many beats each note lasts.

    Legend:
    'o'  - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quarter note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    note_map = {'o': 4, 'o|': 2, '.|': 1}
    return [note_map[x] for x in music_string.split(' ') if x]

 import unittest
from HumanEval_17_code import parse_music

class TestParseMusic(unittest.TestCase):
    def test_normal_input(self):
        input_str = 'o o| .| o| o| .| .| .| o o'
        expected_output = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
        self.assertEqual(parse_music(input_str), expected_output)

    def test_empty_string(self):
        input_str = ''
        expected_output = []
        self.assertEqual(parse_music(input_str), expected_output)

    def test_single_note(self):
        input_str = 'o'
        expected_output = [4]
        self.assertEqual(parse_music(input_str), expected_output)

    def test_multiple_notes(self):
        input_str = 'o o| .| o| .| .| .| o o o|'
        expected_output = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4, 4]
        self.assertEqual(parse_music(input_str), expected_output)

    def test_invalid_input(self):
        input_str = 'o|.|o'
        with self.assertRaises(ValueError):
            parse_music(input_str)

if __name__ == '__main__':
    unittest.main()