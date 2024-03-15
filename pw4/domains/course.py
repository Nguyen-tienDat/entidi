from .base import Base
from input import get_int_input, get_str_input
from output import print_course_info

class Course(Base):
    course_list = []

    def __init__(self, course_id, course_name):
        super().__init__()
        self.id = course_id
        self.name = course_name
        Course.course_list.append(self)

    def course_Info(self):
        return f"CourseID: {self.id}, Course Name: {self.name}"

    @classmethod
    def course_Add(cls):
        course_number = get_int_input("Enter the number of courses: ")
        for _ in range(course_number):
            course_id = get_str_input("Enter the ID of course: ")
            course_name = get_str_input("Enter the Name of course: ")
            course = cls(course_id, course_name)
            cls.course_list.append(course)

    @classmethod
    def list_courses(cls):
        for course in cls.course_list:
            print_course_info(course)

