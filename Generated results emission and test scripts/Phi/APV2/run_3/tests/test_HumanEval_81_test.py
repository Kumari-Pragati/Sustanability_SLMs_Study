You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_81_code import unknown_function
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """

    letter_grade = []
        for gpa in grades:
            if gpa == 4.0:
                letter_grade.append("A+")
            elif gpa > 3.7:
                letter_grade.append("A")
            elif gpa > 3.3:
                letter_grade.append("A-")
            elif gpa > 3.0:
                letter_grade.append("B+")
            elif gpa > 2.7:
                letter_grade.append("B")
            elif gpa > 2.3:
                letter_grade.append("B-")
            elif gpa > 2.0:
                letter_grade.append("C+")
            elif gpa > 1.7:
                letter_grade.append("C")
            elif gpa > 1.3:
                letter_grade.append("C-")
            elif gpa > 1.0:
                letter_grade.append("D+")
            elif gpa > 0.7:
                letter_grade.append("D")
            elif gpa > 0.0:
                letter_grade.append("D-")
            else:
                letter_grade.append("E")
        return letter_grade

 import unittest
from HumanEval_81_code import numerical_letter_grade

class TestNumericalLetterGrade(unittest.TestCase):

    def test_numerical_letter_grade_4_0(self):
        grades = [4.0]
        expected_output = ['A+']
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_numerical_letter_grade_above_3_7(self):
        grades = [3.8]
        expected_output = ['A']
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_numerical_letter_grade_above_3_3(self):
        grades = [3.4]
        expected_output = ['A-']
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_numerical_letter_grade_above_3_0(self):
        grades = [3.1]
        expected_output = ['B+']
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_numerical_letter_grade_above_2_7(self):
        grades = [2.8]
        expected_output = ['B']
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_numerical_letter_grade_above_2_3(self):
        grades = [2.4]
        expected_output = ['B-']
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_numerical_letter_grade_above_2_0(self):
        grades = [2.1]
        expected_output = ['C+']
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_numerical_letter_grade_above_1_7(self):
        grades = [1.8]
        expected_output = ['C']
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_numerical_letter_grade_above_1_3(self):
        grades = [1.4]
        expected_output = ['C-']
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_numerical_letter_grade_above_1_0(self):
        grades = [1.1]
        expected_output = ['D+']
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_numerical_letter_grade_above_0_7(self):
        grades = [0.8]
        expected_output = ['D']
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_numerical_letter_grade_above_0_0(self):
        grades = [0.1]
        expected_output = ['D-']
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_numerical_letter_grade_equal_0_0(self):
        grades = [0.0]
        expected_output = ['E']
        self.assertEqual(numerical_letter_grade(grades), expected_output)

    def test_numerical_letter_grade_empty_list(self):
        grades = []
        expected_output = []
        self.assertEqual(numerical_letter_grade(grades), expected_output)

if __name__ == '__main__':
    unittest.main()