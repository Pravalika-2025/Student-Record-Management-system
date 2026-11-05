# Student Record Management System

## 1. Project Overview

The Student Record Management System is a Python-based application designed to manage student information easily. It allows users to add, view, search, update and delete student records.

The application stores student information using CSV and JSON files, so records can be accessed even after closing the program.

## 2. Objectives

- To maintain student records digitally.
- To reduce manual record-keeping.
- To provide easy searching and updating of student details.
- To store student information in CSV and JSON formats.
- To handle invalid inputs and file-related errors.

## 3. Technologies Used

- Programming Language: Python
- IDE: Visual Studio Code
- Data Storage: CSV and JSON
- Python Libraries: csv, json

## 4. Main Features

1. **Add Student:** Enter and save new student details.
2. **View Students:** Display all available student records.
3. **Search Student:** Find a student using their Student ID.
4. **Update Student:** Modify existing student information.
5. **Delete Student:** Remove a student record.
6. **Exit:** Close the application.

## 5. Student Information

Each student record contains:

- Student ID
- Name
- Age
- Department
- Marks

## 6. Project File Structure

- main.py – Main application and menu.
- student.py – Student class and student details.
- file_handler.py – CSV and JSON file operations.
- students.csv – Stores student records in CSV format.
- students.json – Stores student records in JSON format.

## 7. How to Run the Project

1. Install Python 3.11 or a compatible version.
2. Open the project folder in Visual Studio Code.
3. Open the terminal.
4. Run the following command:

   `python main.py`

5. Select an option from the displayed menu.

## 8. Exception Handling

The project uses try-except blocks to handle invalid numerical inputs and file-related errors. This helps prevent unexpected program termination.

## 9. Conclusion

The Student Record Management System provides a simple and effective way to manage student information using Python. It demonstrates object-oriented programming, functions, file handling, CSV and JSON storage, and exception handling.

## 10. Future Enhancements

- Add a graphical user interface.
- Introduce database connectivity.
- Generate student performance reports.
- Add user authentication and access control.