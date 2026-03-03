You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the `parse_music` function:


import unittest
from HumanEval_17_code import parse_music

class TestParseMusic(unittest.TestCase):

    def test_parse_music_basic(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

    def test_parse_music_empty(self):
        self.assertEqual(parse_music(''), [])

    def test_parse_music_single_note(self):
        self.assertEqual(parse_music('o'), [4])
        self.assertEqual(parse_music('o|'), [2])
        self.assertEqual(parse_music('.|'), [1])

    def test_parse_music_multiple_notes(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])
        self.assertEqual(parse_music('o| o| o| o'), [2, 2, 2, 2])
        self.assertEqual(parse_music('.| .| .| .| .'), [1, 1, 1, 1])

    def test_parse_music_spaces(self):
        self.assertEqual(parse_music('   o   o|   .|   o|   o|   .|   .|   .|   .|   o   o   '), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as empty strings, single notes, multiple notes, and spaces in the input string. The test cases are designed to be comprehensive and cover various edge cases.