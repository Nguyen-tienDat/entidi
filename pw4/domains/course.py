from .base import Base

class Course(Base):
    course_list = []

    def __init__(self, course_id, course_name):
        super().__init__(course_id, course_name)
        Course.course_list.append(self)

    def course_Info(self):
        return f"CourseID: {self.id}, Course Name: {self.name}"

    @classmethod
    def list_courses(cls):
        for course in cls.course_list:
            print(course.course_Info())
