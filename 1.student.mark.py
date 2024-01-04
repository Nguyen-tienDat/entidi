def number_of_students():
    numStudents = int(input("The number of students in class: "))
    return numStudents

def student_info():
    studentID = str(input("\nStudent ID: "))
    studentName = str(input("Student Name: "))
    studentDoB = str(input("Date of Birth (DD/MM/YYYY): "))
    return [studentID, studentName, studentDoB]

def number_of_courses():
    numCourses = int(input("\nCourse's number: "))
    return numCourses

def course_info():
    courseID = str(input("\nCourse ID: "))
    courseName = str(input("Course Name: "))
    return [courseID, courseName]

def select_course_to_mark(courseList):
    print("Select course to mark: ")
    for i in range(len(courseList)):
        print(f"{i+1}.{courseList[i][1]}")
    courseNum = int(input("Enter the course number: "))
    num_students_to_mark = int(input("Enter the number of students to mark: "))
    students_and_marks = []
    for i in range(num_students_to_mark):
        studentID = input("Enter the student ID to mark: ")
        courseMark = int(input(f"Enter the mark for Student {studentID}: "))
        students_and_marks.append((studentID, courseMark))
    return courseList[courseNum-1], students_and_marks

def list_courses(courseList):
    print("\nCourse's List: ")
    for i in range(len(courseList)):
        print(f"Course {courseList[i][0]} - {courseList[i][1]}")

def list_students(studentList):
    print("\nStudent's List: ")
    for i in range(len(studentList)):
        print(f"Student {studentList[i][0]}, Name: {studentList[i][1]}, DoB: {studentList[i][2]}")

def list_student_marks_for_given_course(courseList, studentCourseMarks):
    print("\nScore's List:")
    for i in range(len(courseList)):
        courseID = courseList[i][0]
        courseName = courseList[i][1]
        marks = studentCourseMarks[i]
        print(f"\nCourse {courseID} - {courseName}:")
        for studentID, mark in marks.items():
            print(f"  Student {studentID}: {mark}")

def main():
    global courseList, studentList, studentCourseMarks
    studentList = []
    courseList = []
    studentCourseMarks = []

    numStudents = number_of_students()
    for i in range(numStudents):
        studentList.append(student_info())

    numCourses = number_of_courses()
    for i in range(numCourses):
        courseList.append(course_info())
    
    for i in range(numCourses):
        studentCourseMarks.append({})

    for i in range(numCourses):
        course, students_and_marks = select_course_to_mark(courseList)
        courseID = course[0]
        for studentID, mark in students_and_marks:
            studentCourseMarks[i][studentID] = mark

    list_students(studentList)
    list_courses(courseList)
    list_student_marks_for_given_course(courseList, studentCourseMarks)

main()
