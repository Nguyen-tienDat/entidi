
def noOfStudent():
    return int(input("Enter the number of students: "))
    
def infoStudent():
    student_number = noOfStudent()
    student_list = [] #create an empty list to store all information about each student
    for _ in range(student_number):
        student_id = input("Enter the Student'ID: ")
        student_name = input("Enter the Student'name: ")
        student_dob = input("Enter the Student's DoB: ")
        
        student_info = {'ID': student_id, 'Name' : student_name, 'DoB': student_dob}
        #Create  a dictionary containing id, name and date of birth. Add it into the student_list
        student_list.append(student_info)
        #Added student info  into the empty list
        return student_list
    
def noOfCourse():
    return int(input("Enter the number of courses: "))
    
def infoCourse():
    course_list = []
    course_number = noOfCourse()
    for _ in range(course_number):
        course_id = input("Enter the Course's ID: ")
        course_name = input("Enter the Course's name: ")
        
        course_info = {'ID': course_id, 'Name': course_name}
        course_list.append(course_info)
        return course_list
    
def getMark (student_list, course_list): 
    mark_list = []
    while True:
        print("Enter a course to mark: ")
        #list existing courses
        for course in course_list:
            course_id = course['ID']
            course_name = course['Name']
            print(f"{course_id}: {course_name}") 
            selected_course = input("Enter Course ID to mark(or 'q' to quit): ")
            
            if selected_course == 'q':
                break
            else:    
                
        
        #check if the input course is existed or not
                if  selected_course not in [course_id]:
                    print("Invalid Course ID, try again!")
                    continue  
                else : 
                    selected_student = input("Enter Student ID to mark: ")
                
                    for student in student_list:
                        student_id = student['ID']
                        student_name = student['Name']
                        print(f"{student_id}: {student_name}")
                
                    if  selected_student in [student_id] :
                        mark = input("Enter mark of {student_name} in {course_name}: ")
                        mark_list.append({'CourseID': course_id, 'StudentID': student_id, 'Mark': mark })
                        print("Added Mark")
                    else:
                        print("Invalid student ID, try again!")
                        continue
                    
def listStudent(student_list):
    print("Student's List: ")
    for student in student_list:
        print(f"{student['ID']}__{student['Name']}__{student['DoB']}")
        
def listCourse(course_list):
    print("Course's List: ")
    for course in course_list:
        print(f"{course['ID']}__{course['Name']}")

def listMark(mark_list, course_id):
    while True:
        listed_mark = input("Enter Course ID to see Mark List(or 'q' to quit if none of course is chosen): ")
        if listed_mark not in course_id:
            print("Invalid course ID to see mark. Try again!")
            continue
        else:
            print(f"Mark List for course {listed_mark}: ")
            for i in mark_list:
                print(f"\nID: {i['ID']}___Name: {i['Name']}___Mark: {i['Mark']}")
                continue

# Main Program

if __name__ == "__main__":
    # Initialise empty lists and dictionaries
        student_list = []
        course_list = []
        mark_list = []
        while True: 
            print("__________STUDENT MANAGEMENT SYSTEM_________")
            print("Options: ")
            print("1.  Add Student.")
            print("2.  Add Course.")
            print("3.  Add Mark.")
            print("4.  View Students.")
            print("5.  View Courses. ")
            print("6.  View Mark List. ")
            print("7. Exit")
            choice  = int(input("Enter option: "))
            if choice  == 1: 
                student_number = noOfStudent
                student_list = infoStudent(student_number)
            if choice == 2: 
                course_number = noOfCourse
                course_list = infoCourse(course_number)
            if choice == 3: 
                if len(student_list)==0 or len(course_list) == 0 :
                    print("\nPlease add students and courses information first!")
                    continue
                else:
                    getMark(student_list, course_list, mark_list)
            if choice == 4: 
                if  len(student_list) == 0:
                    print("No student added yet!\n")
                    continue
                else:
                    listStudent(student_list)
            if choice == 5:
                if len(course_list) == 0 :
                    print("No courses added yet!\n") 
                    continue
                else:
                    listCourse(course_list)
            if choice == 6: 
                if len(course_list) == 0 and len(mark_list) == 0: 
                    print("No data to display.\n")
                else:
                    listMark(course_list, mark_list)
            if choice == 7:
                break
            else:
                print("\nInvalid Option. Try again!!!")
                continue
        print("______Completed!!!________")
    
                
        
        
                
        