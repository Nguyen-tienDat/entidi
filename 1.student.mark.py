#list of dict
student_list = []
course_list = []
mark_list = []

def student_number():
    s_num = int(input("Enter the number students: "))
    return s_num

def student_info(s_num):
    for _ in range(s_num):
        s_id = input("\nEnter student ID: ")
        s_name = input("Enter student name: ")
        s_dob = input("Enter student's birth of date: ")
        student_list.append({'ID': s_id, 'Name': s_name, 'DoB': s_dob})
    return student_list 

def course_number():
    n_course = int(input("\nEnter the number of courses: "))
    return n_course

def course_info(n_course):
    for _ in range(n_course):
        c_id = input("\nEnter the course ID: ")
        c_name = input("Enter the course name: ")
        course_list.append({'ID': c_id, 'Name': c_name})
    return course_list 

def get_marks(student_list, course_list):
    for course in course_list:
        course_id = course['ID']
        course_name = course['Name']
        print(f"\nEntering marks for {course_name}: ")
        for student in student_list:
            student_id = student['ID']
            student_name = student['Name']
            mark = int(input(f"Enter the mark of {student_name} in {course_name}: "))
            mark_list.append({'CourseID': course_id, 'StudentID': student_id, 'Mark': mark})
    return mark_list

def list_courses():
    print("\nCourse's List: ")
    for course in course_list:
        print(f"{course['ID']} : {course['Name']}")

def list_students():
    print("\nStudent's List: ")
    for student in student_list:
        print(f"{student['ID']} : {student['Name']} : {student['DoB']}")

def list_marks(mark_list, course_id):
    if course_id not in [course['ID'] for course in course_list]:
        print("Invalid course ID. Please try again!")
        return
    for course in course_list:
        if course['ID'] == course_id:
            print(f"\nMarks for {course['Name']}: ")
            break
    for mark in mark_list:
        if mark['CourseID'] == course_id:
            for student in student_list:
                if student['ID'] == mark['StudentID']:
                    student_name = student['Name']
                    break
            print(f"{student_name}: {mark['Mark']}")

def main():
    s_num = student_number()
    student_info(s_num)

    n_course = course_number()
    course_info(n_course)

    mark_list = get_marks(student_list, course_list)

    list_courses()
    list_students()
    course_id = input("\nEnter the course ID to show marks: ")
    list_marks(mark_list, course_id)

if __name__ == "__main__":
    main()
