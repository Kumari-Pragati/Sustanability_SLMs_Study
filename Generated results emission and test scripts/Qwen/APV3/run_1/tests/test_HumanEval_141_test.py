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
   - Include from HumanEval_141_code import file_name_check
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
2. Include: from HumanEval_141_code import file_name_check
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    suf = ['txt', 'exe', 'dll']
    lst = file_name.split(sep='.')
    if len(lst) != 2:
        return 'No'
    if not lst[1] in suf:
        return 'No'
    if len(lst[0]) == 0:
        return 'No'
    if not lst[0][0].isalpha():
        return 'No'
    t = len([x for x in lst[0] if x.isdigit()])
    if t > 3:
        return 'No'
    return 'Yes'


assistant

import unittest

# Importing the function we want to test
from HumanEval_141_code import file_name_check

class TestFileCheck(unittest.TestCase):
    
    def test_valid_file_names(self):
        self.assertEqual(file_name_check("example.txt"), "Yes")
        self.assertEqual(file_name_check("validName.exe"), "Yes")
        self.assertEqual(file_name_check("test.dll"), "Yes")

    def test_invalid_file_names(self):
        self.assertEqual(file_name_check("1invalid.txt"), "No")
        self.assertEqual(file_name_check(".hiddenfile"), "No")
        self.assertEqual(file_name_check("noextension"), "No")
        self.assertEqual(file_name_check("invalid..dot"), "No")
        self.assertEqual(file_name_check("invalid!dot"), "No")
        self.assertEqual(file_name_check("invalid@dot"), "No")
        self.assertEqual(file_name_check("invalid%dot"), "No")
        self.assertEqual(file_name_check("invalid^dot"), "No")
        self.assertEqual(file_name_check("invalid*dot"), "No")
        self.assertEqual(file_name_check("invalid?dot"), "No")
        self.assertEqual(file_name_check("invalid&dot"), "No")
        self.assertEqual(file_name_check("invalid(dot)", "No")
        self.assertEqual(file_name_check("invalid()dot", "No")
        self.assertEqual(file_name_check("invalid[]dot", "No")
        self.assertEqual(file_name_check("invalid{}dot", "No")
        self.assertEqual(file_name_check("invalid|dot", "No")
        self.assertEqual(file_name_check("invalid;dot", "No")
        self.assertEqual(file_name_check("invalid<dot", "No")
        self.assertEqual(file_name_check("invalid>dot", "No")
        self.assertEqual(file_name_check("invalid/\\dot", "No")
        self.assertEqual(file_name_check("invalid/*dot", "No")
        self.assertEqual(file_name_check("invalid~dot", "No")
        self.assertEqual(file_name_check("invalid`dot", "No")
        self.assertEqual(file_name_check("invalid(123).txt", "No")
        self.assertEqual(file_name_check("invalid(abc).exe", "No")
        self.assertEqual(file_name_check("invalid(a.b).dll", "No")
        self.assertEqual(file_name_check("invalid(.c.d).txt", "No")
        self.assertEqual(file_name_check("invalid(.e.f).exe", "No")
        self.assertEqual(file_name_check("invalid(g.h.i).dll", "No")
        self.assertEqual(file_name_check("invalid(i.j.k).txt", "No")
        self.assertEqual(file_name_check("invalid(l.m.n).exe", "No")
        self.assertEqual(file_name_check("invalid(o.p.q).dll", "No")
        self.assertEqual(file_name_check("invalid(r.s.t).txt", "No")
        self.assertEqual(file_name_check("invalid(u.v.w).exe", "No")
        self.assertEqual(file_name_check("invalid(x.y.z).dll", "No")
        self.assertEqual(file_name_check("invalid(y.z.a).txt", "No")
        self.assertEqual(file_name_check("invalid(z.a.b).exe", "No")
        self.assertEqual(file_name_check("invalid(a.b.c).dll", "No")
        self.assertEqual(file_name_check("invalid(d.e.f).txt", "No")
        self.assertEqual(file_name_check("invalid(e.f.g).exe", "No")
        self.assertEqual(file_name_check("invalid(h.i.j).dll", "No")
        self.assertEqual(file_name_check("invalid(k.l.m).txt", "No")
        self.assertEqual(file_name_check("invalid(m.n.o).exe", "No")
        self.assertEqual(file_name_check("invalid(p.q.r).dll", "No")
        self.assertEqual(file_name_check("invalid(s.t.u).txt", "No")
        self.assertEqual(file_name_check("invalid(v.w.x).exe", "No")
        self.assertEqual(file_name_check("invalid(y.z.a).dll", "No")
        self.assertEqual(file_name_check("invalid(z.a.b).txt", "No")
        self.assertEqual(file_name_check("invalid(a.b.c).exe", "No")
        self.assertEqual(file_name_check("invalid(d.e.f).txt", "No")
        self.assertEqual(file_name_check("invalid(e.f.g).exe", "No")
        self.assertEqual(file_name_check("invalid(h.i.j).dll", "No")
        self.assertEqual(file_name_check("invalid(k.l.m).txt", "No")
        self.assertEqual(file_name_check("invalid(m.n.o).exe", "No")
        self.assertEqual(file_name_check("invalid(p.q.r).dll", "No")
        self.assertEqual(file_name_check("invalid(s.t.u).txt", "No")
        self.assertEqual(file_name_check("invalid(v.w.x).exe", "No")
        self.assertEqual(file_name_check("invalid(y.z.a).dll", "No")
        self.assertEqual(file_name_check("invalid(z.a.b).txt", "No")