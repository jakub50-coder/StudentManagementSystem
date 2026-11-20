#This is the main class of the program that includes the main menu and methods that validate the gpa, age, name, and major. 
from student import Student
from student_manager import StudentManager

# This method is used to validate the gpa to make sure that the gpa value is between 0.0 and 4.0
def get_valid_gpa():
    while True:
        try:
            gpa = float(input("Enter the gpa of the student: "))
            if(gpa >= 0.0 and gpa <= 4.0):
                return gpa
            print("Enter a valid GPA value")
        except ValueError:
            print("Enter a valid GPA value")
        
#This method is used to validate age by making sure that the age is not a negative number       
def get_valid_age():
    while True:
        try:
            age = int(input("Enter the age of the student: "))
            if(age >= 0):
                return age
            print("Enter a valid age")
        except ValueError:
            print("Enter a valid age value")

#This method validate the name and major by making sure that they are not blank
def get_valid_text(prompt):
    while True:
        answer = input(prompt).strip()
        if answer:
            return answer
        print("Field can't be empty")

#This is where the menu us created
print("--------------------------------------------\n")
print("***     Student Management System        ***\n")
print("--------------------------------------------\n")
manager = StudentManager()
manager.load_students()
while(True):
    #Menu options
    print("Welcome to the Student Management System\n")
    print("1. Add New Student\n")
    print("2. View All Students\n")
    print("3. Search Student\n")
    print("4. Update Student\n")
    print("5. Delete Student\n")
    print("6. Exit\n")
    try:
        choice = int(input("Enter the choice that you want to do: "))
        #Choice one, adds a new student
        if(choice == 1):
            name = get_valid_text("Enter the name of the student: ")
            age = get_valid_age()
            major = get_valid_text("Enter the major of the student: ")
            gpa = get_valid_gpa()
            student = Student(name, age, major, gpa)
            manager.add_student(student)
        #Choice two, allows the user to view all the students in the data
        elif(choice == 2):
            manager.view_students()
        #Choice three, allows the user to search for an individual student
        elif(choice == 3):
           name = get_valid_text("Enter the name of the student you want to view: ")
           manager.search_student(name)
        #Choice four, allows a user to update a student's information
        elif(choice == 4):
            name = get_valid_text("Enter the name of the student that you want to change: ")
            student = manager.find_student(name)
            if student is None:
                print("Student not found")
            else:
                new_age = get_valid_age()
                new_major = get_valid_text("What would you like to change the major to: ")
                new_gpa = get_valid_gpa()
                manager.update_student(name, new_age, new_major, new_gpa)
        #Choice five allows the user to delete a student's data
        elif(choice == 5):
            name = get_valid_text("Enter the name of the student that you want to delete: ")    
            manager.delete_student(name)
        #Choice six saves the data into the .json file and exits the program
        elif choice == 6:
            manager.save_students()
            print("Have a nice day!")  
            break 
        #When a user types an invalid option
        else:
            print("Please enter a valid option between 1 - 6.")    
    except ValueError:
            print("Enter a valid number")
