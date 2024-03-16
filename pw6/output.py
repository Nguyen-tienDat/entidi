def print_student_info(student):
    print(f"StudentID: {student.id}, Student Name: {student.name}, Student DoB: {student.dob}")

def print_course_info(course):
    print(f"CourseID: {course.id}, Course Name: {course.name}")

def print_mark_info(mark):
    print(f"StudentID: {mark.student.id}, Student Name: {mark.student.name}, CourseID: {mark.course.id}, Course Name: {mark.course.name}, Mark: {mark.mark}")
