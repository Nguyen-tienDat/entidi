from .base import Base
from input import get_int_input, get_str_input
from output import print_student_info

class Student(Base):
    student_list = []

    def __init__(self, student_id, student_name, student_dob):
        super().__init__()
        self.id = student_id
        self.name = student_name
        self.dob = student_dob
        Student.student_list.append(self)

    def student_Info(self):
        return f"StudentID: {self.id}, Student Name: {self.name}, Student DoB: {self.dob}"

    @classmethod
    def student_Add(cls):
        student_number = get_int_input("Enter the number of students: ")
        for _ in range(student_number):
            student_id = get_str_input("Enter the Student'ID: ")
            student_name = get_str_input("Enter the Student'name: ")
            student_dob = get_str_input("Enter the Student's DoB: ")
            new_student = cls(student_id, student_name, student_dob)
            cls.student_list.append(new_student)

    @classmethod
    def student_List(cls):
        for student in cls.student_list:
            print_student_info(student)
