from input import get_student_info, get_course_info, get_mark_info
from output import display_students
from domains import Student, Course, System

def main():
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
            student_info = get_student_info()
            student = Student(*student_info)
        elif choice == 2:
            course_info = get_course_info()
            course = Course(*course_info)
        elif choice == 3:
            mark_info = get_mark_info()
            system.add_Mark(*mark_info)
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

if __name__ == '__main__':
    main()
