Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

    def test_parse_music(self):
        # Test case 1: Basic test with expected output
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

        # Test case 2: Empty string input
        self.assertEqual(parse_music(''), [])

        # Test case 3: Single note input
        self.assertEqual(parse_music('o'), [4])

        # Test case 4: Invalid input with non-matching characters
        with self.assertRaises(ValueError):
            parse_music('x o| .| o| .| .| o')

        # Test case 5: Multiple spaces between notes
        self.assertEqual(parse_music('o   o|   .|   o|   .|   .|   .   o   o'), [4, 2, 1, 2, 1, 1, 1, 1, 4, 4])

        # Test case 6: No note input
        self.assertEqual(parse_music(' '), [])

        # Test case 7: Mixed notes input
        self.assertEqual(parse_music('o| .| o o| .| .| o'), [2, 1, 4, 2, 1, 1, 4])

        # Test case 8: Longer string with multiple note groups
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o o| .| .| .| .| o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 4])

        # Test case 9: All notes in a row
        self.assertEqual(parse_music('o o| o| .| o| .| .| o o'), [4, 2, 1, 2, 1, 1, 4])

        # Test case 10: All notes in reverse order
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| o'), [4, 2, 1, 2, 1, 1, 4])

if __name__ == '__main__':
    unittest.main()