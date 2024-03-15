from domains.student import Student
from domains.course import Course
from domains.mark import Mark
from input import get_int_input

if __name__ == '__main__':
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

        choice = get_int_input("Enter the option: ")

        if choice == 1:
            Student.student_Add()
        elif choice == 2:
            Course.course_Add()
        elif choice == 3:
            if len(Student.student_list) == 0 or len(Course.course_list) == 0:
                print("\nPlease add information of students and courses first!\n")
            else:
                Mark.add_Mark()
        elif choice == 4:
            if len(Student.student_list) == 0:
                print("\n No student added yet!")
                continue
            else:
                Student.student_List()
        elif choice == 5:
            if len(Course.course_list) == 0:
                print("No courses added yet!\n")
                continue
            else:
                Course.list_courses()
        elif choice == 6:
            if len(Course.course_list) == 0 and len(Mark.mark_list) == 0: 
                    print("No data to display.\n")
                    continue
            else:
                    Mark.list_Mark()   
        elif choice == 7:
            student_id = int(input("Enter the student ID to check GPA: "))
            student = next((s for s in Student.student_list if s.id == student_id), None)
            if not student:
                print("Student not found")
                continue
            else:
                gpa = student.calculate_GPA()
                print(f"The GPA is {gpa}")
        elif choice == 8:  
            print(" Exit  Program...... \n")
            break           
            
        else:
            print("Please enter a valid option.")

        print("___Update Completed____")
           
