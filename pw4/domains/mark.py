from .base import Base

class Mark(Base):
    marks = []

    def __init__(self, course, student, mark):
        super().__init__()
        self.course = course
        self.student = student
        self.mark = mark

    def mark_Info(self):
        return f"StudentID: {self.student._get_id()}, Student Name: {self.student._get_name()}, CourseID: {self.course._get_id()}, Course Name: {self.course._get_name()}, Mark: {self.mark}"
