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

 Here is a comprehensive unittest test suite for the `parse_music` function:


import unittest
from HumanEval_17_code import parse_music

class TestParseMusic(unittest.TestCase):

    def test_parse_music_basic(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])
        self.assertEqual(parse_music('o'), [4])
        self.assertEqual(parse_music('o|'), [2])
        self.assertEqual(parse_music('.|'), [1])
        self.assertEqual(parse_music(''), [])

    def test_parse_music_spaces(self):
        self.assertEqual(parse_music('o   o|   .|   o|   o|   .|   .|   .|   .|   o   o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])
        self.assertEqual(parse_music('o|   '), [2])
        self.assertEqual(parse_music('.|   '), [1])

    def test_parse_music_invalid_notes(self):
        self.assertEqual(parse_music('x'), [])
        self.assertEqual(parse_music('o x'), [])
        self.assertEqual(parse_music('o|x'), [])
        self.assertEqual(parse_music('.|x'), [])
        self.assertEqual(parse_music('x o'), [])
        self.assertEqual(parse_music('ox'), [])
        self.assertEqual(parse_music('o|x'), [])
        self.assertEqual(parse_music('.|x'), [])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for basic functionality, handling spaces in the input string, and tests for invalid notes. The test cases are designed to cover a variety of edge cases and ensure that the function behaves as expected.