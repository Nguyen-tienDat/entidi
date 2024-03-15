from .base import Base
from input import get_str_input, get_float_input
from output import print_mark_info
from .student import Student
from .course import Course

class Mark(Base):
    mark_list = []

    def __init__(self, course, student, mark):
        super().__init__()
        self.course = course
        self.student = student
        self.mark = mark

    def mark_Info(self):
        return f"StudentID: {self.student.id}, Student Name: {self.student.name}, CourseID: {self.course.id}, Course Name: {self.course.name}, Mark: {self.mark}"

    @classmethod
    def add_Mark(cls):
        while True:
            course_id = get_str_input("Enter course ID to mark (or 'q' to quit): ")
            if course_id == 'q':
                break
            else:
                course = None
                for c in Course.course_list:
                    if c.id != course_id:
                        print("Invalid course ID, try again!")
                        continue
                    else:
                        course = c

                student_id = get_str_input("Enter Student ID to mark(or 'q' to quit): ")
                if student_id == 'q':
                    break
                else:
                    student = None
                    for s in Student.student_list:
                        if s.id != student_id:
                            print("Invalid student ID, try again!")
                            continue
                        else:
                            mark = get_float_input(f"Enter the mark of student {student_id} in course {course_id}: ")
                            mark = round(mark * 10) / 10
                            mark_saved = cls(course, student, mark)
                            cls.mark_list.append(mark_saved)
                            print("Mark added Successfully!")

    @classmethod
    def list_Mark(cls):
        while True:
            listed_mark = get_str_input("Enter Course ID to see Mark List: ")
            print(f"Mark List for course {listed_mark}: ")
            for i in range(len(cls.mark_list)):
                if cls.mark_list[i].course.id == listed_mark:
                    print(f"StudentID={cls.mark_list[i].student.id}, Mark= {cls.mark_list[i].mark}")
