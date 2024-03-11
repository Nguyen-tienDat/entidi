import math
import numpy as np
import curses

class Base:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.dob = ''

    def _get_name(self):
        return self.name

    def _set_name(self, name):
        self.name = name

    def _get_id(self):
        return self.id

    def _set_id(self, id):
        self.id = id

    def _get_dob(self):
        return self.dob

    def _set_dob(self, dob):
        self.dob = dob

class Student(Base):
    student_list = []

    def __init__(self, student_id, student_name, student_dob, student_credits):
        super().__init__(student_id, student_name, student_dob)
        self.marks = []
        self.credits  = student_credits
        Student.student_list.append(self)

    def student_Info(self):
        return f"StudentID: {self.id}, Student Name: {self.name}, Student DoB: {self.dob}"

    @classmethod
    def student_Add(cls):
        student_id = int(input("Enter the ID of Student: "))
        student_name = input("Enter the Name of Student: ")
        student_dob = input("Enter the DoB of Student: ")
        student_credits = float(input("Enter no.of Credits for this Student : "))
        new_student = cls(student_id, student_name, student_dob, student_credits)
        return new_student

    @classmethod
    def student_List(cls):
        for student in cls.student_list:
            print(student.student_Info())

    def mark_Add(self, mark):
        self.marks.append(mark)

    def calc_GPA(self):
        marks_arr = np.array(self.marks)
        weighted_sum = np.sum(marks_arr * self.credits)
        total_credits = len(self.marks) * self.credits
        student_gpa = weighted_sum / total_credits
        return student_gpa

    def sort_student(cls):
        sorted_list = sorted(Student.student_list, key=lambda student:student.calc_GPA(), reverse=True)
        for student in sorted_list:
            print(student.student_Info())

class Course(Base):
    course_list = []

    def __init__(self, course_id, course_name):
        super().__init__(course_id, course_name)
        Course.course_list.append(self)

    def course_Info(self):
        return f"CourseID: {self.id}, Course Name: {self.name}"

    @classmethod
    def course_Add(cls):
        course_id = int(input("Enter the ID of course: "))
        course_name = input("Enter the Name of course: ")
        new_course = cls(course_id, course_name)
        return new_course

    @classmethod
    def list_courses(cls):
        for course in cls.course_list:
            print(course.course_Info())

class Mark(Base):
    marks = []

    def __init__(self, course, student, mark):
        super().__init__()
        self.course = course
        self.student = student
        self.mark = mark

    def mark_Info(self):
        return f"StudentID: {self.student._get_id()}, Student Name: {self.student._get_name()}, CourseID: {self.course._get_id()}, Course Name: {self.course._get_name()}, Mark: {self.mark}"

class System:
    def __init__(self):
        self.marks = []

    def add_Mark(self):
        course_id = int(input("Enter course ID: "))
        student_id = int(input("Enter student ID: "))
        course = None
        student = None
        for c in Course.course_list:
            if c.id == course_id:
                course = c
                break
        if not course:
            print("Invalid course id")
            return
        for s in Student.student_list:
            if s.id == student_id:
                student = s
                break
        if not student:
            print("Invalid student id")
            return
        mark = float(input("Enter the mark: "))
        mark = round(mark * 10) / 10
        m = Mark(course, student, mark)
        self.marks.append(m)
        print("Mark added Successfully!")

if __name__ == '__main__':
    system = System()

    while True:
        print("_______Student Management System_______\n")
        print("1. ADD INFORMATION OF STUDENT")
        print("2. ADD INFORMATION OF COURSE")
        print("3. ADD MARK OF STUDENT")
        print("4. STUDENT'S LIST")
        print("5. COURSE'S LIST")
        print("6. MARK'S LIST")
        print("7. STUDENT'S GPA")
        print("8. EXIT!")

        choice = int(input("Enter the option: "))

        if choice == 1:
            student = Student.student_Add()
        elif choice == 2:
            Course.course_Add()
        elif choice == 3:
            system.add_Mark()
        elif choice == 4:
            Student.student_List()
        elif choice == 5:
            Course.list_courses()
        elif choice == 6:
            for mark in system.marks:
                print(mark.mark_Info())
        elif choice == 7:
            student_id = int(input("Enter the student ID to check the GPA: "))
            student = next((s for s in Student.student_list if s.id == student_id), None)
            if not student:
                print("Student not found")
                continue
            gpa = student.calc_GPA()
            print(f"GPA of the student is : {gpa}")
        elif choice == 8:
            break
        else:
            print("Please enter a valid option.")

        print("___Update Completed____")