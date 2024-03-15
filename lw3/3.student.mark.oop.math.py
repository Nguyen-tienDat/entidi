import numpy as np
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

    def __init__(self, student_id, student_name, student_dob):
        super().__init__()
        self.id = student_id
        self.name = student_name
        self.dob = student_dob
        Student.student_list.append(self)

    def student_Info(self):
        return f"StudentID: {self.id}, Student Name: {self.name}, Student DoB: {self.dob}"

    @classmethod
    def student_Add(cls):
        student_number = int(input("Enter the number of students: "))
        for _ in range (student_number):
            student_id = input("Enter the Student'ID: ")
            student_name = input("Enter the Student'name: ")
            student_dob = input("Enter the Student's DoB: ")
            student_credits = float(input("Enter no.of Credits for this Student : "))
            
            new_student = cls(student_id, student_name, student_dob, student_credits)
            cls.student_list.append(new_student)

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
        super().__init__()
        self.id = course_id
        self.name = course_name
        Course.course_list.append(self)

    def course_Info(self):
        return f"CourseID: {self.id}, Course Name: {self.name}"

    @classmethod
    def course_Add(cls):
        course_number = int(input("Enter the number of courses: "))
        for _ in range (course_number):
            course_id = input("Enter the ID of course: ")
            course_name = input("Enter the Name of course: ")
            
            course = cls(course_id, course_name)
            cls.course_list.append(course)

    @classmethod
    def list_courses(cls):
        for course in cls.course_list:
            print(course.course_Info())


class Mark(Base):
    mark_list = []

    def __init__(self, course, student, mark):
        super().__init__()
        self.course = course
        self.student = student
        self.mark = mark

    def mark_Info(self):
        return f"StudentID: {self.student.id}, Student Name: {self.student.name}, CourseID: {self.course.id}, Course Name: {self.course.name}, Mark: {self.mark}"

    def __init__(self):
        self.marks = []

    def add_Mark(cls):
        while True:
            course_id = input("Enter course ID to mark (or 'q' to quit): ")
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

                student_id = input("Enter Student ID to mark(or 'q' to quit): ")
                if student_id == 'q':
                    break
                else:
                    student = None
                    for s in Student.student_list:
                        if s.id != student_id:
                            print("Invalid student ID, try again!")
                            continue
                        else:
                            mark = float(input("Enter the mark of student {student_id} in course{course_id}: "))
                            mark = round(mark*10)/10
                            mark_saved = cls(course, student, mark)
                            cls.mark_list.append(mark_saved)
                            print("Mark added Successfully!")
    @classmethod
    def list_Mark(cls):
        while True:
            listed_mark = input("Enter Course ID to see Mark List: ")
            print(f"Mark List for course {listed_mark}: ")
            for i in  range(len(cls.mark_list)):
                if cls.mark_list[i].course.id == listed_mark:
                    print(f"StudentID={cls.mark_list[i].student.id}, Mark= {cls.mark_list[i].mark}")
            

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

        choice = int(input("Enter the option: "))

        if choice == 1:
            Student.student_Add()
        elif choice == 2:
            Course.course_Add()
        elif choice == 3:
            if len(Student.student_list)==0 or len(Course.course_list) == 0:
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
