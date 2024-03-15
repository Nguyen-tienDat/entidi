from domains.student import Student
from domains. course import Course
from domains.mark import Mark

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid floating-point number.")

def get_str_input(prompt):
    return input(prompt)

def write_student_info():
    with open ("C:\Users\admin\entidi\pw5\student.txt", "a")as file:
        print("\nStudent Information")
        print("-----------------------")
        for student_name, student_id, student_dob in Student.student_Add:
            file.write(f"Student ID: {student_id}_____Student Name: {student_name}_____Student DoB: {student_dob}")
            
def write_course_info():
    with open("C:\Users\admin\entidi\pw5\courses.txt","a") as file :
        print("\nCourse Information")
        print("----------------------")
        for course_name, course_id in Course.course_Add:
            file.write(f"Course ID: {course_id}_____Course Name: {course_name}")

def write_mark_info():
    with open("C:\Users\admin\entidi\pw5\mark.txt", "a") as file:
        print("Marks Information")
        print("-------------------")
        file.write(Mark.list_Mark())