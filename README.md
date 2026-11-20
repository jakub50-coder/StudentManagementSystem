# Student Management System
A Python-based Student Management System that allows users to manage student records through a command-line interface. The application uses JSON data persistence to save student information between program executions.

## Overview
The Student Management System allows users to manage student information, including names, ages, majors, and GPAs.

The application uses JSON persistence to store student records in a file. This means that information is not lost when the program closes and can be loaded again the next time the application runs.

## Features
- **Add Students:** Add new students with their name, age, major, and GPA.
- **View Students:** Display all students currently stored in the system.
- **Search Students:** Find a student by name.
- **Update Students:** Modify a student's age, major, and GPA.
- **Delete Students:** Remove student records from the system.
- **Input Validation:** Validate student information and prevent invalid entries.
- **JSON Persistence:** Save student records to a JSON file and load them when the application starts.

## Technologies Used
- Python 3
- Object-Oriented Programming (OOP)
- JSON
- Git and GitHub

## Project Structure
StudentManagementSystem/
│
├── main.py
├── student.py
├── student_manager.py
├── students.json
├── README.md
└── .gitignore

### File Descriptions
- **main.py:** Contains the main menu and application logic. Handles user input and validates student information.
- **student.py:** Defines the `Student` class, which manages individual student information, displays student details, validates information, and converts student objects into dictionaries.
- **student_manager.py:** Defines the `StudentManager` class, which manages the student collection and handles adding, searching, updating, deleting, saving, and loading student records.
- **students.json:** Stores student information in JSON format so that records can be preserved between application executions.

## Installation and Usage
### Prerequisites

- Python 3 installed on your computer.

### Running the Application

1. Clone the repository:
   https://github.com/jakub50-coder/StudentManagementSystem.git
2. Navigate to the project directory:

   cd StudentManagementSystem

3. Run the application:

   python main.py

4. Follow the command-line menu to manage student records.

## Sample Data
The included `students.json` file contains two sample student records:

- John Smith
- Julia Roberts

Each record includes the student's name, age, major, and GPA. These records allow users to explore the application's functionality immediately after launching it.

## Future Improvements

- Implement a graphical user interface (GUI).
- Add database integration.
- Expand student search functionality.
