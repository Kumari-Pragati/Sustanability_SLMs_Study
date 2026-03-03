You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_17_code import parse_music

class TestParseMusic(unittest.TestCase):
    def test_whole_notes(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

    def test_empty_string(self):
        self.assertEqual(parse_music(''), [])

    def test_single_note(self):
        self.assertEqual(parse_music('o'), [4])

    def test_invalid_note(self):
        with self.assertRaises(KeyError):
            parse_music('x')

    def test_multiple_notes(self):
        self.assertEqual(parse_music('o| .| o o|'), [2, 1, 4, 2])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

- `test_whole_notes`: Tests the function with a string containing all types of notes.
- `test_empty_string`: Tests the function with an empty string.
- `test_single_note`: Tests the function with a string containing only one note.
- `test_invalid_note`: Tests the function with a string containing an invalid note, which should raise a KeyError.
- `test_multiple_notes`: Tests the function with a string containing multiple notes of the same type.

Please note that the function `parse_music` should be in a file named `HumanEval_17_code.py` in the same directory for these tests to work.