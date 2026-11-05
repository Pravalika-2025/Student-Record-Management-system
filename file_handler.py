
import csv
import json
from student import Student

FILE_NAME = "students.csv"
JSON_FILE = "students.json"


# Save student records
def save_students(students):
    try:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Student ID", "Name", "Age", "Department", "Marks"
            ])

            for student in students:
                writer.writerow([
                    student.student_id,
                    student.name,
                    student.age,
                    student.department,
                    student.marks
                ])

        data = []

        for student in students:
            data.append({
                "student_id": student.student_id,
                "name": student.name,
                "age": student.age,
                "department": student.department,
                "marks": student.marks
            })

        with open(JSON_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("Records saved successfully!")

    except OSError as error:
        print("File saving error:", error)


# Load student records
def load_students():
    students = []

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = Student(
                    int(row["Student ID"]),
                    row["Name"],
                    int(row["Age"]),
                    row["Department"],
                    float(row["Marks"])
                )

                students.append(student)

    except FileNotFoundError:
        print("No existing student file found. Starting fresh.")

    except (ValueError, KeyError, csv.Error) as error:
        print("Error reading student records:", error)

    except OSError as error:
        print("File access error:", error)

    return students
