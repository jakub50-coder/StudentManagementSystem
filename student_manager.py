#This is the student_manager class where it deals with mutiple student objects in a list and adds, views, searched, updated, and deletes any student and converts the data to a json or converts the .json to a Student object
from student import Student
import json
from pathlib import Path

STUDENTS_FILE = Path(__file__).resolve().with_name("students.json")

class StudentManager:
    #Constructor
    def __init__(self):
        self.students = []

    #This method adds a student object to the list
    def add_student(self, student):
        self.students.append(student)

    #This method shows all students in the list with their information
    def view_students(self):
        if(not self.students):
            print("The Student list is empty")
        else:
            for student in self.students:
                student.display_info()
            
    #This method searchs for an individual student is a list by looking for their name
    def search_student(self,name):
        for student in self.students:
            if student.name.lower() == name.lower():
                student.display_info()
                break
        else:
            print("Student not found")

    #This method updates a students age, major, and gpa
    def update_student(self,name, new_age, new_major, new_gpa ):
        student = self.find_student(name)
        if student is None:
            print("Student not found")
        else:
            student.update_age(new_age)
            student.update_major(new_major)
            student.update_gpa(new_gpa)
            print("Student information updated successfully!")

    #This deletes a student's data from a list
    def delete_student(self,name):
        for student in self.students:
            if(student.name.lower() == name.lower()):
                self.students.remove(student)
                print(f"{name} was deleted")
                break
        else:
            print("Student not found")

    #This method finds out whether a student is in a list or not
    def find_student(self,name):
        for student in self.students:
            if(student.name.lower() == name.lower()):
                return student
        else:
            return None

    #This method saves the students information into a .json file by converting from a Student object to a .JSON  
    def save_students(self):
        with open(STUDENTS_FILE, "w") as file:
            students_data = [student.to_dict() for student in self.students]
            json.dump(students_data,file,indent=4)

    #This method loads the student information from the .json file by converting from a .JSON to a Student Object
    def load_students(self):
        try:
            with open(STUDENTS_FILE, "r") as file:
                student_data = json.load(file)
                for information in student_data:
                    student = Student(**information)
                    self.add_student(student)
        except FileNotFoundError:
            print("Unable to find the file")
        except json.JSONDecodeError:
            print("Unable to read the file due to corruption or is empty")