You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function `numerical_letter_grade`.


import unittest
from HumanEval_81_code import numerical_letter_grade

class TestNumericalLetterGrade(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(numerical_letter_grade([]), [])

    def test_single_gpa(self):
        self.assertListEqual(numerical_letter_grade([4.0]), ["A+"])
        self.assertListEqual(numerical_letter_grade([3.8]), ["A"])
        self.assertListEqual(numerical_letter_grade([3.2]), ["A-"])
        self.assertListEqual(numerical_letter_grade([3.1]), ["B+"])
        self.assertListEqual(numerical_letter_grade([2.8]), ["B"])
        self.assertListEqual(numerical_letter_grade([2.2]), ["B-"])
        self.assertListEqual(numerical_letter_grade([2.1]), ["C+"])
        self.assertListEqual(numerical_letter_grade([1.8]), ["C"])
        self.assertListEqual(numerical_letter_grade([1.2]), ["C-"])
        self.assertListEqual(numerical_letter_grade([1.1]), ["D+"])
        self.assertListEqual(numerical_letter_grade([0.8]), ["D"])
        self.assertListEqual(numerical_letter_grade([0.1]), ["D-"])
        self.assertListEqual(numerical_letter_grade([0.0]), ["E"])

    def test_multiple_gpas(self):
        self.assertListEqual(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]), ["A+", "B", "C-", "C", "A-"])
        self.assertListEqual(numerical_letter_grade([3.8, 3.2, 3.1, 2.8, 2.2, 2.1, 1.8, 1.2, 1.1, 0.8, 0.1, 0.0]),
                              ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for an empty list, single GPAs, and multiple GPAs. It covers all the possible cases mentioned in the given table.