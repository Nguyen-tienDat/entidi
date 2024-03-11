import numpy as np
from .base import Base

class Student(Base):
    student_list = []

    def __init__(self, student_id, student_name, student_dob, student_credits):
        super().__init__(student_id, student_name, student_dob)
        self.marks = []
        self.credits = student_credits
        Student.student_list.append(self)

    def student_Info(self):
        return f"StudentID: {self.id}, Student Name: {self.name}, Student DoB: {self.dob}"

    @classmethod
    def student_List(cls):
        for student in cls.student_list:
            print(student.student_Info())

    def add_mark(self, mark):
        self.marks.append(mark)

    def calc_GPA(self):
        marks_arr = np.array(self.marks)
        weighted_sum = np.sum(marks_arr * self.credits)
        total_credits = len(self.marks) * self.credits
        student_gpa = weighted_sum / total_credits
        return student_gpa

    @classmethod
    def sort_student(cls):
        sorted_list = sorted(Student.student_list, key=lambda student:student.calc_GPA(), reverse=True)
        for student in sorted_list:
            print(student.student_Info())
