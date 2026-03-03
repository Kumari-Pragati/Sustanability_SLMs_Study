You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

 import unittest
from HumanEval_17_code import parse_music

class TestParseMusic(unittest.TestCase):

    def test_whole_notes(self):
        self.assertEqual(parse_music('o o'), [4, 4])

    def test_half_notes(self):
        self.assertEqual(parse_music('o| o|'), [2, 2])

    def test_quarter_notes(self):
        self.assertEqual(parse_music('.| .| .| .|'), [1, 1, 1, 1])

    def test_mixed_notes(self):
        self.assertEqual(parse_music('o o| .| o| .| .| .|'), [4, 2, 1, 2, 1, 1, 1])

    def test_empty_string(self):
        self.assertEqual(parse_music(''), [])

    def test_invalid_note(self):
        with self.assertRaises(KeyError):
            parse_music('x o| .|')

if __name__ == '__main__':
    unittest.main()