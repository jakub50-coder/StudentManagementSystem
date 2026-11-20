#This is a student class, which deals with the individual data of each student, such as the name, age, major, and gpa of a student
class Student:
    #Constructor
    def __init__(self, name, age, major, gpa):
        if not name.strip():
            raise ValueError("Name can't be empty")
        self.name = name
        if age < 0:
            raise ValueError("The age can't be less than 0")
        self.age = age
        if not major.strip():
            raise ValueError("Major can't be empty")
        self.major = major
        if gpa < 0.0 or gpa > 4.0:
            raise ValueError("The GPA value must be between 0.0 and 4.0")
        self.gpa = gpa

    #This method displays the information of a student, which is their name, age, major, and gpa
    def display_info(self):
        print(f"Name: {self.name}\n")
        print(f"Age: {self.age}\n")
        print(f"Major: {self.major}\n")
        print(f"GPA: {self.gpa:.2f}\n")

    #This method updates a student's gpa
    def update_gpa(self, new_gpa):
        if new_gpa < 0.0 or new_gpa > 4.0:
            raise ValueError("The new GPA value must be between 0.0 and 4.0")
        self.gpa = new_gpa

    #This method updates a student's major
    def update_major(self, new_major):
        if not new_major.strip():
            raise ValueError("The new major can't be blank")
        self.major = new_major.strip()

    #This method updates a student's age
    def update_age(self, new_age):
        if new_age < 0:
            raise ValueError("Age can't be negative")
        self.age = new_age

    #This method converts the students information into a dictionary
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "major": self.major,
            "gpa": self.gpa
        }
    
    